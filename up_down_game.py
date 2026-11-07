import random
import time

game_start = True
random_start = True

print("<<업 다운 게임!>>")
print("<<10번의 기회 안에 1~100 사이의 숫자를 맞춰보세요!>>")
print("<<컴퓨터가 up과 down으로 답해드립니다!>>")

while random_start:
    x = random.randint(1,100)
    count = 0
    game_start = True

    while game_start:
        print("<<게임을 종료하려면 0번을 눌러주세요>>")
        a = int(input("숫자를 입력해 주세요! : "))

        if a == 0:
            print("<<게임을 종료합니다!>>")
            random_start = False
            game_start = False
            break

        elif a < 1 or a > 100:
            print("<<잘못 입력하셨습니다!>>")

        else:
            y = random.randint(1,2)
            count += 1

            if a > x:
                time.sleep(y)
                print("<<down!>>")
                
                if count == 10:
                    print("<<10번의 기회를 전부 사용했습니다!>>")
                    print("<<으악으악! 눈 앞이 깜깜해졌다!>>")

                    while True:
                        b = int(input("게임을 다시 시작하려면 1번 종료하려면 2번을 눌러주세요 : "))

                        if b == 1:
                            print("<<게임을 재시작 합니다!>>")
                            game_start = False
                            break

                        elif b == 2:
                            print("<<게임을 종료합니다!>>")
                            random_start = False
                            game_start = False
                            break

                        else:
                            print("<<잘못된 입력입니다!>>")


            elif a < x:
                time.sleep(y)
                print("<<up!>>")

                if count == 10:
                    print("<<10번의 기회를 전부 사용했습니다!>>")
                    print("<<으악으악! 눈 앞이 깜깜해졌다!>>")
                                    
                    while True:
                        b = int(input("게임을 다시 시작하려면 1번 종료하려면 2번을 눌러주세요 : "))

                        if b == 1:
                            print("<<게임을 재시작 합니다!>>")
                            game_start = False
                            break

                        elif b == 2:
                            print("<<게임을 종료합니다!>>")
                            random_start = False
                            game_start = False
                            break

                        else:
                            print("<<잘못된 입력입니다!>>")

            else:
                time.sleep(y)
                print("<<정답입니다!>>")
                print(f"<<질문한 횟수는 {count}번 입니다!>>")

                while True:
                    b = int(input("게임을 다시 시작하려면 1번 종료하려면 2번을 눌러주세요 : "))

                    if b == 1:
                        print("<<게임을 재시작 합니다!>>")
                        game_start = False
                        break

                    elif b == 2:
                        print("<<게임을 종료합니다!>>")
                        random_start = False
                        game_start = False
                        break

                    else:
                        print("<<잘못된 입력입니다!>>")