# MYSQL 연동
'''
- AWS페이지 가입 및 EC2 무료 사용 설정
- 보안요건으로 pem 확장자의 private key를 다운로드 받은 후, putty로 접속 시, pem 키 인식을 위해 ppk 키로 확장자 변경(puttygen 다운로드해서 확장자 변경)
- 이후 putty 옵션 ssh -> auth에서 Pirvate key file for authentication에서 ppk 확장자인 키를 넣어주고 해당 세션정보 저장하여 지속 사용
- AWS 기본 로그인 계정은 ubuntu며, 접속 후 root로 변경해서 사용
- Putty 접속 후, APM 설치는 문서 참조 / SQL 실습 툴은 HeidiSQL 툴 기준으로 사용
'''




# member 테이블 모든 필드를 select해서 출력
# pip 모듈 설치 pymysql 사용



import pymysql # 사용할 pymysql import해줌


conn = pymysql.connect(host = '54.180.120.24', user = 'root', password = 'root', db = 'study', charset = 'utf8')
# AWS 호스트 정보 / mysql 로그인 명 / mysql PW / 설정한 db명 / charset 파라미터를 pymysql에서 커넥션
# 참고로 host는 http://로 시작하지 않는 이유가 3306 포트 연결을 위함


curs = conn.cursor()
# DB 파라미터 정보가 담긴 conn의 커서를 사용


sql = "select * from member" # 사용할 구문 명시 후 변수에 담아줌
curs.execute(sql) # 타 언어에서 SQL 실행 시, 커서의 execute로 실행



rows = curs.fetchall() # fetchall로 전체 출력에 사용 / fetchone, fetchmore 등 다양하게 있음
print(rows)

conn.close()