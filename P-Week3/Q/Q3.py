# 함수명 : three_time(x)
# 첫번째 매개변수 : 몇까지 실행할지 입력
    # 1 ~ 첫번째 매개변수의 값까지 반복하며, 3의 배수의 합을 구해서 리턴


# 함수 안과 함수 밖의 변수는 이름이 같더라도 다른 변수
# total = 0
def three_time(x):
    total = 0
    for i in range(1,x):
        if x % 3 == 0:
            total = total + i
    return total

x = int(input())
print(three_time(x))
