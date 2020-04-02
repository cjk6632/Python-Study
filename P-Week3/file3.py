# 파일 읽기
# readline : 한줄 씩 읽기 ( 거의 사용 x )
# readlines : 리스트 형태로 변환
# read : 전체 내용

f = open('newfile.txt','r',encoding='utf8')

line = f.read()
print(line)