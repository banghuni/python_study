#예제 2-6 컴퓨터 가위 바위 보 게임을 하는 프로그램 컴퓨터는 사용자에게 알리지 않고 가위,바위,보 중에서 임의로 하나를 선택. 사용자는 입력 메시지에 따라서 3개중 하나를 선택. "이겻음","비겼음","졌음" 을 축력(if-else와 random.randiant를 사용)
import random

computer=random.randint(1,3)
choice=int(input("선택하시오(1:가위 2:바위 3:보)"))
print('컴퓨터의 선택(1:가위 2:바위 3:보)'),computer

if choice == 1:
    if computer == 1:
        print("비김")
    elif computer == 2:
        print("짐")
    elif computer == 3:
        print("이김")
elif choice == 2:
    if computer == 1:
        print("이김")
    elif computer == 2:
        print("비김")
    elif computer == 3:
        print("짐")
elif choice == 3:
    if computer == 1:
        print("짐")
    elif computer == 2:
        print("이김")
    elif computer == 3:
        print("비김")