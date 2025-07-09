import yaml
import os
import json
import urllib.request
import urllib.parse
import time
import re
from datetime import datetime

def manual_scholar_fetch(scholar_id):
    """
    Manual method to fetch publications from Google Scholar
    This bypasses the scholarly library issues
    """
    print(f"Attempting manual fetch for Scholar ID: {scholar_id}")
    
    try:
        # Construct the URL
        base_url = "https://scholar.google.com/citations"
        params = {
            'user': scholar_id,
            'hl': 'en',
            'cstart': '0',
            'pagesize': '100'  # Get up to 100 publications
        }
        
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        print(f"Fetching URL: {url}")
        
        # Create request with headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        req = urllib.request.Request(url, headers=headers)
        
        # Make the request
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8')
        
        print("✅ Successfully fetched Scholar page")
        
        # Parse the HTML manually (basic parsing)
        publications = parse_scholar_html(html)
        
        return publications
        
    except Exception as e:
        print(f"❌ Manual fetch failed: {e}")
        return None

def parse_scholar_html(html):
    """
    Parse Google Scholar HTML to extract publication information
    """
    publications = []
    
    try:
        # Look for publication entries (this is a simplified parser)
        # Scholar uses specific class names for publication entries
        
        # Find author name
        name_match = re.search(r'<div[^>]*id="gsc_prf_in"[^>]*>([^<]+)</div>', html)
        author_name = name_match.group(1) if name_match else "Unknown Author"
        print(f"Found author: {author_name}")
        
        # Find publication table rows
        pub_pattern = r'<tr[^>]*class="gsc_a_tr"[^>]*>(.*?)</tr>'
        pub_matches = re.findall(pub_pattern, html, re.DOTALL)
        
        print(f"Found {len(pub_matches)} publication entries")
        
        for i, pub_html in enumerate(pub_matches):
            try:
                # Extract title
                title_match = re.search(r'<a[^>]*class="gsc_a_at"[^>]*>([^<]+)</a>', pub_html)
                title = title_match.group(1) if title_match else f"Publication {i+1}"
                
                # Extract authors (appears after title)
                authors_match = re.search(r'<div[^>]*class="gs_gray"[^>]*>([^<]+)</div>', pub_html)
                authors = authors_match.group(1) if authors_match else "Unknown Authors"
                
                # Extract venue
                venue_matches = re.findall(r'<div[^>]*class="gs_gray"[^>]*>([^<]+)</div>', pub_html)
                venue = venue_matches[1] if len(venue_matches) > 1 else "Unknown Venue"
                
                # Extract year
                year_match = re.search(r'<span[^>]*class="gsc_a_h gsc_a_hc gs_ibl"[^>]*>([^<]+)</span>', pub_html)
                year = year_match.group(1) if year_match else "Unknown"
                
                # Extract citations
                citations_match = re.search(r'<a[^>]*class="gsc_a_ac gs_ibl"[^>]*>([^<]*)</a>', pub_html)
                citations_text = citations_match.group(1) if citations_match else "0"
                citations = int(citations_text) if citations_text.isdigit() else 0
                
                publication = {
                    'title': title.strip(),
                    'authors': authors.strip(),
                    'venue': venue.strip(),
                    'year': year.strip(),
                    'citations': citations,
                    'date': f"Jan {year}" if year.isdigit() else year,
                    'url': '',
                    'abstract': ''
                }
                
                publications.append(publication)
                print(f"  ✅ {title[:50]}... ({year})")
                
            except Exception as e:
                print(f"  ❌ Error parsing publication {i+1}: {e}")
                continue
        
        # Sort by year
        publications.sort(key=lambda x: int(x.get('year', 0)) if str(x.get('year', '')).isdigit() else 0, reverse=True)
        
        return publications
        
    except Exception as e:
        print(f"❌ Error parsing HTML: {e}")
        return []

