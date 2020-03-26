# while로 1부터 1000까지 자연 수 중 3의 배수 합을 구해보기

number = 0
three = 0
while True:
    number = number + 1

    if number % 3 == 0:
        three = number + three
        continue

    if number == 1000:
        break

print(three)