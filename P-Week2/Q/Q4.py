# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

# 구글링은 최대한 짧게
# 검색 방식 : 내가 사용하는 언어나 프로그램명 / 기능명 / 함수 기능


scoreList = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
size = len(scoreList)
print(size)

# result = sum(scoreList) sum은 리스트 내 모든 값을 합해줌
# print(result)
total = 0
for i in scoreList:
    total = total + i
print(total/size)

