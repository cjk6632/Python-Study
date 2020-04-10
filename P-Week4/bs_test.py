# 모듈 호출 다른 방법 : from 모듈명 import 함수명

import requests # 이 방식은 모듈명.이름 으로 사용하는 형태
from bs4 import BeautifulSoup # 이 방식은 모듈명 대신 함수명만 써서 사용 가능


result = requests.get('https://naver.com') # requests로 naver의 코드를 가져옴
print(result.text)  # 가져온 코드 내에서 text만 추출해서 출력


soup = BeautifulSoup(result.text, 'html.parser') # text만 추린 후, BeautifulSoup에 DOM 형태로 볼 수 있게 Parsing
# bs4 모듈에서 트리형태에 접근 시, . 으로 접근을 하면 됨 (단, . 접근은 가장 먼저 나오는 대상만 접근)
print(soup.a.text) # soup의 가장 먼저 발견되는 a태그 내에서 text를 출력

# 검색 예시
# 파이썬 href 가져오기 (x)
# bs4 href 가져오기 (o)

