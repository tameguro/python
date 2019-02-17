import requests
from bs4 import BeautifulSoup

def main():

    url_ossdb_sample_root = 'https://oss-db.jp/measures/'
    url_ossdb_sample = 'sample.shtml'

    rq = requests.get(url_ossdb_sample_root + "/" + url_ossdb_sample)
    soup = BeautifulSoup(rq.content, 'lxml')

    silver = soup.find(class_="silver_sample")
    ataglist = silver.find_all("a")

    for atag in ataglist:
        txt = atag.text
        url = atag.get("href")

        if url is not None:
            req = requests.get(url_ossdb_sample_root + "/" + url)
            sample_soup = BeautifulSoup(req.content, 'lxml')
            silver_sample = sample_soup.find(class_="silver_sample")
            h3list = silver_sample.find_all("h3")

            for h3tag in h3list:
                detail_html = h3tag.a.get("href")
                detail_req = requests.get(url_ossdb_sample_root + "/" + detail_html)
                detail_soup = BeautifulSoup(detail_req.content, 'lxml')
                div_silver_sample = detail_soup.find(class_="silver_sample")

                if div_silver_sample is None:
                    div_silver_sample = detail_soup.find(id="section_sample")
                    q = detail_soup.find(class_="que")
                else:
                    q = div_silver_sample.find_all("span")[1].string

                sel = div_silver_sample.find_all("ol")
                ans = div_silver_sample.find(class_="kaitou")

                print(detail_html)
                print(q)
                print(sel)
                print(kaitou)
                #soup = BeautifulSoup(h3tag, 'lxml')
                #print(h3tag)
                #atag = soup.find("a")
                #url = atag.get("href")
                #print(url)

def getUrlList(h3list):
    for h3tag in h3list:
        soup = BeautifulSoup(h3tag, 'lxml')
        atag = soup.find("a")
        url = atag.get("href")
        print(url)

    return

# pythonコマンドで実行された場合にmain関数を呼び出す。これはモジュールとして他のファイルから
# インポートされたときに、main関数が実行されないようにするための、Pythonにおける一般的なイディオム。
if __name__ == '__main__':
    main()
