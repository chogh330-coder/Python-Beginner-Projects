import random
import time

game_start = True

player_score = 0
computer_score = 0

print("<<컴퓨터와 3판2선 가위 바위 보!>>")
print("<<1번은 가위 2번은 바위 3번은 보>>")
print("<<종료하려면 0번을 스코어를 확인하려면 9번을 눌러주세요!>>")

while game_start:

    print("1 = 가위, 2 = 바위, 3 = 보")
    a = int(input("가위 바위 보 중 하나를 골라주세요! : "))

    if a == 0:
        print("<<가위 바위 보 종료!>>")
        break

    elif a == 9:
        print(f"<<현재 스코어는 {player_score}대{computer_score} 입니다!>>")

    elif a > 3 or a < 1:
        print("<<잘못된 입력입니다!>>")

    else:
        x = random.randint(1,3)
        y = random.randint(2,3)
        
        print(f"{a}를 선택하셨습니다!")
        time.sleep(0.7)
        print("<<두구두구두구두구>>")
        time.sleep(y)
        print(f"<<플레이어는 {a}>>")
        time.sleep(0.7)
        print(f"<<컴퓨터는 {x}>>")

        if (a == 1 and x == 3) or (a == 2 and x == 1) or (a == 3 and x == 2):
            print("<<승리하셨습니다!>>")
            print("<<플레이어에게 1점!>>")
            player_score += 1
            
            if player_score >= 2:
                print("<<축하합니다! 플레이어의 승리입니다!!!>>")
               
                while True:
                    c = int(input("게임을 다시 시작하려면 1번을 종료하려면 2번을 눌러주세요! : "))
                
                    if c == 1:
                        player_score = 0
                        computer_score = 0
                        break
                    
                    elif c == 2:
                        print("<<즐거운 승부였습니다!>>")
                        game_start = False
                        break
                    
                    else:
                        print("<<잘못된 입력입니다!>>")

                if game_start == False:
                    break
                
                continue

        elif (x == 1 and a == 3) or (x == 2 and a == 1) or (x == 3 and a == 2):
            print("<<패배하셨습니다!>>")
            print("<<컴퓨터에게 1점!>>")
            computer_score += 1
            
            if computer_score >= 2:
                print("<<아쉽습니다... 컴퓨터의 승리입니다...>>")

                while True:
                    c = int(input("게임을 다시 시작하려면 1번을 종료하려면 2번을 눌러주세요! : "))
                    
                    if c == 1:
                        player_score = 0
                        computer_score = 0
                        break
                    
                    elif c == 2:
                        print("<<즐거운 승부였습니다!>>")
                        game_start = False
                        break
                    
                    else:
                        print("<<잘못된 입력입니다!>>")

                if game_start == False:
                    break
                
                continue
            
        else:
            print("<<비겼습니다!>>")

        while True:
                b = int(input("게임을 종료하려면 0번을 그대로 진행하려면 1번을 스코어를 확인하려면 9번을 눌러주세요! : "))

                if b == 0:
                    print("<<게임을 종료합니다!>>")
                    game_start = False
                    break

                if b == 1:
                    break
                
                elif b == 9:
                    print(f"<<현재 스코어는 {player_score}대{computer_score} 입니다!>>")
                    break

                else:
                    print("<<잘못된 입력입니다!>>")