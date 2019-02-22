import time
import requests
from bs4 import BeautifulSoup

url_ossdb_sample_root = 'https://oss-db.jp'

def main():
    soup = getBeautifulSoup(url_ossdb_sample_root + "/sample")
    ataglist = soup.find_all("a", class_="size-s black")

    for atag in ataglist:
        #txt = atag.text
        url = atag.get("href")
        getQuestionUrl(url)

def getQuestionUrl(url):
    soup = getBeautifulSoup(url_ossdb_sample_root + url)
    ataglist = soup.find_all("a", class_="size-s black")

    for atag in ataglist:
        url = atag.get("href")
        getQuestionAndAnswer(url)

def getQuestionAndAnswer(url):
    soup = getBeautifulSoup(url_ossdb_sample_root + url)

    question = soup.select("div.question > h4")
    list = soup.select("div.upper-latin > ol")
    kaisetsu = soup.select_one("div.answer > p")
    answer = soup.find("strong")

    print(url_ossdb_sample_root + url)
    print(question)
    print(list)
    print(kaisetsu)
    print(answer)

def getBeautifulSoup(url):
    rq = requests.get(url)
    time.sleep(5)
    soup = BeautifulSoup(rq.content, 'lxml')
    return soup

# pythonコマンドで実行された場合にmain関数を呼び出す。これはモジュールとして他のファイルから
# インポートされたときに、main関数が実行されないようにするための、Pythonにおける一般的なイディオム。
if __name__ == '__main__':
    main()
