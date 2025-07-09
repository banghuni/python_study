#예제 2-4번 원의 넓이를 구하는 프로그램을 만들고 사용자가 입력한 원의 반지름으로 계산해서 출력음수 입력의 경우 "잘못된 값입니다"
#파이썬에서 원의 넓이를 구하는 공식은 다음과 같습니다.
# 원의 넓이 = math.pi * (반지름 ** 2)
import math
radius = float(input("원의 반지름을 입력하십시오:"))
if radius < 0:
    print("잘못된 값입니다")
else:
    area = math.pi * (radius ** 2)
    print(f"원의 넓이는{area}입니다")