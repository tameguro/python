#coding:utf-8
import sys, codecs
import time
import requests
import pg8000
from bs4 import BeautifulSoup

url_ossdb_sample_root = 'https://oss-db.jp'

def main():
    soup = getBeautifulSoup(url_ossdb_sample_root + "/sample")
    ataglist = soup.find_all("a", class_="size-s black")

    question_dict_list = []

    for atag in ataglist:
        question_group_id = atag.get("href")
        question_dict_list.extend(makeQuestionsDictList(question_group_id))

    insertOrUpdateRecords(question_dict_list)

def makeQuestionsDictList(question_group_id):
    soup = getBeautifulSoup(url_ossdb_sample_root + question_group_id)
    page_title = soup.find("h2").text
    ataglist = soup.find_all("a", class_="size-s black")
    question_dict_list = []

    for atag in ataglist:
        url = atag.get("href")
        question_dict = getQuestionDict(page_title, url)
        question_dict_list.append(question_dict)

    #outputFile(question_dict_list)

    return question_dict_list

def getQuestionDict(page_title, url):
    print(url_ossdb_sample_root + url)

    soup = getBeautifulSoup(url_ossdb_sample_root + url)

    question = getSelectOne(soup, "div.question > h4")
    choices = soup.select("div.upper-latin > ol")
    if choices is None or len(choices) == 0:
        choices = soup.select("div.upper-latin > p")
    commentary = getSelectOne(soup, "div.answer > p")
    #answer = soup.find("strong")
    answer = getSelectOne(soup, "strong")

    url_array = url.split("/")
    tmp_question_group_id = url_array[2]
    tmp_exam_level_id = tmp_question_group_id.split("_")
    exam_level_id = tmp_exam_level_id[0]
    question_group_id = tmp_exam_level_id[1]
    question_id = url_array[3]

    question_dict = {
        'exam_level_id':exam_level_id,
        'question_group_id':question_group_id,
        'question_id':question_id,
        'page_title':page_title,
        'question':question,
        'choices':choices,
        'commentary':commentary,
        'answer':answer,
        'page_url':url_ossdb_sample_root + url,
    }

    return question_dict

def getBeautifulSoup(url):
    rq = requests.get(url)
    time.sleep(3)
    soup = BeautifulSoup(rq.content, 'lxml')
    return soup

def getSelectOne(soup, selector):
    tmp = soup.select_one(selector)

    if not tmp is None:
        rtn = tmp.text
    else:
        rtn = ""

    return rtn

def outputFile(question_dict_list):
    file_name = "oss_db_sample_questions.txt"
    f = codecs.open(file_name, 'a', 'utf-8')

    for question_dict in question_dict_list:
        print(question_dict['page_url'] + "\n", file=f)
        print(question_dict['page_title'] + "\n", file=f)
        print(question_dict['question'] + "\n", file=f)
        for choice in question_dict['choices']:
            print(choice.text + "\n", file=f)
        print(question_dict['commentary'] + "\n", file=f)
        print(question_dict['answer'] + "\n", file=f)

    f.close()

def insertOrUpdateRecords(question_dict_list):
    dbuser = "postgres"
    dbpassword = "password"
    dbdatabase = "oss_db"
    pg8000.paramstyle = 'qmark'
    conn = pg8000.connect(user=dbuser, password=dbpassword, database=dbdatabase)
    cur = conn.cursor()

    for question_dict in question_dict_list:
        exam_level_id = question_dict['exam_level_id']
        question_group_id = question_dict['question_group_id']
        question_id = question_dict['question_id']
        page_title = question_dict['page_title']
        question_dict['question']
        question_dict['commentary']
        question_dict['answer']
        question_dict['page_url']

        record_question_group_mst = (exam_level_id, question_group_id, page_title, page_title)
        cur.execute("INSERT INTO QUESTION_GROUP_MST VALUES (?,?,?) ON CONFLICT ON question_group_mst_pkey DO UPDATE SET question_group=?", record_question_group_mst)





# pythonコマンドで実行された場合にmain関数を呼び出す。これはモジュールとして他のファイルから
# インポートされたときに、main関数が実行されないようにするための、Pythonにおける一般的なイディオム。
if __name__ == '__main__':
    main()
