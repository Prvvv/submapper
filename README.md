# Submapper
## A subdomain enumeration tool desgined to find WAF'S and Vulnerable 404 pages.

## Submapper can detect:

- Amazon WAF's 
- Cloudflare WAF's 
- 404 Pages (Potentially Vulnerable to takeover)
- Subdomains Public IP Address and ISP data 

## How it works:

Submapper sends a constant but discrete stream of HTTP/1.1 requests to commonly listed sudomains found on most websites and domains.

Submapper uses 3 main techniques all at once to gather as many potential subdomains as possible.

***Brute force:***  submapper uses brute force ranging from small text ranges (a-z/aaaaa - zzzzz) and numerical ranges (1 - 10/1 - 1000) ect, to find short charactered and numbered subdomains.

***wordlisting:*** submapper also uses many wordlists made up of common names, directories, services ect that other mainstream site builders and domains use to list out many potentially interesting or vulnerable subdomains.

***common directory listing:*** along with using common words, submapper also uses confirmed subdomains known to appear on other websites, using many different common names of pluggins and services to best find and enumerate otherwise tricky subdomain names.

## Efficiency

All while remaining as un-noisy as possible, submapper uses only ***1*** file and multiple different threads on each task.

Submapper will also index all currently found subdomains and list them in its own cache to avoid finding the same subdomain twice, giving the best and most reliable results.

![](https://i.ibb.co/59ctRJZ/submapper.png)

## Installation

Submapper requires ***python3.9+*** with ***pip3 or higher*** installed with the following dependancies:

- Colorama (https://pypi.org/project/colorama/)

- Faker (https://pypi.org/project/Faker/)

- Requests (https://pypi.org/project/requests/)

Currently works and tested on:

- ***Linux***
- ***Windows 10/11***










