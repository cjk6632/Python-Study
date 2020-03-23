# 딕셔너리 a에서 'B'에 해당되는 값을 pop함수 사용해서 추출하기

a = {'A':90, 'B':80, 'C':70}

b = a.pop('B') # print(a.pop('B')) 와 같음
print(a) # pop으로 값이 뽑히면 기존 위치에서 제거됨
print(b)