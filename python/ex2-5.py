# 사용자로부터 3개의 정수를 입력받고 if-else문을 사용하여 가장 작은 값을 출력
a = int(input("첫 번째 정수를 입력하십시오"))
b = int(input("두 번째 정수를 입력하십시오"))
c = int(input("세 번째 정수를 입력하십시오"))
if a < b and a < c:
    print(f"가장 작은 값은 {a}입니다")
if b < a and b < c:
    print(f"가장 작은 값은 {b}입니다")
if c < a and c < b:
    print(f"가장 작은 값은 {c}입니다")