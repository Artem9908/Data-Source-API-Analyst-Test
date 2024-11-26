import requests

def safe_request(url, headers, params=None):
    """
    Make a safe API request with error handling.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        status_code = response.status_code
        handle_http_error(status_code, http_err)
    except Exception as err:
        print(f'An error occurred: {err}')
    return None

def handle_http_error(status_code, http_err):
    """
    Handle HTTP errors based on status code.
    """
    if status_code == 401:
        print('Error 401: Unauthorized. Check your authentication token.')
    elif status_code == 403:
        print('Error 403: Forbidden. You might have hit the rate limit.')
    elif status_code == 404:
        print('Error 404: Not Found. Check the URL and parameters.')
    else:
        print(f'HTTP error occurred: {http_err}')
