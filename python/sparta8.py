num = int(input('4자리 정수:'))
num1 = num//1000
num2 = (num%1000)//100
num3 = (num%100)//10
num4 = (num%10)

sum= num1+num2+num3+num4
print(sum)