# 파일 입력

f = open('newfile.txt', 'w', encoding = 'utf8')
f.write('Hello\n') # \n 은 개행 문자
f.write('Python\n')
f.write('I am\n')
f.write('Studying')

f.close()