#2-8 사용자로부터 키를 입력받고 표준 체중을 계산 if else 를 사용하여 저체중,표준,과체중을 출력, 표준체중 =(키 -100) * 0.9
h = int(input("키:"))
aw = (h - 100) * 0.9
if aw < 18.5:
    print("메르치")
elif aw < 23:
    print("고등어")
elif aw < 25:
    print("참치")