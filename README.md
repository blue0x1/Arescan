<h1 align="center">Arescan: Advanced Directory Discovery Tool</h1>

Arescan is a powerful web directory discovery tool that helps you uncover hidden directories and links on any website. By performing a breadth-first search, it efficiently scans websites and collects useful information that can be utilized for web security assessment, bug bounty hunting, or simply discovering new pages.

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

## Changelog

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

python3 Arescan.py <url> [-w <wordlist>] [-o <output>]


``` bash

python3 Arescan.py https://example.com -w path/to/wordlist.txt -o output.txt


<url> : The base URL to search.
-w <wordlist> (optional): Path to the wordlist file.
-o <output> (optional): Path to the output file.

```

## Output <br>
Arescan will print discovered URLs with their corresponding HTTP status codes. Once the scan is complete, it will display a list of all found URLs within the target domain. If an output file is specified, the found URLs will be saved in the file.
<br>

## License <br>
Arescan is released under the MIT License. See the [LICENSE](https://github.com/blue0x1/Arescan/blob/main/LICENSE) file for details.<br>
## Disclaimer
Arescan is intended for educational and legal purposes only. The author and contributors are not responsible for any misuse or damage caused by using this tool. Always obtain permission from the website owner before scanning their site.


