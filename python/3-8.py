#3-10 1**+2**+3**+...+n**의 합을 구하는 프로그램
n = int(input("정수"))
total = 0
for x in range(1, n + 1):
    total += x ** 2
print("합계:",total)