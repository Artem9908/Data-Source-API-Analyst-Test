import requests

def search_repositories(query, headers, per_page=30, page=1):
    """
    Search public repositories based on a query.
    """
    url = 'https://api.github.com/search/repositories'
    params = {'q': query, 'per_page': per_page, 'page': page}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def list_commits(owner, repo, headers, per_page=30, page=1):
    """
    List commits for a given repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'per_page': per_page, 'page': page}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_repository_contents(owner, repo, headers, path=''):
    """
    Get contents of a repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
