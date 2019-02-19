import requests
from bs4 import BeautifulSoup

url_ossdb_sample_root = 'https://oss-db.jp'

def main():

    rq = requests.get(url_ossdb_sample_root + "/sample")
    soup = BeautifulSoup(rq.content, 'lxml')

    ataglist = soup.find_all("a", class_="size-s black")

    for atag in ataglist:
        #txt = atag.text
        url = atag.get("href")
        getQuestionUrl(url)

def getQuestionUrl(url):

    rq = requests.get(url_ossdb_sample_root + url)
    soup = BeautifulSoup(rq.content, 'lxml')
    ataglist = soup.find_all("a", class_="size-s black")

    for atag in ataglist:
        url = atag.get("href")
        getQuestionAndAnswer(url)

def getQuestionAndAnswer(url):
    print(url_ossdb_sample_root + url)
    rq = requests.get(url_ossdb_sample_root + url)
    soup = BeautifulSoup(rq.content, 'lxml')
    question = soup.select(".question")
    # 回答の選択肢の取得
    answer = soup.select(".answer")

    print(question)
    print(answer)

# pythonコマンドで実行された場合にmain関数を呼び出す。これはモジュールとして他のファイルから
# インポートされたときに、main関数が実行されないようにするための、Pythonにおける一般的なイディオム。
if __name__ == '__main__':
    main()
