#1~100사이 3의 배수의합을 더함
total = 0
for x in range(1,101):
    if x % 3 == 0:
       total += x 

print("1부터 100까지 3의 배수의 합", total)