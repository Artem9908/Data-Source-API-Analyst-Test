import requests
import time

def check_rate_limit(headers):
    """
    Check the current rate limit status.
    """
    url = 'https://api.github.com/rate_limit'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    remaining = data['resources']['core']['remaining']
    reset_time = data['resources']['core']['reset']
    return remaining, reset_time

def wait_if_rate_limited(headers):
    """
    Wait until the rate limit resets if limit is reached.
    """
    remaining, reset_time = check_rate_limit(headers)
    if remaining == 0:
        wait_time = reset_time - int(time.time()) + 1
        print(f'Rate limit exceeded. Waiting for {wait_time} seconds.')
        time.sleep(wait_time)
