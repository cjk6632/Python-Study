# https://programmers.co.kr/learn/courses/30/lessons/12903

# len()에 문자열 넘길 시, 문자열의 크기를 알려줌
# 문자열 슬라이싱 기능 이용하여 풀어보기

# 입출력 예
# "abcde" -> "c"
# "qwer" -> "we"

# 단어 s의 가운데 글자를 반환하는 함수, Soulution 만들기
# 단어 길이가 짝수라면 가운데 두 글자를 반환하면 됨

def solution(string):
    if len(string) % 2 == 0:
        d = len(string) // 2
        return string[d-1:d+1]
    else:
        return string[len(string) // 2]

# def solution(string):
#     return string[(len(string) - 1) // 2:len(string) // 2 + 1]
#             #abcde      #5 - 1 (4)     //  #2: 4 // 2  + 1 (2:3)

print('단어 입력 (1 ~ 100글자 이내로 입력 : ')
string = input()
print(solution(string))

''' len()으로 문자열 크기(수) 확보 후 길이의 홀/짝 구분
홀 -> 가운데 글자 반환 / 짝 -> 가운데 두 글자 반환'''