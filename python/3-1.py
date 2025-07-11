#3-1 2부터 50까지의 모든 짝수를 공백으로 구분하여 한 줄에 출력
for x in range(2,51,1):
    if x % 2 == 0:
        print(end=' ')
        print(x, end=' ')