import requests
from bs4 import BeautifulSoup

def fetch_headlines():
    url = "https://www.bbc.com/news"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(" Error fetching the page:", e)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # BBC usually uses <h3> tags with class "gs-c-promo-heading__title"
    headlines = soup.find_all('h3')
    
    extracted = []
    for tag in headlines:
        text = tag.get_text(strip=True)
        if text:
            extracted.append(text)

    return extracted

def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding='utf-8') as f:
        for i, headline in enumerate(headlines, 1):
            f.write(f"{i}. {headline}\n")

if __name__ == "__main__":
    print("Fetching top news headlines...\n")
    headlines = fetch_headlines()

    if headlines:
        save_to_file(headlines)
        print(f" {len(headlines)} headlines saved to 'headlines.txt'")
    else:
        print("No headlines found.")
