# "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
#
# f2 = open("test.txt", 'r')
# print(f2.read())

# 단, 이 경우 예상하는 Life is too short 문장을 출력하지 않음. 예상한 값을 출력할 수 있도록 프로그램 수정

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() # 파일을 .close() 로 닫지 않은 상태로 다시 열면 데이터를 읽을 수 없기 때문에 .close()는 습관처럼 사용 필요

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()


# 아래는 .close()가 필요없는 with 구문
# with open("test.txt", 'w') as f1:
#     f1.write("Life is too short!")
# with open("test.txt", 'r') as f2:
#     f2.read())