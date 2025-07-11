# 3-4 정수의 약수를 구하고 출력
x = int(input("정수를 입력하시오:"))
for y in range(1, x + 1):
    if x % y == 0:
        print(y, end=' ')