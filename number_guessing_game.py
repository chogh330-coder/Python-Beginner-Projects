import random

game_start = True
choice_num = True

while choice_num:
    y = random.sample(range(0, 10), 3)
    
    while y[0] == 0:
        y = random.sample(range(0, 10), 3)
   
    game_start = True
    
    while game_start:
        print("<<숫자 추리 게임!>>")
        print("<<숫자 추리의 룰을 자세히 알고 싶다면 0번을 눌러주세요!>>")
        print("<<숫자 추리를 끝내시려면 1번을 눌러주세요!>>")
        a = input("세 자리 숫자를 입력하세요 : ")

        correct = 0
        misplace = 0
        wrong = 0
        
        if int(a) == 0:
            print("""
    1. 컴퓨터가 0~9 사이의 숫자 중 서로 다른 숫자 3개를 선택합니다.
    2. 숫자의 순서까지 정해서 정답을 만듭니다.
    3. 첫 번째 숫자는 0이 될 수 없습니다.
    4. 플레이어는 세 자리 숫자를 입력합니다.
    5. 입력한 숫자와 정답을 비교해서 결과를 알려줍니다.
    6. 숫자를 맞추게 되면 승리합니다.

    정위치: 숫자와 위치가 모두 일치
    위치 오류: 숫자는 일치하지만 위치가 다름
    불일치: 정답에 포함되지 않는 숫자
    """)

        elif int(a) == 1:
            print("<<숫자 추리 종료!>>")
            choice_num = False
            break

        elif int(a) < 100 or int(a) > 999:
            print("<<잘못된 입력입니다!>>")

        else:
            z = list(map(int, a))

            if z[0] == y[0]: 
                correct += 1 
            
            if z[1] == y[1]:
                correct += 1  
            
            if z[2] == y[2]:
                correct += 1

            if z[0] in y and z[0] != y[0]:
                misplace += 1

            if z[1] in y and z[1] != y[1]:
                misplace += 1

            if z[2] in y and z[2] != y[2]:
                misplace += 1

            if z[0] not in y:
                wrong += 1

            if z[1] not in y:
                wrong += 1

            if z[2] not in y:
                wrong += 1

            print(f"<<정위치 {correct}개!, 위치 오류 {misplace}개!, 불일치 {wrong}개!>>")
            
            if correct == 3: 
                print("<<축하합니다! 승리하셨습니다!>>")
                print(f"<<플레이어의 숫자는 {''.join(map(str, z))}, 컴퓨터의 숫자도 {''.join(map(str, y))}이었습니다!>>")

                while True:
                    b = int(input("게임을 종료하려면 1번을 다시 시작하시려면 0번을 눌러주세요! : "))

                    if b == 1:
                        print("<<즐거운 게임이었습니다!>>")
                        choice_num = False
                        game_start = False
                        break

                    elif b == 0:
                        game_start = False
                        break

                    else:
                        print("<<잘못된 입력입니다!>>")