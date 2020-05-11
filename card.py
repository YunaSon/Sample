### 한도가 50000인 카드를 금액을 초과할때 까지 사용할 수 있는 코드를 작성하세요 만약 금액을 초과하면 사용이 불가해야 합니다.

card = 50000
expend_total = 0
r = card - expend_total

while expend_total < 50000:
    expend = int(input("사용금액: "))
    
    if expend > r:
        print("한도를 초과하였습니다.")
        break

    expend_total += expend
    r = card - expend_total
    print("현재 잔액은",r,"원 입니다.")
#print("현재 잔액은 {}입니다".format(r)) 