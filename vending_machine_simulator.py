vending = True
product = {1 : ('콜라', 1500), 2 : ('사이다', 1500), 3 : ('생수', 1000), 4 : ('커피', 2000), 5 : ('이온음료', 1800)}

while vending:
   
    print("""
    ==========음료 자판기==========
    1. 콜라              - 1,500원
    2. 사이다            - 1,500원
    3. 생수              - 1,000원
    4. 커피              - 2,000원
    5. 이온음료          - 1,800원
    ==============================
    """)

    a = int(input("투입하실 금액을 입력하세요. : "))

    print(f"{a}원이 투입되었습니다.")

    b = int(input("구매하실 음료의 번호를 입력하세요. : "))

    if b < 1 or b > 5:
        print("잘못 입력하셨습니다")
        print(f"{a}원이 반환됩니다.")
        continue

    print(f"{product[b][0]}를 선택하셨습니다")
    print(f"투입하신 {a}원에서 {product[b][1]}원이 차감됩니다.")

    if a < product[b][1]:
        print("금액이 부족합니다.")
        d = int(input("금액 추가 : 1, 구매 취소 : 2"))
        if d == 1:
            while a < product[b][1]:
                f = int(input("추가하실 금액을 입력하세요. : "))
                if f > 0:
                    print(f"{f}원이 투입되었습니다.")
                    a = a + f
                else:
                    print("잘못된 입력입니다.")

        elif d == 2:
            print("구매를 취소합니다.")
            print(f"{a}원이 반환됩니다.")
            continue

        else:
            print("잘못된 입력입니다.")
            print(f"{a}원이 반환됩니다.")
            continue

    x = a - product[b][1]
    print(f"거스름돈은 {x}원 입니다.")

    while True:
        c = int(input("처음으로 돌아가기 : 1, 음료 구매 종료 : 2"))

        if c == 1:
            break

        elif c == 2:
            print("이용해 주셔서 감사합니다.")
            vending = False
            break

        else:
            print("잘못된 입력입니다.")