from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import pymongo

url = 'https://mars.nasa.gov/news/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.text
print(title)

executable_path = {'executable_path': './chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('a', class_='button fancybox')
    
for image in images:
    href = image["data-fancybox-href"]
    print('https://www.jpl.nasa.gov' + href)
    
featured_image_url = 'https://www.jpl.nasa.gov' + href

url = 'https://space-facts.com/mars/'

tables = pd.read_html(url)
tables

type(tables)

df = tables[0]
df.columns = [' ',' ']
df.head()

html_table = df.to_html()
html_table

conn = 'mongodb://localhost:27107'
client = pymongo.MongoClient(conn)
db = client.mars
collection = db.hemispheres

hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemisphere_url)
html=browser.html

soup = BeautifulSoup(html, 'html.parser')

hemisphere_image_urls = []

links = browser.find_by_css('a.product-item h3')

for l in range(len(links)):
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[l].click()
    sample_link=browser.links.find_by_text('Sample').first
    hemisphere['url'] = sample_link['href']
    hemisphere['title']=browser.find_by_css('h2.title').text
    hemisphere_image_urls.append(hemisphere)
    browser.back()

hemisphere_image_urls    