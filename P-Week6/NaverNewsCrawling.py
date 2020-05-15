# 네이버증권 - 종목명에 따른 종목 코드 추출
# 참조 코드 : https://jeongwookie.github.io/2019/03/18/190318-naver-finance-data-crawling-using-python/



#import requests
#from bs4 import BeautifulSoup
# 네이버 증권 입력값에따라 코드 동적으로 변환되어 시작부터 requests를 사용하는 것은 불가




# from 으로 사용할 시, CMD로 즉각 변환하여 사용할 수 없음(오류 발생하여 CMD 창 Down)
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests




Search = str(input()) # 검색할 대상
driver = webdriver.Chrome('./chromedriver') # 브라우저 열림(exe 붙이면 실행안됨)
driver.get('https://finance.naver.com/')




driver.find_element_by_xpath('//*[@id="stock_items"]').send_keys(Search) # 개발자도구 해당 폼 copy -> xpath
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/form/fieldset/div/button').click()
sleep(5)
Source = driver.page_source
# 입력값이 올라가고 클릭으로 넘어간 상태(동적으로 다 반영된 상태)에서 Source 가져오기




soup = BeautifulSoup(Source, 'html.parser')
# DOM 형태로




soup2 = soup.find_all('td', class_='tit')
# 종목명과 종목 코드를 담고 있는 기준점 잡기 (종목명 중복으로 여러개 뜰 수 있음)






# 아래부터는 종목명이 중복되는것이 없어서 바로 메인 페이지하거나(if), 종목명이 중복되는 문자열이 있어서 거치는 페이지가 있거나(else) -> 구분
if len(soup2) == 0: # soup2를 출력했을 때, 비어있는 Dictionary([])가 확인되기 때문에 해당 len 값이 0 즉, else처럼 중복 페이지들때문에 어떤 코드가 잡히는게 아님을 확인
    Url = driver.current_url # 크롬드라이버를 담은 변수.current_url로 해당 페이지 URL을 바로 가져옴
    Code = str(Url[-6:]) # URL 내에서 필요한 종목 코드들만 추출함
    NewsPage = requests.get('https://finance.naver.com/item/news_news.nhn?code='+Code+'&page=&sm=title_entity_id.basic&clusterId=')
    # 종목 코드를 넣어 뉴스기사가 있는 온전한 URL

    NewsTotalCode = BeautifulSoup(NewsPage.text, 'html.parser') # 뉴스기사 페이지 HTML DOM 파싱
    NewsBasePoint1 = NewsTotalCode.find('div', class_='tb_cont') # 1차 기준점
    NewsBasePoint2 = NewsBasePoint1.tbody # 2차 기준점
    eachNews = NewsBasePoint2.findAll('tr') # 2차 기준점 뉴스기사들(각각 tr로 자리잡혀있음)
    count = 0 # 딕셔너리 반복문에 쓰일 카운트
    NewsDict = {} # 빈 딕셔너리를 우선 생성
    RepeatRemoval = [] # 딕셔너리 값들을 모아둘 빈 리스트

    for i in eachNews: # 각 뉴스기사들을 추출해주기 위해 반복문 구성
        Title = i.td.a.text  # 제목
        Url = 'https://finance.naver.com' + i.td.a.attrs['href']  # URL
        Provider = i.find('td', class_='info').text  # 출처

        NewsDict[count] = { #count를 0부터 1씩 증가시켜서 딕셔너리들에 각각 담아줌
            'Title' : Title,
            'Url' : Url,
            'Provider' : Provider
        }
        RepeatRemoval.append(NewsDict[count]) # 중복 제거를 위한 빈 리스트에 값을 반복문 내에서 순차적으로 append
        count + 1 # count를 1씩 증가시키며 반복문 수행


    NewsList = ({RepeatRemoval['Title']:RepeatRemoval for RepeatRemoval in RepeatRemoval}.values())
    print(NewsList)






else: # soup2 출력 시, 종목 문자열 일치하는 부분이 있어서 한번 더 분해해줘야 하는 페이지가 발생하는 경우 (ex - 삼성전자, 삼성전자우)
    for tag in soup2: # 종목명이 중복으로 여러개 확인되어 반복문 수행
        Name = tag.a.text # tag의 내용(종목명)


        if Name == Search: # 검색 종목명과 tag 내용 일치하는 부분만 활용
            Code = str(tag.a.attrs['href'][-6:]) # attrs로 종목 코드(href) 추출 후 Code 변수에 넣음
            NewsPage = requests.get('https://finance.naver.com/item/news_news.nhn?code='+Code+'&page=&sm=title_entity_id.basic&clusterId=')
            # https://finance.naver.com/item/news.nhn?code=005930&sm=title_entity_id.basic 방식으로 Source를 그대로 끌고 오면 크롤링 불가능
            # 불가능한 이유는 iframe으로 외부 Source를 끌고오는 형태로 사용하고 있는 것을 확인하여 해당 iframe Url까지 포함시켜줌
            # &page= 뒷 부분을 &sm=entity_id.basic 로 바꿔주면 내용 기준 뉴스 크롤링 해오는 파라미터


            NewsTotalCode = BeautifulSoup(NewsPage.text, 'html.parser') # 종목코드를 삽입한 뉴스,공시 페이지 전체 DOM 파싱


            NewsBasePoint1 = NewsTotalCode.find('div', class_='tb_cont') # 추출할 뉴스부분들만 기준점으로 잡기
            NewsBasePoint2 = NewsBasePoint1.tbody # 바로 tr로만 잡으면 범위가 너무 커서 바로 상위 태그인 tbody로 한번 더 좁혀줌

            eachNews = NewsBasePoint2.findAll('tr') # 기준점 내에서 각 기사들의 시작점을 나타내는 tr들을 모두 수집
            count = 0  # 딕셔너리 반복문에 쓰일 카운트
            NewsDict = {} # 빈 딕셔너리를 우선 생성
            RepeatRemoval = []  # 딕셔너리 값들을 모아둘 빈 리스트

            for i in eachNews:
                Title = i.td.a.text  # 제목
                Url = 'https://finance.naver.com' + i.td.a.attrs['href']  # URL
                Provider = i.find('td', class_='info').text  # 출처

                NewsDict[count] = { #count를 0부터 1씩 증가시켜서 딕셔너리들에 각각 담아줌
                    'Title': Title,
                    'Url': Url,
                    'Provider': Provider
                }
                RepeatRemoval.append(NewsDict[count]) # 중복 제거를 위한 빈 리스트에 값을 반복문 내에서 순차적으로 append
                count + 1
            NewsList = ({RepeatRemoval['Title']: RepeatRemoval for RepeatRemoval in RepeatRemoval}.values())
            print(NewsList)



driver.close()
