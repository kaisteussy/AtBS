import requests
import bs4
import re
import os

url = 'https://imgur.com/search?q='
imgur = 'https://imgur.com'
search = "monkey on a beach"

# Create images directory to store images
os.makedirs('images', exist_ok=True)

# Use 'requests' module to download search results
print(f'Searching for "{search}" on {imgur}...')
search_pg = requests.get(url + search)
search_pg.raise_for_status()

# Create beautiful soup object
search_page_soup = bs4.BeautifulSoup(search_pg.text, 'html.parser')

# Using beautiful soup, find all img tags
img_tags = search_page_soup.find_all('img')

# Add all src links to list
image_urls = [img['src'] for img in img_tags]

# Loop through all links to download each image
for image in image_urls:
    image_url = 'https:' + image
    req = requests.get(image_url)
    req.raise_for_status()
    print(image_url)

    # Save the image to the 'images' folder
    with open(os.path.join('images', os.path.basename(image_url)), 'wb') as image_file:
        for chunk in req.iter_content(100000):
            image_file.write(chunk)

    req.close()

search_pg.close()
