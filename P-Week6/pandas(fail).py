# movie.py에서 selenium과 bs4로만 네이버증권의 종목코드를 추출하기에는 한계가 있어서 pandas 모듈을 사용
# 1차적으로 pandas로 kind.krx.co.kr의 코덱스, 코스닥 시장의 종목 엑셀에 대한 접근 및 종목 코드 추출
# 이후 기존 방식들을 활용해서 종목코드를 활용해 네이버 증권에서 필요한 자료를 크롤링


import pandas as pd

#df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]

#df.head()




# 판다스는 도큐먼트 해석하다가 실패