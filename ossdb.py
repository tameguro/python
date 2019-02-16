import requests
from bs4 import BeautifulSoup

url_ossdb_sample_root = 'https://oss-db.jp/measures/'
url_ossdb_sample = 'sample.shtml'

rq = requests.get(url_ossdb_sample_root + "/" + url_ossdb_sample)
soup = BeautifulSoup(rq.content, 'html.parser')

silver = soup.find(class_="silver_sample")
aaa = silver.find_all("a")

for atag in aaa:
    txt = atag.text
    url = atag.get("href")

    if url is not None:
        print(url + ":" + txt)
        req = requests.get(url_ossdb_sample_root + "/" + url)
        sample_soup = BeautifulSoup(req.content, 'html.parser')
        print(sample_soup)
