sales = int(input('가격'))
if sales > 1000:
    discount = sales*0.1
    print(discount,"할인 ok!")
else:
    if sales >500 :
        discount = sales*0.05
        print(discount, "할인 ok!")
    else:
        print("할인!")