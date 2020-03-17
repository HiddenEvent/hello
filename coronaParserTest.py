import json
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://ncov.mohw.go.kr/'
soup = BeautifulSoup(urllib.request.urlopen(url).read().decode('utf-8'), "html.parser")
data1 = soup.find('ul', {'class': 'liveNum'})
data1 = data1.find_all('li')

# data1 = soup.select('ul.liveNum')
# data1[0].select('strong.tit')
# print(data1[0].select('strong.tit'))
# data2 = data1.find_all('strong', 'tit')
print(data1)

patientInfo_list = []
completeCureInfo_list = []
cureInfo_list = []
DeathInfo_list = []

#def addCoronaList(item) :



# 대분류 환자현황
for item in data1:
    # 중분류 [0]확진환자, [1]완치, [2]치료중, [3]사망
    if item == data1[0]:
        print(item.find('strong', 'tit').get_text())
        print(item.find('span', 'num').get_text())
        print(item.find('span', 'before').get_text())
        patientInfo_list.append(item.find('strong', 'tit').get_text())
        patientInfo_list.append(item.find('strong', 'tit').get_text())
        patientInfo_list.append(item.find('strong', 'tit').get_text())

print(patientInfo_list)


# for item in data1:
#     print(item.get_text().replace('\n','').replace(' ', ''))

# print(data1)

# data1_list = []
# data2_list = []
# for item in data1:
#     data1_list.append(item.get_text().replace('\n', '').replace(' ', ''))
# for item in data2:
#     data2_list.append(item.get_text().replace('\n', '').replace(' ', ''))
#
# confirmedPatient = data1_list[0]
# uspectedPatient = data1_list[1]
#
# x = data2_list[0].find('사망')
# curedPatient = data2_list[0][2:4]
# diedPatient = data2_list[0][x + 2:]
#
# print(curedPatient)
# print(diedPatient)
# *참고 <변수이름>

# 확진자 = confirmedPatient
# 의심 환자 = suspectedPatient
# 격리 해제 = curedPatient
# 사망자 =  diedPatient
