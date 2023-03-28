<h1 align="center">Arescan: Advanced Directory Discovery Tool</h1>

<br>Arescan is a powerful web directory discovery tool that helps you uncover hidden directories and links on any website. By performing a breadth-first search, it efficiently scans websites and collects useful information that can be utilized for web security assessment, bug bounty hunting, or simply discovering new pages.
<br>
## Features

- Accelerated scanning performance
- Stealth capabilities
- Comprehensive link examination
- Robust connection security
- Advanced HTML processing
- Python 3 optimization



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
## Output <br>
Arescan will print discovered URLs with their corresponding HTTP status codes. Once the scan is complete, it will display a list of all found URLs within the target domain.<br>


## Disclaimer
Arescan is intended for educational and legal purposes only. The author and contributors are not responsible for any misuse or damage caused by using this tool. Always obtain permission from the website owner before scanning their site.


