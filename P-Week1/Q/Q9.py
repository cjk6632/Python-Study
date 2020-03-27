# 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우는 어떤 경우인지?

a = dict()
print(a) #결과 값 {}

# 아래 중 오류가 발생하는 경우와 그 이유는
# a['name'] = 'python'
# a[('a',)] = 'python'
# a[[1]] = 'python'
# a[250] = 'python'

print(a)
# 3번 예시에서 에러 발생 : dict의 Key에는 변할 수 있는(Mutable0 값을 사용할 수 없음(3번의 [1]은 리스트로 변하는 값