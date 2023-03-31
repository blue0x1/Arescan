#!/usr/bin/env python3

"""
Title: Arescan Advanced Directory Discovery Tool 
Author: Chokri Hammedi (blue0x1)
"""

print("\033[31m" + """


     /\                                  
    /  \   _ __ ___  ___  ___ __ _ _ __  
   / /\ \ | '__/ _ \/ __|/ __/ _` | '_ \ 
  / ____ \| | |  __/\__ \ (_| (_| | | | |
 /_/    \_\_|  \___||___/\___\__,_|_| |_|
                                           v 1.3 by blue0x1




""" + "\033[0m")

import random
import requests
from bs4 import BeautifulSoup
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib3
import signal
import os
import sys
from itertools import product
import socks
import socket
import time

def read_wordlist(wordlist_path):
    with open(wordlist_path, 'r') as f:
        words = f.read().splitlines()
    return words


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_links(soup, base_url):
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            if base_url in href:
                links.append(href)
    return links


def get_proxies():
    url = 'https://www.sslproxies.org/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    proxies_table_div = soup.find('div', {'class': 'table-responsive fpl-list'})
    if proxies_table_div is None:
        raise ValueError("Unable to find proxies table on website")
    proxies_table = proxies_table_div.find('table')
    proxies = []
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
            'ip': row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
        })
    return proxies


def get_random_proxy(proxies, auto_proxy=False):
    if auto_proxy:
        return random.choice(get_proxies())
    return random.choice(proxies) if proxies else None


def apply_rate_limiting_evasion(delay, auto_proxy=False, proxies=None):
    if delay:
        time.sleep(delay)
    if auto_proxy or proxies:
        while True:
            random_proxy = get_random_proxy(proxies, auto_proxy)
            
            proxy_address = f"http://{random_proxy['ip']}:{random_proxy['port']}"
            try:
                response = requests.get('http://httpbin.org/ip', proxies={'http': proxy_address, 'https': proxy_address})
                if response.ok:
                    print(f"Using proxy: {proxy_address}")
                    return {'http': proxy_address, 'https': proxy_address}
            except:
                pass
            time.sleep(60)



def process_url(url, base_url, user_agents, found_links, visited_urls, delay=0, auto_proxy=False, proxies=None):
    if url in visited_urls:
        return None

    headers = {'User-Agent': random.choice(user_agents)}

    try:
        proxies_config = apply_rate_limiting_evasion(args.delay, auto_proxy, proxies)
        if url.startswith("https://"):
            response = requests.get(url, headers=headers, proxies=proxies_config, verify=False)
        else:
            response = requests.get(url, headers=headers, proxies=proxies_config)
    except requests.exceptions.RequestException:
        return None

    if response.status_code == 200:
        if url not in found_links:
            found_links.append(url)
            print(f"\t{url} - 200 OK")
        soup = BeautifulSoup(response.content, 'html.parser')
        links = get_links(soup, base_url)
        return links
    return None


def find_directories(base_url, found_links, wordlist=None, output_file=None):
    """
    Perform a breadth-first search for directories.
    """
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'
    ]

    if wordlist:
        urls_to_search = [os.path.join(base_url, word) for word in wordlist]
    else:
        urls_to_search = [base_url]

    visited_urls = set()

    max_threads = 20

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        while urls_to_search:
            future_to_url = {executor.submit(process_url, url, base_url, user_agents, found_links, visited_urls, args.delay, args.auto_proxy, proxies): url
                             for url in urls_to_search}


            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    links = future.result()
                    if links:
                        for link in links:
                            if link.startswith(base_url) and link not in visited_urls and link not in urls_to_search:
                                urls_to_search.append(link)
                except Exception as e:
                    print(f"Error processing {url}: {e}")

                visited_urls.add(url)

    print("\nFound URLs:")
    if output_file:
        with open(output_file, 'a') as f:
            for link in found_links:
                print(f"\t{link}")
                f.write(f"{link}\n")
    else:
        for link in found_links:
            print(f"\t{link}")


