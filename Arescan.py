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
                                           v 1.0 by blue0x1
                                         
        
          

""" + "\033[0m")

import random
import requests
from bs4 import BeautifulSoup
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_links(soup, base_url):
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            if base_url in href:
                links.append(href)
    return links


def process_url(url, base_url, user_agents, found_links, visited_urls):
    if url in visited_urls:
        return None

    headers = {'User-Agent': random.choice(user_agents)}

    try:
        if url.startswith("https://"):
            response = requests.get(url, headers=headers, verify=False)
        else:
            response = requests.get(url, headers=headers)
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



def find_directories(base_url):
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

    urls_to_search = [base_url]
    visited_urls = set()
    found_links = []

    max_threads = 20

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        while urls_to_search:
            future_to_url = {executor.submit(process_url, url, base_url, user_agents, found_links, visited_urls): url for url in urls_to_search}
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
    for link in found_links:
        if link.startswith(base_url):
            print(f"\t{link}")




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Arescan Advanced Directory Discovery Tool')
    parser.add_argument('url', help='The base URL to search')
    args = parser.parse_args()

    find_directories(args.url)
