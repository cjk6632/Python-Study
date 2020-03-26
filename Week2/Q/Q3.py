# while 문으로 별(*) 표시 프로그램 작성
# 개행 print('*\n**\n***\n****\n*****') # print 시 자동 개행됨
# *
# **
# ***
# ****
# *****

i = 1
while True:
    if i != 6:
        print('*'*i)
        i = i + 1
        continue

    if i == 6:
        break
        
  # 아래는 continue 없이 결과값 동일      
# while True:
#     print('*'*i)
#     i = i + 1
# 
#     if i == 6:
#         break
# while문에 break, continue가 꼭 있어야 하는건 아님 (개발자 마음)
