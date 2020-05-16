import pymysql

conn = pymysql.connect(host = '54.180.120.24', user = 'root', password = 'root', db = 'study', charset = 'utf8')

curs = conn.cursor()




for i in range(1,10): # 해당 반복문을 통해서 DB의 Table내에 정햇던 칼럼들에 정보들을 연속적으로 넣어줌
    sql = "insert into member(id, passwd, name) values (%s, %s, %s)" # sql문을 바로 나열하지 않고, string 등의 값들을 받는 PDO 방식을 사용
    curs.execute(sql, ('abcd'+str(i), '123', 'qqq'+str(i))) # PDO 방식이 보안성이 조금 더 좋은편
    # 구문 삽입 PDO 방식 사용

conn.commit()
conn.close()