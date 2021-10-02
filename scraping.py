import requests
##import re
from bs4 import BeautifulSoup

result = requests.get("")

##print(result.status_code)
##
##print(result.headers)

src = result.content
##print(src)

soup = BeautifulSoup(src,'lxml')
##print(soup)
##links = soup.find_all('a',attrs={'href':re.compile("^http")})

urls = []

for link in soup.find_all("a"):
    if link.has_attr('href'):
##        if 'mp4' in link.get_text().lower():
            print(link.get("href"))
