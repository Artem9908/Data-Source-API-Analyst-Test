import json
import os

def load_raw_response(filename):
    """
    Load raw API response from a JSON file.
    """
    filepath = os.path.join('saved_responses', f'{filename}.json')
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def save_cleaned_data(data, filename):
    """
    Save cleaned data to a JSON file.
    """
    directory = 'cleaned_data'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, f'{filename}.json')
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def clean_repository_data(raw_data):
    """
    Clean repository data by extracting relevant fields.
    """
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
        for repo in raw_data.get('items', [])
    ]
    return cleaned_data

def clean_commit_data(raw_data):
    """
    Clean commit data by extracting relevant fields.
    """
    cleaned_data = [
        {
            'sha': commit['sha'],
            'author': commit['commit']['author']['name'],
            'date': commit['commit']['author']['date'],
            'message': commit['commit']['message'],
            'url': commit['html_url']
        }
        for commit in raw_data
    ]
    return cleaned_data

def clean_content_data(raw_data):
    """
    Clean repository content data by extracting relevant fields.
    """
    cleaned_data = [
        {
            'name': item['name'],
            'path': item['path'],
            'type': item['type'],
            'download_url': item['download_url']
        }
        for item in raw_data
    ]
    return cleaned_data
