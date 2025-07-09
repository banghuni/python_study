#오판 프로그램
import random
num1 = random.randint(0,10)
num2= random.randint(0,10)

cal=random.randint(1,4)

if cal==1:
    answer=num1+num2
    reply=int(input('{0}+{1}의 값은?'.format(num1,num2)))
    if answer==reply:
        print("정답")
    else:
        print("오답")
elif cal==2:
    answer=num1-num2
    reply=int(input('{0}-{1}의 값은?'.format(num1,num2)))
    if answer==reply:
        print("정답")
    else:
        print("오답")
elif cal==3:
    answer=num1*num2
    reply=int(input('{0}*{1}의 값은?'.format(num1,num2)))
    if answer==reply:
        print("정답")
    else:
        print("오답")
elif cal == 4:
    while num2 == 0:
        num2 = random.randint(1, 10)
    answer = round(num1 / num2, 2)
    reply = float(input(f'{num1} / {num2}의 값은? (소수 둘째자리까지) '))
    if abs(answer - reply) < 0.01:
        print("정답")
    else:
        print("오답")