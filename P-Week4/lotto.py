import requests

from bs4 import BeautifulSoup


#https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=905
a = 900
result = 0 # for끼리 반복 변수 똑같지 않게 하기
for a in range(900,906):
    result = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='+str(a))
    soup = BeautifulSoup(result.text, 'html.parser')
    soup2 = soup.find('div', class_='num win')
    soup3 = soup2.findAll('span')
    for b in soup3:
        print(b.text)

# 값들 리스트 별로 분할 저장
# 보너스 번호도 가지고 오게 만들기

