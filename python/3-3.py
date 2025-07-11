#3-2 다음리스트에 저장된 정수들의 합을 계산하는 프로그램, sum() 사용하지 말고 my list =[11,22,23,99,81,93,35]
my_list = [11,22,23,99,81,93,35]#다른방법 일일이 뽑아내기도 가능 ex int(mylist[0] + mylist[1]------) 
total = 0
for x in my_list: # for x in (순차적 데이터)
    total += x

print("리스트에 저장된 정수들의 합", total)