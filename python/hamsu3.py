#2번에서 정의한 4개의 함수를 새로운 calc()함수에서 호출하여 두개의 입력값을 받아 동시에 수행하고 출력
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

def calc():
    a = int(input("1st 입력값"))
    b = int(input("2st 입력값"))

print("합:",add(a,b))
print("차:",subtract(a,b))
print("곱",multiply(a,b))
print("나눗셈",divide(a,b))