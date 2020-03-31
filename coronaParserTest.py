import json
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://ncov.mohw.go.kr/'
soup = BeautifulSoup(urllib.request.urlopen(url).read().decode('utf-8'), "html.parser")
data1 = soup.find('ul', {'class': 'liveNum'})
data1 = data1.find_all('li')
list = []

# def addCoronaList(item) :
midleRoot = {}


# 대분류 환자현황
for item in data1:
    # 중분류 [0]확진환자, [1]완치, [2]치료중, [3]사망
    patientInfo_dic = {}
    title = item.find('strong', 'tit').get_text()
    totNum = item.find('span', 'num').get_text()
    beforeNum = item.find('span', 'before').get_text()
    patientInfo_dic["title"] = title
    patientInfo_dic["tot_num"] = totNum
    patientInfo_dic["before_num"] = beforeNum
    list.append(patientInfo_dic)

midleRoot["patient_status"] = list

# Print JSON
#print(json.dumps(midleRoot, ensure_ascii=False, indent="\t"))
print(json.dumps(midleRoot))
