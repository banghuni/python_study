#4 성적이 90점이상이면 A,80점이상이면 b,70점이상이면 c,60점 이상이면d 그오ㅔ에는 f를 반환하는 함수 getgrade(scroe)를 정의하고 입력을 받아 출력
def getGrade(score):
    if score >= 90:
        print("A")
    elif score >= 80 and score <90:
        print("B")
    elif score >= 70 and score <80:
        print("C")
    elif score >= 60 and score <70:
        print("D")
    else:
        print("F")
score =int(input("점수 입력"))
getGrade(score)