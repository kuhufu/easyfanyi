#!/usr/bin/env python3
"""
EasyFanyi - Youdao Translation Tool
A command-line translation tool using Youdao API.
"""

import sys
import json
import http.client
from urllib import parse


# API Configuration
API_CONFIG = {
    'keyfrom': 'easyfanyi',
    'key': '1929637537',
    'host': 'fanyi.youdao.com',
}


def fetch_translation(word: str) -> dict:
    """Fetch translation data from Youdao API.
    
    Args:
        word: The word to translate
        
    Returns:
        JSON response from the API
        
    Raises:
        Exception: If the API request fails
    """
    query = parse.quote(word)
    endpoint = (
        f'/openapi.do?keyfrom={API_CONFIG["keyfrom"]}'
        f'&key={API_CONFIG["key"]}'
        f'&type=data&doctype=json&version=1.1&q={query}'
    )
    
    connection = None
    try:
        connection = http.client.HTTPConnection(API_CONFIG['host'])
        connection.request('GET', endpoint)
        response = connection.getresponse()
        data = response.read().decode('utf-8')
        return json.loads(data)
    finally:
        if connection:
            connection.close()


def display_translation(data: dict, show_phonetic: bool = False) -> None:
    """Display translation results.
    
    Args:
        data: Translation data from API
        show_phonetic: Whether to show US phonetic transcription
    """
    basic = data.get('basic', {})
    
    if show_phonetic:
        phonetic = basic.get('us-phonetic', 'N/A')
        print(f"US Phonetic: {phonetic}")
    
    explains = basic.get('explains', [])
    if explains:
        for explanation in explains:
            print(explanation)
    else:
        print("No translation found.")


def main() -> int:
    """Main entry point.
    
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    if len(sys.argv) < 2:
        print("Usage: dic <word> [-p]")
        print("  -p: Show US phonetic transcription")
        return 1
    
    word = sys.argv[1]
    show_phonetic = '-p' in sys.argv or len(sys.argv) == 3
    
    try:
        data = fetch_translation(word)
        display_translation(data, show_phonetic)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
