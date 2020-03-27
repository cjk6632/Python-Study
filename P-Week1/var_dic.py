# 딕셔너리 -> Key와 Value가 쌍으로 이루어져 있는 형태
# 딕셔너리는 중괄호 {} 로 정의
# 딕셔너리 값 접근 떄도 대괄호 [] 로 접근 -> 대괄호 안 값은 인덱스 값이 아닌, Key값 입력

fruitList = {
    'orange' : 1500,
    'apple' : 3000,
    'banana' : 2000
}

print(fruitList)
# print(fruitList[0]) 인덱스로 지정 시 에러 발생
print(fruitList['apple'])