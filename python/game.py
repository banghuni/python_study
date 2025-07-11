#게임만들기
import random
str = ["스타크래프트","워크래프트","헬다이버즈","배틀그라운드","마인크래프트"]
a = random.choice(str)
#print(a)
#abc=['a','b','c','d','e']
#abc = ['a', 'b', 'c', 'd', 'e']
#random.shuffle(abc) abc=['a','b','c','d','e'] 랜덤하게 섞여서 나옴
#random.choice(abc)
#import time
import time

time.time()
time.localtime(time.time())

lt = time.localtime(time.time())
time.asctime(lt)


start_time = time.time()

type = (input("\n입력:"))
end_time = time.time()
elapsed = end_time - start_time
#print(elapsed)

#correct = 0
#for i in 범주(질문 문장의 길이,입력한 문장의 길이)):
#if 질문문장 단어 == 입력문장 단어:
#correct += 1
correct = 0

for i in range(min(len(a),len(type))):
    if a[i] == type[i]:
         correct += 1

accuracy = correct / len(a) * 100
speed = len(type) / elapsed * 60

#결과 출력
print("\n결과:")
print(f"걸린 시간:{elapsed:.2f}초")
print(f"정확도: {accuracy:.2f}%")
print(f"타자 속도: {speed:.2f} 차/분")
    
#추가요구사항 오타가 없을떄까지 입력을 받도록 수정
#정확도 대신 오타 횟수 출력