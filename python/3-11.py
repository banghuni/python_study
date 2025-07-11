#2와20사이에 있는 모든 소수를 찾는 프로그램
maxNum=20
number=2
count=0

while number<maxNum:
    divisor=2
    prime=True

    while divisor<number:  #while문 안에 while문 위험! 
        if number%divisor==0:
            prime=False
            break
        divisor+=1
    if prime:
        count+=1
        print(number,end=" ")
    number+=1

#while문 -> for 
