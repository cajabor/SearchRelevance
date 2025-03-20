import requests
from bs4 import BeautifulSoup

def scrape_bing_search(query):
    # Construct the Bing search URL
    url = f"https://www.bing.com/search?q={query}"
    
    # Send a GET request to the Bing search page
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch Bing search results. Status code: {response.status_code}")
        return None
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract search result titles and links
    results = []
    for item in soup.find_all('li', class_='b_algo'):
        title = item.find('h2')
        link = item.find('a')
        summary = item.find('p')
        if title and link:
            results.append({
                'title': title.text,
                'link': link['href'],
                'summary': summary.text if summary else 'Summary Not Found'
            })
    
    return results

# Example usage
if __name__ == "__main__":
    search_query = "Who is the president"
    search_results = scrape_bing_search(search_query)
    
    if search_results:
        for idx, result in enumerate(search_results, start=1):
            print(f"{idx}. {result['title']}: {result['link']} - {result['summary']}\n")