# a 리스트에서 중복 숫자를 제거해보기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a) # set은 중복 허용 X, dict와 함께 순서가 없는 Unorderd 특성
print(b) # set상태로만 놓으면 인덱스 사용 불가
print(list(b)) #list나 tuple로 변환 해 주면 인덱싱 가능
