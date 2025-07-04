num = int(input('6자리의 정수')) # if문 사용 

if num>=100000 and num<1000000:
   moreT=num//1000
   lessT=num%1000
   print(moreT,',',lessT)
   print(moreT+lessT)
   print(str(moreT)+','+str(lessT))
   print("%d,%d"%(moreT,lessT))
   print(f"{moreT},{lessT}")
else:
   print("숫자가 범위에 없습니다.")