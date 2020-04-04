# 리스트 내포 방식 (아래 문제를 리스트 내포 방식으로 변경)
# 리스트 중에서 홀수에만 2를 곱하여 저장
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)