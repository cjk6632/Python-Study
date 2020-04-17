# 사용자가 검색 내용 입력
# 당일에 한정해서 네이버 뉴스 내에서 입력문이 뉴스기사 제목에 있으면 가져오기
# 가져와서 엑셀에 정리 (링크 및 헤드라인 제목 기준으로 정리)



# 1. 사용자 입력값을 받아서 네이버 검색폼에 넣기
# 2. 카테고리 중 '뉴스' 페이지의 기사들에서 제목과 링크 저장
# 3. 엑셀에 제목과 링크 정리



# https://search.naver.com/search.naver?where=news&query=임의값&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0
# - 네이버 뉴스 탭의 링크 ('임의값'에 사용자 입력값에 따라 기사들 변경)
# 1. 사용자 입력값에 따라 검색한 페이지 전체의 Source 먼저 가져오기
#
# <ul class="type01">
# - 해당 페이지의 전체 뉴스들

# 2. 아래부터는 반복문 사용 (숫자 1~10까지 늘려가면서 뉴스기사에 접근) -> li 갯수만큼 반복문 돌리기 bs4 기능 findAll)
#   <li id="sp_nws숫자>...</li>
#   - 각 기사 분류
#
#       <dl>
#           <dt>
#               <a href="기사URL" 및 title="기사 제목"
#               - 각 sp_nws숫자 별 가져와야할 URL과 기사 제목 (href와 title)
# 3. 접근한 기사의 <dt>내의 href와 title 가져오기


# request
import requests
from bs4 import BeautifulSoup

search = str(input()) # 사용자 입력 구문에 들어갈 search 변수
result = requests.get('https://search.naver.com/search.naver?where=news&query='+search+'&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0')
# 사용자 입력값이 들어간 네이버 뉴스 Source를 최초로 받는 변수 result

soup = BeautifulSoup(result.text, 'html.parser')
# DOM 형태로 해당 페이지 파싱

soup2 = soup.find('ul', class_='type01')
# 해당 페이지 전체 뉴스들 기준점

soup3 = soup2.findAll('li')

for i in soup3:
    print(i.dl.dt.a.text)
    #href

# <li id="sp_nws숫자>...</li>







