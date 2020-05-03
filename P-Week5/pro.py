# 사용자가 검색 내용 입력
# 당일에 한정해서 네이버 뉴스 내에서 입력문이 뉴스기사 제목에 있으면 가져오기
# 가져와서 엑셀에 정리 (링크 및 헤드라인 제목 기준으로 정리)



# 1. 사용자 입력값을 받아서 네이버 '뉴스' 검색폼에 입력
# 2. 해당 화면의 검색어에 따른 기사들에서 제목과 링크 저장
# 3. 엑셀에 제목과 링크 정리



# https://search.naver.com/search.naver?where=news&query=임의값&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0
# - 네이버 뉴스 탭의 링크 ('임의값'에 사용자 입력값에 따라 기사들 변경)
# 1. 사용자 입력값에 따라 검색한 페이지 전체의 Source 먼저 가져오기
#
# <ul class="type01">
# - 해당 페이지의 전체 뉴스들

# 2. 아래부터는 반복문 사용 (숫자 1~10까지 늘려가면서 뉴스기사에 접근) -> li 갯수만큼 반복문 돌리기 bs4 기능중 findAll)
#   <li id="sp_nws숫자>...</li>
#   - 각 기사 분류
#
#       <dl>
#           <dt>
#               <a href="기사URL" 및 title="기사 제목"
#               - 각 sp_nws숫자 별 가져와야할 URL과 기사 제목 (href와 title)
# 3. 접근한 기사의 <dt>내의 href와 title 가져오기


import requests
import os
from bs4 import BeautifulSoup


print('검색할 기사를 입력 : ')

search = str(input()) # 사용자 입력 구문에 들어갈 search 변수
result = requests.get('https://search.naver.com/search.naver?where=news&query='+search+'&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0')
# 사용자 입력값이 들어간 네이버 뉴스 Source를 최초로 받는 변수 result

soup = BeautifulSoup(result.text, 'html.parser')
# DOM 형태로 해당 페이지 파싱

soup2 = soup.find('ul', class_='type01')
# 해당 페이지 전체 뉴스들 기준점

soup3 = soup2.findAll('li')
# soup2 범위 중 li태그(개별 기사)를 가진 부분을 저장(반복 목적으로 사용 예정)

for i in soup3:
    Title = i.dl.dt.a.attrs['title']
    Url = i.dl.dt.a.attrs['href']
    print(Title,Url)
        #soup3 즉, li 태그 수 만큼 반복을 하게하며, 그 안에 필요한것이 기사의 제목과 URL
        # .attrs는 해당 태그의 특정 속성값을 추출해 주는 기능

os.system("pause")






