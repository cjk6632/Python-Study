import requests
# import의 경우 해당 모듈 전체를 가져옴
# 사용 시, 항상 '모듈명.메소드' 명시

from bs4 import BeautifulSoup
# from '모듈명' import '메소드or변수'
# 해당 모듈 내 메소드나 변수를 가져오는 방식
# 모듈명을 붙이지 않고 그대로 사용할 수 있다


#https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=905
result1 = 0
list1 = [] # 아래의 로또 번호를 받을 리스트
for a in range(900,906): # 로또 900 회차 ~ 905 회차 까지
    result1 = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='+str(a)) # 회차 파라미터 숫자(a)를 기본 int형에서 str(문자형)으로 치환해서 순차적 출력
    soup = BeautifulSoup(result1.text, 'html.parser') # 회차별 페이지 코드 중 text 내용을 parsing 후 DOM 형태로 만들기 위해 BeautifulSoup을 사용 후, Soup 변수에 넣어줌
    soup2 = soup.find('div', class_='num win') # 위 내용이 든 Soup 변수에서 .find로 'div' 태그의 'class'요소가 'num win'인 경우만 찾아서 Soup2에 넣음
    soup3 = soup2.findAll('span') # Soup2 에서 'span' 태그가 포함된 내용들을 모두 Soup3에 떄려박음

    bonus1 = soup.find('div', class_='num bonus') # 보너스 번호 위치 대략 지정
    bonus2 = bonus1.find('span') # 보너스 번호가 담긴 span 태그 찾아 넣음
    c = bonus2.text


    # for가 여러개 사용될 때 for 변수는  반복 변수 똑같지 않게 하기
    for b in soup3:
        list1.append(b.text) #Soup3의 내용들을 순차적으로 출력해줌
    print(str(a)+'회 : ',list1, '+ 보너스 번호 : ',str(c))
    list1 = []
    c = 0



# 값들 리스트 별로 분할 저장
# 보너스 번호도 가지고 오게 만들기

