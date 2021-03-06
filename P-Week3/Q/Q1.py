# 주어진 자연수가 홀수인지, 짝수인지 판별
# 함수명 : is_odd
# 사용자에게 입력값을 받을때는 input() 함수를 이용
# input() 함수에 입력된 입력값은 무조건 string 형태로, 정수로 사용이 필요하면 형 변환이 필요
# int(input()) 형태로 사용

# 함수를 정의 할 시, 함수 기능이 명확하면 좋다 (아래 함수에서 input까지 넣으면 짝, 홀을 구분하는것 외에 입력값 받는것도 추가됨)
# 함수를 만드는 가장 큰 이유는 재사용
def is_odd(x):
    # x = int(input())
    if x % 2 == 0:
        return '짝수'
    else:
        return '홀수'
x = int(input())
print(is_odd(x))

# 개발을 하면서 어떤 문자를 그냥 입력했다 -> 변수
# 어떤 문자를 입력하고 ()를 열고 닫았다 -> 함수