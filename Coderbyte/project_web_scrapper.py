import requests
from bs4 import BeautifulSoup

req = requests.get("https://thecleverprogrammer.com/")
soup =BeautifulSoup(req.content, "html.parser")
#print(soup.prettify())
print(soup.get_text()); ## to get the text
res =soup.title
print(res) # which returns with title tag and text inside it
print(res.get_text());## which retruns only text
