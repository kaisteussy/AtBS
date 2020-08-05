import requests
import bs4

website_to_validate = 'https://blogger.com'
errors = []  # List of links that returned errors on download
validated_links = []  # List of verified links

# Download the main website to begin validation on
req = requests.get(website_to_validate)
req.raise_for_status()

# Create Beautiful Soup object to parse html
soup = bs4.BeautifulSoup(req.text, 'html.parser')

# Find all hyperlinks
hyperlinks = soup.find_all('a', href=True)

# Loop through each hyperlink
for link in hyperlinks:
    # Isolate the hyperlink from the tag and store in string
    url_string = link.get('href')
    # Check for full hyperlink syntax. If partial, convert to full and store in full_url
    if url_string.startswith('http'):
        full_url = url_string
    elif url_string.startswith('//'):
        full_url = 'https:' + url_string
    elif url_string.startswith('#'):
        full_url = website_to_validate + url_string

    # Attempt to download the page. If error, add to errors list.
    req = requests.get(full_url)
    try:
        req.raise_for_status()
        print('Link validated...')
        validated_links.append(full_url)
    except Exception as exc:
        print(f'Broken link detected...')
        errors.append(full_url)
    req.close()

# Print out all broken links
if errors:
    print('The following links were unable to be downloaded:')
    for link in errors:
        print(link)

req.close()
