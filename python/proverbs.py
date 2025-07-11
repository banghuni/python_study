import random
proverbs = [
         ("호랑이 굴에","들어가야 산다"),("등잔 밑이","어둡다"),("가는 말이","고와야 오는 말이 곱다"),
        ("고생 끝에","낙이 온다"),("원숭이도","나무에서 떨어진다"),("티끌 모아","태산"),
        ("백문이","불여일견"),("똥 묻은 개가","겨 묻은 개 나무란다"),("바늘 도둑이","소 도둑 된다")
]
print("속담 맞추기 게임입니다")
input("ENTER를 누르면 시작합니다")
score = 0
trial = 0
for total in range(5):
    front,back = random.choice(proverbs)#랜덤함수 출력 random.
    print(f"속담:\"{front}?\"")

    answer = input("뒷부분을 입력하세요:").strip()
    correct1 = 0
    if answer == back:
        print("정답\n")
        score += 1      
    else:#힌트제공
        hint = back[0] #첫 글자
        length = len(back)
        print(f"오답입니다. 힌트: '{hint}'로 시작하시오")
        answer = input("힌트를 보고 다시 입력하세요:").strip()
        if answer == back:
            print('정답\n')
            score += 1
        else:
            print(f"오답 정답은:\"{back}\"입니다\n")
total += 1
print(f"\n게임 종료! 당신의 총 {total}중 {score}문제 정답입니다")
#오답을 입력했을떄, 정답의 일부 를 힌트로 보여주는 기능추가
#힌트를 보고 한번 더 입력하도록 기능 추가