import yaml
import os
from scholarly import scholarly
import time

def fetch_publications_from_scholar():
    """
    Fetch publications from Google Scholar using ID from environment variable
    """
    scholar_id = os.environ.get('SCHOLAR_ID')
    if not scholar_id:
        print("Error: SCHOLAR_ID environment variable not set")
        return
    
    print(f"Fetching publications for Scholar ID: {scholar_id}")
    print(f"Scholar ID length: {len(scholar_id)}")
    
    try:
        # Add some delay to be nice to Google Scholar
        time.sleep(2)
        
        print("Step 1: Searching for author...")
        search_query = scholarly.search_author_id(scholar_id)
        
        if search_query is None:
            print("❌ ERROR: No author found with this Scholar ID")
            print("This could mean:")
            print("  1. The Scholar ID is incorrect")
            print("  2. Your Google Scholar profile is not public")
            print("  3. The profile URL format has changed")
            return
        
        print("Step 2: Found author, filling details...")
        author = scholarly.fill(search_query)
        
        if author is None:
            print("❌ ERROR: Could not fill author details")
            return
            
        print(f"✅ Found author: {author.get('name', 'Unknown')}")
        print(f"   Affiliation: {author.get('affiliation', 'Unknown')}")
        print(f"   Interests: {author.get('interests', 'Unknown')}")
        
        # Check if publications exist
        publications_raw = author.get('publications', [])
        print(f"   Number of publications found: {len(publications_raw)}")
        
        if not publications_raw:
            print("⚠️  No publications found for this author")
            # Create empty publications file
            os.makedirs('_data', exist_ok=True)
            with open('_data/publications.yml', 'w', encoding='utf-8') as f:
                yaml.dump([], f)
            print("Created empty publications.yml file")
            return
        
        # Get detailed publication info
        publications = []
        
        print("Step 3: Processing publications...")
        for i, pub in enumerate(publications_raw):
            try:
                print(f"  Processing publication {i+1}/{len(publications_raw)}...")
                
                # Fill in details for each publication
                pub_details = scholarly.fill(pub)
                
                if pub_details is None:
                    print(f"    ⚠️  Could not get details for publication {i+1}")
                    continue
                
                # Extract relevant information
                bib = pub_details.get('bib', {})
                
                publication = {
                    'title': bib.get('title', 'Unknown Title'),
                    'authors': bib.get('author', 'Unknown Authors'),
                    'venue': bib.get('venue', 'Unknown Venue'),
                    'year': bib.get('pub_year', 'Unknown Year'),
                    'citations': pub_details.get('num_citations', 0),
                    'url': pub_details.get('pub_url', ''),
                    'abstract': bib.get('abstract', '')[:200] + '...' if bib.get('abstract') else ''
                }
                
                # Format the date
                if publication['year'] and publication['year'] != 'Unknown Year':
                    try:
                        year = int(publication['year'])
                        publication['date'] = f"Jan {year}"
                    except:
                        publication['date'] = str(publication['year'])
                else:
                    publication['date'] = "Unknown"
                
                publications.append(publication)
                print(f"    ✅ {publication['title'][:50]}... ({publication['year']})")
                
                # Add delay between requests
                time.sleep(1)
                
            except Exception as e:
                print(f"    ❌ Error processing publication {i+1}: {e}")
                continue
        
        print(f"Step 4: Successfully processed {len(publications)} publications")
        
        # Sort by year (most recent first)
        publications.sort(key=lambda x: int(x.get('year', 0)) if str(x.get('year', '')).isdigit() else 0, reverse=True)
        
        # Create _data directory if it doesn't exist
        os.makedirs('_data', exist_ok=True)
        
        # Write to YAML file for Jekyll
        with open('_data/publications.yml', 'w', encoding='utf-8') as f:
            yaml.dump(publications, f, default_flow_style=False, allow_unicode=True)
        
        print(f"✅ Successfully saved {len(publications)} publications to _data/publications.yml!")
        
        # Show a preview
        print("\nFirst publication preview:")
        if publications:
            pub = publications[0]
            print(f"  Title: {pub['title']}")
            print(f"  Authors: {pub['authors']}")
            print(f"  Year: {pub['year']}")
            print(f"  Citations: {pub['citations']}")
        
    except Exception as e:
        print(f"❌ Error fetching publications: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        print("Full traceback:")
        traceback.print_exc()

if __name__ == "__main__":
    fetch_publications_from_scholar()
