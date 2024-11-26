from getpass import getpass

def get_github_token():
    """
    Securely prompt for the GitHub Personal Access Token (PAT).
    """
    token = getpass('Enter your GitHub Personal Access Token: ')
    return token

def create_headers(token):
    """
    Create headers for authenticated GitHub API requests.
    """
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    return headers
