#3-5 중첩 반복문을 이용하여 입력된 정수만큼 *을  순차적으로 출력
x = int(input("정수를 압력하시오"))
for y in range(1, x + 1):
    for z in range(1, y + 1):
        print("*", end=' ')
    print()