# 함수(function)
# 파이썬에서는 def(definition) 으로 사용
# def 함수명(인자값1, 인자값2 ...)
# 함수는 만들기만 한다고 실행 되는게 아님
# 호출을 시켜야 실행 가능
# 실제 수학시간에 공부하는 함수와 동일한 개념

def fx(x): # 함수에 어떤 값을 넘겨주는데, 그 값을 인자값(매개 변수) 라고 부름(x는 매개 변수)
    print(x+3) # 매개변수가 무조건 존재하는 것은 아님(단순 문자열 출력 등)
                    # ㄴ 개발자가 어떤 의도로 함수를 만드냐에 따라 달라짐
fx(5)