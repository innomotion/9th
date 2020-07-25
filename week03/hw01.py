import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
recordlist = soup.select('#regularTeamRecordList_table > tr')
print(recordlist)




#
# # # movies (tr들) 의 반복문을 돌리기
# for list in recordlist:
#     # movie 안에 a 가 있으면,
# #     tm = list.select_one('td.tm > div > span').text
# #  print(tm)
# # #
# # #     if a_tag is not None:
# # #         # a의 text를 찍어본다.
# # #         value = img_tag ['alt'] + " " + a_tag.text + td_tag.text
# # #         print(value)
# # #         # print (a_tag.text)
# # #         # print (td_tag.text)