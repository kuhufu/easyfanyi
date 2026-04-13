#!/usr/bin/env python3
"""
EasyFanyi - Baidu Translation Tool
A command-line translation tool using Baidu API.
"""

import sys
import hashlib
import random
import json
import http.client
from urllib import parse


# API Configuration
API_CONFIG = {
    'appid': '20160922000029057',
    'secret_key': '2Dv2Qw9S0e7Z7zz7TrU9',
    'host': 'api.fanyi.baidu.com',
    'endpoint': '/api/trans/vip/translate',
    'from_lang': 'en',
    'to_lang': 'zh',
}


def generate_sign(query: str, salt: int) -> str:
    """Generate MD5 signature for Baidu API request.
    
    Args:
        query: The text to translate (URL encoded)
        salt: Random salt value
        
    Returns:
        MD5 hash signature
    """
    sign_str = (
        f"{API_CONFIG['appid']}{query}{salt}{API_CONFIG['secret_key']}"
    )
    return hashlib.md5(sign_str.encode('utf-8')).hexdigest()


def fetch_translation(word: str) -> dict:
    """Fetch translation data from Baidu API.
    
    Args:
        word: The word to translate
        
    Returns:
        JSON response from the API
        
    Raises:
        Exception: If the API request fails
    """
    query = parse.quote(word)
    salt = random.randint(32768, 65536)
    sign = generate_sign(query, salt)
    
    endpoint = (
        f"{API_CONFIG['endpoint']}?appid={API_CONFIG['appid']}"
        f"&q={query}&from={API_CONFIG['from_lang']}"
        f"&to={API_CONFIG['to_lang']}&salt={salt}&sign={sign}"
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


def display_translation(data: dict) -> None:
    """Display translation results.
    
    Args:
        data: Translation data from API
    """
    if 'trans_result' in data and len(data['trans_result']) > 0:
        print(data['trans_result'][0]['dst'])
    elif 'error_code' in data:
        print(f"API Error: {data.get('error_msg', 'Unknown error')}")
    else:
        print("No translation found.")


def main() -> int:
    """Main entry point.
    
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    if len(sys.argv) < 2:
        print("Usage: dic-baidu <word>")
        return 1
    
    word = sys.argv[1]
    
    try:
        data = fetch_translation(word)
        display_translation(data)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
