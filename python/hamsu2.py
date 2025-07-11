#합,차,곱,나눗셈을 수행하는 함수를 가각 정의한다. 입력값 두개를 받아서 모든 함수를 한번씩 실행하고 출력
def add(x,y):
    return x+b
def subtract(x,y):
    return x-b
def multiply(x,y):
    return x*b
def divied(x,y):
    return x%b

a = int(input("1st 입력값"))
b = int(input("2st 입력값"))

print("합:",add(a,b))
print("차:",subtract(a,b))
print("곱:",multiply(a,b))
print("나눗셈:",divied(a,b))