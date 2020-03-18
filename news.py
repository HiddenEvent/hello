import json
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

# sbs 뉴스기준 최신 코로나 뉴스
url = "https://news.sbs.co.kr/news/newsHotIssueList.do?tagId=10000050973"
base_url = "https://news.sbs.co.kr"
soup = BeautifulSoup(urllib.request.urlopen(url).read().decode('utf-8'), "html.parser")
data1 = soup.find_all('a', {'class': 'news'})

midleRoot = {}
list = []

# 대분류 sbs_news
for item in data1:
    patientInfo_dic = {}

#    print(title)
    # totNum = item.find('span', 'num').get_text()
    articleUrl = item.get("href")
    articleUrl = base_url+articleUrl

    title = item.get("title")
    img = item.find("img")  # 이미지 태그
    img_src = img.get("data-src")  # 상대 이미지 경로
    content = item.find("span", {"class": "read"}).get_text()
    date = item.find("span", {"class": "date"}).get_text()
    # print("\n")
    # print(img_src)
    patientInfo_dic["article_title"] = title
    patientInfo_dic["article_url"] = articleUrl
    patientInfo_dic["article_img_src"] = img_src
    patientInfo_dic["article_content"] = content
    patientInfo_dic["write_date"] = date
    list.append(patientInfo_dic)

midleRoot["sbs_news"] = list

print(json.dumps(midleRoot))
# print(json.dumps(midleRoot, ensure_ascii=False, indent="\t"))