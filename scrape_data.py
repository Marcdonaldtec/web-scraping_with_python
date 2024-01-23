import requests
from bs4 import BeautifulSoup
import csv


url = "https://lenouvelliste.com/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

featured_article_divs = soup.find_all('div', class_='lnv-featured-article-sm')

csv_file = open('output.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Description', 'Link', 'Image'])

for div in featured_article_divs:
    title_tag = div.find('h1')
    title = title_tag.text.strip() if title_tag else None

    description_tag = div.find('p')
    description = description_tag.text.strip() if description_tag else None

    link_tag = div.find('a', href=True)
    link = link_tag['href'] if link_tag else None

    image_tag = div.find('img', src=True)
    image = image_tag['src'] if image_tag else None

    csv_writer.writerow([title, description, link, image])

csv_file.close()
