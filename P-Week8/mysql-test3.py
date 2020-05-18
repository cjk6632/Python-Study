import pymysql

conn = pymysql.connect(host = '54.180.120.24', user = 'root', password = 'root', db = 'study', charset = 'utf8')

curs = conn.cursor()



sql = "update member set passwd = %s where passwd = %s" # update의 경우 기존 데이터 수정에 사용
curs.execute(sql, ('000', '123'))

sql = "delete from member where no = %s" # delete의 경우 기존 데이터 삭제에 사용
curs.execute(sql, '10')

conn.commit()
conn.close()