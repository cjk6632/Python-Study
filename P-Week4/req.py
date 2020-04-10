# requests 모듈 사용 : 단순 가져오기 목적

# 모듈 설치 후 사용 방법
# import 모듈명

import requests

params = {

}
r = requests.get('http://naver.com')

# 변수명.text : HTML 내용이 저장됨
print(r.text)