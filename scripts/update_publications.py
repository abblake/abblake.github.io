import yaml
import os
from scholarly import scholarly

def fetch_publications_from_scholar():
    """
    Fetch publications from Google Scholar using ID from environment variable
    """
    scholar_id = os.environ.get('SCHOLAR_ID')
    if not scholar_id:
        print("Error: SCHOLAR_ID environment variable not set")
        return
    
    try:
        print(f"Fetching publications for Scholar ID: {scholar_id}")
        
        # Search for the author by their Scholar ID
        search_query = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(search_query)
        
        # Get all publications
        publications = []
        
        for pub in author['publications']:
            # Fill in details for each publication
            pub_details = scholarly.fill(pub)
            
            # Extract relevant information
            publication = {
                'title': pub_details.get('bib', {}).get('title', 'Unknown Title'),
                'authors': pub_details.get('bib', {}).get('author', 'Unknown Authors'),
                'venue': pub_details.get('bib', {}).get('venue', 'Unknown Venue'),
                'year': pub_details.get('bib', {}).get('pub_year', 'Unknown Year'),
                'citations': pub_details.get('num_citations', 0),
                'url': pub_details.get('pub_url', ''),
                'abstract': pub_details.get('bib', {}).get('abstract', '')[:200] + '...' if pub_details.get('bib', {}).get('abstract') else ''
            }
            
            # Format the date
            if publication['year'] and publication['year'] != 'Unknown Year':
                try:
                    year = int(publication['year'])
                    publication['date'] = f"Jan {year}"
                except:
                    publication['date'] = publication['year']
            else:
                publication['date'] = "Unknown"
            
            publications.append(publication)
        
        # Sort by year (most recent first)
        publications.sort(key=lambda x: int(x.get('year', 0)) if str(x.get('year', '')).isdigit() else 0, reverse=True)
        
        # Create _data directory if it doesn't exist
        os.makedirs('_data', exist_ok=True)
        
        # Write to YAML file for Jekyll
        with open('_data/publications.yml', 'w', encoding='utf-8') as f:
            yaml.dump(publications, f, default_flow_style=False, allow_unicode=True)
        
        print(f"Successfully fetched {len(publications)} publications!")
        print("Saved to _data/publications.yml")
        
    except Exception as e:
        print(f"Error fetching publications: {e}")

if __name__ == "__main__":
    fetch_publications_from_scholar()
