# 길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성
# 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴

# n은 길이 10,000이하인 자연수입니다.


def WaterMellon(n):
    a = '수박' * n
    print(a[:n])

n = int(input('숫자를 입력해 주세요 : '))
WaterMellon(n)