#게임만들기
import random
str = ["스타크래프트",
       "워크래프트",
       "헬다이버즈",
       "배틀그라운드",
       "마인크래프트"]
print('타자연습 게임입니다.')
input('엔터를 누르면 시작합니다')
target = random.choice(str)
print('\n다음 문장을 그대로 입력하세요:\n')
print(f'{target}\n')
input('준비되면 ENTER를 누르시오')
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


start_time = time.time()#시간측저이작
trial = 0
while True:
        
    typed = (input("\n입력"))# 사용자 입력 받기

    end_time = time.time()#시간 측정 종료

    elapsed = end_time - start_time
    #print(elapsed)

    #correct = 0
    #for i in 범주(질문 문장의 길이,입력한 문장의 길이)):
    #if 질문문장 단어 == 입력문장 단어:
    #correct += 1
    correct = 0#정확도 계산

    for i in range(min(len(target),len(typed))):
        if target[i] == typed[i]:
            correct += 1

    total = max(len(target), len(typed))#오류수정
    accuracy = correct / len(a) * 100
    speed = len(typed) / elapsed * 60 # 분당 타자 수(cpm)

    if accuracy == 100:
        print("완료했어요.")
        break
    else:
        print("다시 시도해보세요")
        trial += 1

#결과 출력
print("\n결과")
print(f"걸린 시간:{elapsed:.2f}초")
print(f"정확도: {accuracy:.2f}%")
print(f"시도 횟수 {trial:.2f}")
print(f"타자 속도: {speed:.2f} 차/분")
    
#추가요구사항 오타가 없을떄까지 입력을 받도록 수정
#정확도 대신 오타 횟수 출력