import os
from dotenv import load_dotenv
import argparse
import requests
from urllib.parse import urlparse


def shorten_link(token: str, url: str) -> str:
    response = requests.post(
        'https://api-ssl.bitly.com/v4/bitlinks',
        headers={'Authorization': f'Bearer {token}'},
        json={'long_url': url},
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token: str, url: str) -> str:
    parsed_url = urlparse(url)
    url = f'{parsed_url.netloc}{parsed_url.path}'
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary',
        headers={'Authorization': f'Bearer {token}'},
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token: str, url: str) -> bool:
    parsed_url = urlparse(url)
    url = f'{parsed_url.netloc}{parsed_url.path}'
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url}',
        headers={'Authorization': f'Bearer {token}'},
    )
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    bitly_api_key = os.getenv('BITLY_API_KEY')
    parser = argparse.ArgumentParser(
        description="""Converts link to bitly short link.
        Shows total clicks if shortened bitly link has given.
        """
    )
    parser.add_argument('-l', '--link', help='link to analyze', type=str)
    args = parser.parse_args()
    link = args.link
    if is_bitlink(bitly_api_key, link):
        print(f'Clicks count {count_clicks(bitly_api_key, link)}')
    else:
        print(f'Bitlink {shorten_link(bitly_api_key, link)}')
