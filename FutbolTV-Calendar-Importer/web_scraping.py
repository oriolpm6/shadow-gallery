# web_scraping.py
import requests
from bs4 import BeautifulSoup

def extract_match_information(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all match div elements
        match_divs = soup.find_all('div', class_='match')

        match_data = []
        for match_div in match_divs:
            # Extract relevant information for each match
            match_info = {
                'url': match_div.find('meta', itemprop='url')['content'],
                'name': match_div.find('meta', itemprop='name')['content'],
                'description': match_div.find('meta', itemprop='description')['content'],
                'start_date': match_div.find('meta', itemprop='startDate')['content'],
                'duration': match_div.find('meta', itemprop='duration')['content'],
                'start_time': match_div.find('div', class_='m_time').text.strip(),
                'home_team': match_div.find('span', itemprop='homeTeam').text.strip(),
                'away_team': match_div.find('span', itemprop='awayTeam').text.strip(),
                'channels': [channel.text.strip() for channel in match_div.find_all('span', class_='channelLnk')],
            }
            match_data.append(match_info)

        return match_data

    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
        return []

# Example usage
# match_data = extract_match_information("https://futboltv.info")
# print(match_data)
