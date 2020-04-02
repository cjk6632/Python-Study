# 함수명 : average
# 점수 리스트 [30,40,50,10]
# 점수 리스트를 함수명에 매개변수로 주면 평균 값이 return 되는 기능


def average(x):
    a = sum(x)
    b = len(x)
    return a/b

number = [30,40,50,10]
print(average(number))