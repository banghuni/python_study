#3-11 두개정수 2type
a = int(input("첫 번쨰 정수:"))
b = int(input("두 번째 정수:"))
common=0
max=a # 최대 공약수 구하기 
if a<b:
    max=b # 두 수중 큰 수를 max값에 넣는다

for i in range(1,max):
    if a%i==0 and b%i==0: # and 논리 연산자 (두개다 만족) or = 둘중에 하나 만족
        common=i
print(a,"와",b,"의 최대 공약수는",common,"입니다")