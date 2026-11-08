import random
import time
before_start = True

while before_start:
    game_start = True
    stats_reset = True
    p_hp = random.randint(100,150)
    p_atk = random.randint(15,25)
    m_name = ["슬라임", "고블린", "오크", "박쥐", "스켈레톤"]
    

    reset_count = 5

    while game_start:
        print("<< 어서오세요 용사님! >>")
        a = input("<< 용사님의 이름을 알려주세요! >> :")
        p_stats = {"name" : a, "hp" : p_hp, "attack" : p_atk} 
        time.sleep(0.3)
        print(f"<< {p_stats['name']}용사님의 스텟을 설정했어요! >>")
        print(f"<< {p_stats['name']}용사님의 현제 스텟 >>")
        time.sleep(0.3)
        print("=============================")
        print(f"용사 {p_stats['name']}")
        print(f"체력 : {p_stats['hp']}")
        print(f"공격력 : {p_stats['attack']}")
        print("=============================")
        time.sleep(0.3)
        print("<< 용사님의 특전으로 스텟을 재설정 하실 수 있어요! >>")
        
        while stats_reset:
            b = int(input("<< 재설정 하시려면 1번을 그대로 진행하시려면 2번을 눌러주세요!>> : "))
        
            if b == 1:
                while True:
                    print("<< 용사의 특전 발동! >>")
                    p_stats["hp"] = random.randint(100,150)
                    p_stats["attack"] = random.randint(15,25)
                    reset_count -= 1
                    time.sleep(0.3)
                    print(f"<< 바뀐 용사님의 스텟표 >>")
                    print(f"체력 : {p_stats['hp']}")
                    print(f"공격력 : {p_stats['attack']}")
                    print("==============================")
                
                    if reset_count == 0:
                        print("<< 리셋 카운트를 전부 사용하셨어요 용사님! >>")
                        time.sleep(0.2)
                        print("<< 아쉽지만 더 이상 리셋하실 수 없어요...>>")
                        time.sleep(0.2)
                        print("<< 하지만 용사님은 승리하실 수 있어요! 모험을 출발하겠습니다!>>")
                        stats_reset = False
                        break

                    reset_again = int(input("<< 이대로 모험을 출발하시려면 1번을 한번 더 변경하시려면 2번을 눌러주세요! >> : "))
                        
                    if reset_again == 1:
                        print("<< 좋아요 용사님! 이대로 모험을 출발하겠습니다! >>")
                        stats_reset = False
                        break
                    
                    elif reset_again == 2:
                        continue
                    
                    else:
                        print("<< 잘못 입력하셨어요 용사님! >>")
                        continue

            elif b == 2:
                print("<< 현재 스텟으로 모험을 시작합니다! >>")
                break

            else:
                print("<< 잘못된 입력이에요 용사님! >>")
                continue

            
        m_hp = random.randint(50,100)
        m_atk = random.randint(10,20)
        m_name_random = random.choice(m_name)
        m_stats = {"name" : m_name_random, "hp" : m_hp, "attack" : m_atk}
        p_max_hp = p_stats["hp"]
        m_max_hp = m_stats["hp"]

        print("========= 전투 시작 =========")
        print(f"용사 {p_stats['name']}")
        print(f"체력 : {p_stats['hp']}")
        print(f"공격력 : {p_stats['attack']}")
        print("===========================")
        time.sleep(0.7)
        print(f"몬스터 : {m_stats['name']}")
        print(f"체력 : {m_stats['hp']}")
        print(f"공격력 : {m_stats['attack']}")
        print("===========================")

        while p_stats["hp"] > 0 and m_stats["hp"] > 0:
            dmz = m_stats["attack"] 

            print("\n=========== 상태창 ===========")
            print(f"용사 {p_stats['name']} | 체력 : {p_stats['hp']} | 공격력 : {p_stats['attack']}")
            print(f"몬스터 {m_stats['name']} | 체력 : {m_stats['hp']} | 공격력 : {m_stats['attack']}")
            print("================================")

            print("===== 행동 =====")
            print("- 1. 공격")
            print("- 2. 회복")
            print("- 3. 방어")
            print("===============")
            p_active = int(input(f"<< 용사{p_stats['name']}는 무엇을 할까? >> : "))

            if p_active == 1:
                print("<< 용사의 공격! >>")
                time.sleep(0.3)
                critical = random.randint(1,100)
                
                if critical <= 40:
                    print("<< 눈부신 일격! >>")
                    print(f"<<{m_stats['name']}은 큰 피해를 입었다! >>")
                    battle_result = m_stats["hp"] - p_stats["attack"] * 2
                    m_stats["hp"] = battle_result
                    print(f"<< {m_stats['name']}의 현재 체력 : {m_stats['hp']}/{m_max_hp}>>")
                
                else:
                    print("<< 용사의 일격! >>")
                    print(f"<<{m_stats['name']}은 피해를 입었다! >>")
                    battle_result = m_stats["hp"] - p_stats["attack"]
                    m_stats["hp"] = battle_result
                    print(f"<< {m_stats['name']}의 현재 체력 : {m_stats['hp']}/{m_max_hp}>>")

                if m_stats["hp"] <= 0:
                    print(f"<< {m_stats['name']}은 쓰러졌다! >>")
                
            elif p_active == 2:
                print("<< 용사의 회복! >>")
                critical_heal = random.randint(1,100)
                heal = random.randint(20,150)

                if critical_heal <= 40:
                    print("<< 기적적인 치유! >>")
                    p_stats["hp"] = min(p_stats["hp"] + (heal * 2), p_max_hp)
                    print(f"<< 현제 체력 : {p_stats['hp']}/{p_max_hp}>>")

                else:
                    print("<< 따뜻한 치유! >>")
                    p_stats["hp"] = min(p_stats["hp"] + heal, p_max_hp)
                    print(f"<< 현제 체력 : {p_stats['hp']}/{p_max_hp}>>")
            
            elif p_active == 3:
                print("<< 용사의 방어! >>")
                block = random.randint(1,100)
                if block <= 20:
                    print("<< 완벽한 방어! >>")
                    dmz = 0

                else:
                    print("<< 평범한 방어! >>")
                    dmz = m_stats["attack"] / 2

             
            if m_stats["hp"] > 0 and (p_active == 1 or p_active == 2 or p_active == 3):
                print(f"{m_stats['name']}의 반격!")
                m_critical = random.randint(1,100)
                
                if m_critical <= 20:
                    print("<< 치명적 일격! >>")
                    print(f"<< 용사 {a}는 큰 피해를 입었다! >>")
                    m_result = p_stats["hp"] - dmz * 2
                    p_stats["hp"] = m_result
                    print(f"<< 용사{p_stats['name']}의 현재 체력 : {p_stats['hp']}/{p_max_hp}>>")
                            
                else:
                    print("<< 몬스터의 일격! >>")
                    print(f"<< 용사 {a}는 피해를 입었다! >>")
                    m_result = p_stats["hp"] - dmz
                    p_stats["hp"] = m_result
                    print(f"<< 용사{p_stats['name']}의 현재 체력 : {p_stats['hp']}/{p_max_hp}>>")

        if p_stats["hp"] <= 0:
            print(f"<< {a}용사님! 패배하시다니 한심하네요! >>")

        elif m_stats["hp"] <= 0:
            print(f"<< {m_stats['name']}를 물리쳤어요 대단해요 용사님! >>")