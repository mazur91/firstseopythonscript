import urllib.request
 
url = "http://www.google.com/ping?sitemap=https://www.example.com/sitemap.xml"
response = urllib.request.urlopen(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.read(), "html.parser")
print(soup.find("h2").text)