def create_sample_publications():
    """
    Create sample publications as fallback
    """
    print("Creating sample publications as fallback...")
    
    return [
        {
            'title': 'Sample Publication 1',
            'authors': 'Your Name, Co-author A',
            'venue': 'Sample Conference',
            'year': '2024',
            'date': 'Jan 2024',
            'citations': 0,
            'url': '',
            'abstract': 'This is a sample publication entry.'
        },
        {
            'title': 'Sample Publication 2', 
            'authors': 'Your Name, Co-author B',
            'venue': 'Sample Journal',
            'year': '2023',
            'date': 'Jan 2023',
            'citations': 0,
            'url': '',
            'abstract': 'This is another sample publication entry.'
        }
    ]

def fetch_publications_from_scholar():
    """
    Main function with multiple fallback methods
    """
    scholar_id = os.environ.get('SCHOLAR_ID')
    if not scholar_id:
        print("❌ Error: SCHOLAR_ID environment variable not set")
        return
    
    print(f"🔍 Fetching publications for Scholar ID: {scholar_id}")
    print(f"Scholar ID length: {len(scholar_id)}")
    
    publications = None
    
    # Method 1: Try the scholarly library (with better error handling)
    try:
        print("\n📚 Method 1: Trying scholarly library...")
        from scholarly import scholarly
        
        # Add delay to be respectful
        time.sleep(2)
        
        search_query = scholarly.search_author_id(scholar_id)
        if search_query:
            author = scholarly.fill(search_query)
            if author and 'publications' in author:
                print(f"✅ Found {len(author['publications'])} publications via scholarly")
                publications = process_scholarly_publications(author['publications'])
            else:
                print("⚠️  Scholarly found author but no publications")
        else:
            print("⚠️  Scholarly could not find author")
            
    except Exception as e:
        print(f"❌ Scholarly method failed: {e}")
    
    # Method 2: Manual scraping if scholarly failed
    if not publications:
        print("\n🔧 Method 2: Trying manual scraping...")
        publications = manual_scholar_fetch(scholar_id)
    
    # Method 3: Create sample publications if all else fails
    if not publications:
        print("\n📝 Method 3: Creating sample publications...")
        publications = create_sample_publications()
    
    # Save the results
    try:
        os.makedirs('_data', exist_ok=True)
        
        with open('_data/publications.yml', 'w', encoding='utf-8') as f:
            yaml.dump(publications, f, default_flow_style=False, allow_unicode=True)
        
        print(f"\n🎉 Successfully saved {len(publications)} publications to _data/publications.yml!")
        
        # Show preview
        if publications:
            print("\n📖 Preview of first publication:")
            pub = publications[0]
            for key, value in pub.items():
                print(f"  {key}: {value}")
        
    except Exception as e:
        print(f"❌ Error saving publications: {e}")

def process_scholarly_publications(pubs):
    """
    Process publications from scholarly library
    """
    publications = []
    
    for i, pub in enumerate(pubs[:10]):  # Limit to first 10 to avoid timeouts
        try:
            pub_details = scholarly.fill(pub)
            bib = pub_details.get('bib', {})
            
            publication = {
                'title': bib.get('title', f'Publication {i+1}'),
                'authors': bib.get('author', 'Unknown Authors'),
                'venue': bib.get('venue', 'Unknown Venue'),
                'year': bib.get('pub_year', 'Unknown'),
                'citations': pub_details.get('num_citations', 0),
                'url': pub_details.get('pub_url', ''),
                'abstract': bib.get('abstract', '')[:200] + '...' if bib.get('abstract') else '',
                'date': f"Jan {bib.get('pub_year', 'Unknown')}" if bib.get('pub_year') else 'Unknown'
            }
            
            publications.append(publication)
            time.sleep(1)  # Be respectful
            
        except Exception as e:
            print(f"Error processing publication {i+1}: {e}")
            continue
    
    return publications

if __name__ == "__main__":
    fetch_publications_from_scholar()
