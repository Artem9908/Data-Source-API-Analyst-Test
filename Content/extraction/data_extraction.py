import requests
import json
import os

def search_repositories(query, headers, per_page=30, page=1):
    """
    Search public repositories based on a query.
    """
    url = 'https://api.github.com/search/repositories'
    params = {'q': query, 'per_page': per_page, 'page': page}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    
    # Save raw response
    save_response(data, 'search_repositories')
    
    # Clean data
    cleaned_data = [
        {
            'id': repo['id'],
            'name': repo['name'],
            'full_name': repo['full_name'],
            'html_url': repo['html_url'],
            'description': repo['description'],
            'owner': repo['owner']['login'],
            'stargazers_count': repo['stargazers_count'],
            'forks_count': repo['forks_count'],
            'language': repo['language']
        }
        for repo in data.get('items', [])
    ]
    
    # Save cleaned data
    save_response(cleaned_data, 'cleaned_search_repositories')
    
    return cleaned_data

def list_commits(owner, repo, headers, per_page=30, page=1):
    """
    List commits for a given repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'per_page': per_page, 'page': page}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    
    # Save raw response
    save_response(data, f'commits_{owner}_{repo}')
    
    # Clean data
    cleaned_data = [
        {
            'sha': commit['sha'],
            'author': commit['commit']['author']['name'],
            'date': commit['commit']['author']['date'],
            'message': commit['commit']['message'],
            'url': commit['html_url']
        }
        for commit in data
    ]
    
    # Save cleaned data
    save_response(cleaned_data, f'cleaned_commits_{owner}_{repo}')
    
    return cleaned_data

def get_repository_contents(owner, repo, headers, path=''):
    """
    Get contents of a repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    # Save raw response
    save_response(data, f'contents_{owner}_{repo}_{path.replace("/", "_")}')
    
    # Clean data
    cleaned_data = [
        {
            'name': item['name'],
            'path': item['path'],
            'type': item['type'],
            'download_url': item['download_url']
        }
        for item in data
    ]
    
    # Save cleaned data
    save_response(cleaned_data, f'cleaned_contents_{owner}_{repo}_{path.replace("/", "_")}')
    
    return cleaned_data

def save_response(data, filename):
    """
    Save API response data to a JSON file.
    """
    directory = 'saved_responses'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, f'{filename}.json')
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
