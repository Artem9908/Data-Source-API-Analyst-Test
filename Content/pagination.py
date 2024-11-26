import requests

def fetch_all_pages(url, headers, params=None):
    """
    Fetch all pages of a paginated API response.
    """
    items = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        # Handle different response structures
        if isinstance(data, dict) and 'items' in data:
            items.extend(data['items'])
        elif isinstance(data, list):
            items.extend(data)
        # Check for next page
        if 'next' in response.links:
            url = response.links['next']['url']
            params = None  # Params are included in the 'next' URL
        else:
            url = None
    return items