def signals(sig, frame, found_links, output_file):
    answer = input("\nDo you want to stop the search? (y/n): ").lower().strip()
    if answer == 'y':
        print("Saving the current output...")
        with open(output_file, 'a') as f:
            for link in found_links:
                f.write(f"{link}\n")
        sys.exit(0)


found_links = []
signal.signal(signal.SIGINT, lambda sig, frame: signals(sig, frame, found_links, args.output))


def append_extensions(words, extensions):
    extended_words = set(words)
    for word in words:
        for ext in extensions:
            extended_words.add(word + ext)
    return list(extended_words)

def parse_robots_txt(url):
    try:
        response = requests.get(url + '/robots.txt')
        if response.status_code == 200:
            return response.text.splitlines()
    except requests.exceptions.RequestException:
        pass
    return []


def is_allowed(url, rules):
    for rule in rules:
        if rule.startswith('Disallow:'):
            disallowed_path = rule.split(' ')[1]
            if url.startswith(disallowed_path):
                return False
    return True


def fuzz(wordlist, fuzzing_chars="0123456789-_"):
    fuzzed_words = set(wordlist)
    for word in wordlist:
        for char in fuzzing_chars:
            fuzzed_words.add(word + char)
    return list(fuzzed_words)


def find_directories_recursive(base_url, found_links, wordlist=None, output_file=None, depth=0, max_depth=3):
    if depth > max_depth:
        return

    print(f"\nScanning depth {depth}: {base_url}")
    new_links = find_directories(base_url, found_links, wordlist, output_file)

    for link in new_links:
        if link.endswith('/'):
            find_directories_recursive(link, found_links, wordlist, output_file, depth=depth + 1, max_depth=max_depth)


if __name__ == '__main__':

    
    
    parser = argparse.ArgumentParser(description='Arescan Advanced Directory Discovery Tool')
    parser.add_argument('url', help='The base URL to search')
    parser.add_argument('-w', '--wordlist', help='Path to the wordlist file', default=None)
    parser.add_argument('-o', '--output', help='Path to the output file', default='Ares-autosave.txt')
    parser.add_argument('-r', '--recursive', help='Enable recursive search (default: 3 levels deep)',
                        action='store_true')
    parser.add_argument('-f', '--fuzzing', help='Enable fuzzing to discover hidden files, directories, or parameters',
                        action='store_true')
    parser.add_argument('-d', '--depth', help='Maximum recursion depth (default: 3)', default=3, type=int)
    parser.add_argument('-e', '--extensions',
                        help='Comma-separated list of file extensions to search (e.g., .php,.html)', default='')
    parser.add_argument('--auto-proxy', action='store_true', help='Automatically use proxies from www.sslproxies.org')
    parser.add_argument('-p', '--proxies', help='Path to the proxy list file (one proxy per line)', default=None)
    parser.add_argument('-l', '--delay', help='Delay between requests in seconds (default: 0)', default=0, type=float)
    parser.add_argument('-t', '--tor', help='Enable Tor support', action='store_true')

    args = parser.parse_args()

    print(f"Scanning : {args.url} \n")

    wordlist = None
    if args.wordlist:
        wordlist = read_wordlist(args.wordlist)
        if args.fuzzing:
            wordlist = fuzz(wordlist)

    extensions = args.extensions.split(',') if args.extensions else []
    if extensions:
        wordlist = append_extensions(wordlist, extensions)

    proxies = []
    if args.proxies:
        with open(args.proxies, 'r') as f:
            for line in f:
                ip, port = line.strip().split(':')
                proxies.append({'ip': ip, 'port': port})

    delay = args.delay

    robot_rules = parse_robots_txt(args.url)

    if args.tor:
        try:
            socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
            socket.socket = socks.socksocket
            print("Tor support enabled.")
        except Exception as e:
            print(f"Error enabling Tor support: {e}")
            sys.exit(1)

    
    if args.recursive:
        find_directories_recursive(args.url, found_links, wordlist, args.output, max_depth=args.depth)
    else:
        find_directories(args.url, found_links, wordlist, args.output)

    
