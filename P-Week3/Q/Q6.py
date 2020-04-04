# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가. = 'a' 모드 사용 (append))


user_input = input("저장할 내용을 입력 : ")
f = open('test.txt', 'a', encoding='utf8') # with open('test.txt', 'a', encoding='utf8') as f: 와 같음
f.write(user_input)
f.write("\n")
f.close()


