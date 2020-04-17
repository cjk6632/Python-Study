# selenium 모듈
# 브라우저 제어 (chrome 버전 확인 후 해당 버전과 본인의 OS에 맞는 chromedriver.exe 다운로드 받아서 폴더에 추가
# 장점 : 셀레니움이 requests 모듈로 개발하기 힘든것을 짧은 시간에 개발이 가능하게 도와줌
# 단점 : requests 모듈 보다는 느리다

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('http://naver.com') #get으로 브라우저 자동 열기
print(driver.page_source) # 페이지 Source 가져오기

