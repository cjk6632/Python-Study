# 만약에 ? (if)
# 만약에 그게 아니라면 ? (elif)
# 그것도 아니라면 ? else

# 사용법
# if 조건:
# elif 다른조건:
# elif 다른조건:
# else (위 조건이 한가지도 부합하지 않는 경우 실행)

# elif와 else는 필수가 아님
# 조건문이 부합하는 순간 if문은 끝남

money = 25000
if money > 50000:
    print('하고싶은거 다 해')
elif money > 20000:
    print("짐질방")
elif money > 10000:
    print("피시방을 가")
else:
    print('편의점')