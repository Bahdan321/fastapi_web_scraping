import requests

def parse_images_custom_search(query, api_key, cx):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'searchType': 'image',
        'q': query
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'items' in data:
        image_urls = [item['link'] for item in data['items']]
        return image_urls
    else:
        print("Failed to retrieve images.")
        return []

# Replace 'YOUR_API_KEY' and 'YOUR_CX' with your actual Google Custom Search API key and custom search engine ID
api_key = 'YOUR_API_KEY'
cx = 'YOUR_CX'
query = 'kitten'
images = parse_images_custom_search(query, api_key, cx)
print(images)