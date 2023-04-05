<h1 align="center">Arescan: Advanced Directory Discovery Tool</h1>

Arescan is a powerful web directory discovery tool that helps you uncover hidden directories and links on any website. By performing a breadth-first search, it efficiently scans websites and collects useful information that can be utilized for web security assessment, bug bounty hunting, or simply discovering new pages.



![Ares](https://e1.pxfuel.com/desktop-wallpaper/687/39/desktop-wallpaper-god-of-war-ares-backgrounds-god-of-war-monster.jpg)


## Features

- Accelerated scanning performance with multi-threading
- Stealth capabilities with randomized user agents
- Comprehensive link examination
- Robust connection security
- Advanced HTML processing with Beautiful Soup 4
- Customizable wordlists
- Supports pausing the search and saving progress.
- Output to a file for easy post-processing
- Python 3 optimization
- Recursive directory scanning
- Fuzzing to discover hidden files, directories, or parameters
- Ability to specify maximum recursion depth
- Support for file extensions search
- Support for proxy list and rate limiting
- Support for Tor network
- Support for automatically select proxies

## Changelog
### v1.3 
- Added a new option to enable automatic proxy usage
- Added autosave

### Fixes:
Fixed an issue where proxies were not being used properly.

### v1.2 
- Added support for recursive search
- Added support for file/directory fuzzing
- Added support for searching specific file extensions
- Added support for using proxies
- Added option for delay between requests
- Added Tor support

### v1.1

- Added multi-threading support for faster scanning
- Added support for custom wordlists
- Supports the ability to pause and resume the search process.
- Fixed a bug when using a wordlist

### v1.0

- Initial release

## Requirements

- Python 3.x
- Beautiful Soup 4
- Requests



## Installation <br>
Clone the Arescan repository:<br>
``` bash

git clone https://github.com/blue0x1/Arescan.git
```
Change to the Arescan directory:<br>
``` bash

cd Arescan
```
Install the required Python packages:
``` bash
pip install -r requirements.txt
```
## Usage <br>
``` bash
python3 Arescan.py <url>
```
Replace <url> with the base URL of the website you want to scan.

## Example <br>
``` bash
python3 Arescan.py https://example.com
  ```
## Advanced Options

python3 Arescan.py <url> [-w <wordlist>] [-o <output>] [-r] [-f] [-d <depth>] [-e <extensions>] [-p <proxies>] [-l <delay>] [-t]



``` bash

python3 Arescan.py http://example.com -w wordlist.txt -o output.txt -r -f -d 5 -e .php,.html -p proxies.txt -l 1 -t



<url>: The base URL to search.
-w <wordlist> (optional): Path to the wordlist file.
-o <output> (optional): Path to the output file.
-r (optional): Enable recursive search (default: 3 levels deep).
-f (optional): Enable fuzzing to discover hidden files, directories, or parameters.
-d <depth> (optional): Maximum recursion depth (default: 3).
-e <extensions> (optional): Comma-separated list of file extensions to search (e.g., .php,.html).
--auto-proxy (optional): Automatically use proxies
-p <proxies> (optional): Path to the proxy list file (one proxy per line).
-l <delay> (optional): Delay between requests in seconds (default: 0).
-t (optional): Enable Tor support.

```
This will perform a recursive search on http://example.com, using the wordlist.txt wordlist file, and saving the output to output.txt. The search will be up to 5 levels deep, and will include fuzzing to discover hidden files and directories with the extensions .php and .html. The search will be rate-limited by a delay of 1 second between requests, using the proxies listed in proxies.txt. Finally, Tor support will be enabled.

## Output <br>
Arescan will print discovered URLs with their corresponding HTTP status codes. Once the scan is complete, it will display a list of all found URLs within the target domain. If an output file is specified, the found URLs will be saved in the file.
<br>

## License <br>
Arescan is released under the MIT License. See the [LICENSE](https://github.com/blue0x1/Arescan/blob/main/LICENSE) file for details.<br>
## Disclaimer
Arescan is intended for educational and legal purposes only. The author is not responsible for any misuse or damage caused by using this tool. Always obtain permission from the website owner before scanning their site.


