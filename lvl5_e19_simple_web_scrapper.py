"""
Simple Web Scraper (BeautifulSoup)
    Use `requests` and `BeautifulSoup` to scrape the headlines from 
    a news website (please check the site's `robots.txt` first!).
    Store the headlines and their links in a structured format 
    (e.g., a list of dictionaries, a CSV file).
"""
import requests
from bs4 import BeautifulSoup

# Get html content
url = "https://www.europapress.es/"
response = requests.get(url)
html_content = response.text

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Extract article's title and link and store in a list of dictionarys
data = []
articulos = soup.find_all('article')
for articulo in articulos:
    titulo = articulo.find('h2').get_text()
    link = articulo.find('a').get('href')
    # print(f"Título: {titulo:<25} -==###==- Enlace: {link:<20} ")
    data.append({'titulo':titulo, 'link':link})

print(data)