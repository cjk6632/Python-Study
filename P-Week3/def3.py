# 매개 변수에 디폴트값 설정 할 수 있음

# def add(x,y):
#     return x+y
# 
# result = add(3)
# print(result)
# 위 경우 매개 변수가 하나 없어서 에러 발생


def add(x = 0,y = 0): # 이 경우 매개변수가 할당되지 않더라도 기본값이 설정 되어 에러가 없음
    return x+y # 기본값을 0으로 설정했지만, 매개변수 값이 정상적으로 들어온 경우 값이 덮어 씌워짐

result = add(3)
print(result)