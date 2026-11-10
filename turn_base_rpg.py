import random
import time
before_start = True

while before_start:
    game_start = True
    stats_reset = True
    adventure = True
    p_hp = random.randint(100,150)
    p_atk = random.randint(15,25)
    m_name1 = ["슬라임", "고블린", "산적", "스켈레톤", "좀비", "임프"]
    m_name2 = ["오크", "데스웜", "홉고블린", "구울", "놀 워리어", "산적 간부"]
    m_name3 = ["놀 치프틴", "오크 워리어", "듀라한", "산적 두목", "중급 악마", "산성 슬라임"]
    m_name_boss = ["여왕 놀", "오크 대족장", "데스나이트", "악마 귀족", "킹 슬라임"]

    m_count = 1
    reset_count = 5

    while game_start:
        exp = 0
        level = 1
        print("<< 어서오세요 용사님! >>")
        a = input("<< 용사님의 이름을 알려주세요! >> :")
        p_stats = {"name" : a, "hp" : p_hp, "attack" : p_atk} 
        time.sleep(0.3)
        print(f"<< {p_stats['name']}용사님의 스텟을 설정했어요! >>")
        print(f"<< {p_stats['name']}용사님의 현제 스텟 >>")
        time.sleep(0.3)
        print("=============================")
        print(f"용사 {p_stats['name']}")
        print(f"레벨 : {level}")
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

                    reset_again = int(input("<< 한번 더 변경하시려면 1번을 이대로 모험을 시작하시려면 2번을 눌러주세요! >> : "))
                        
                    if reset_again == 1:
                        continue
                    
                    elif reset_again == 2:
                        print("<< 좋아요 용사님! 이대로 모험을 출발하겠습니다! >>")
                        stats_reset = False
                        break
                    
                    else:
                        print("<< 잘못 입력하셨어요 용사님! >>")
                        continue

            elif b == 2:
                print("<< 현재 스텟으로 모험을 시작합니다! >>")
                break

            else:
                print("<< 잘못된 입력이에요 용사님! >>")
                continue
            
        p_max_hp = p_stats["hp"]

        while adventure:
            m_hp = random.randint(50,100)
            m_atk = random.randint(10,20)
            
            if m_count >= 1 and m_count <= 3:
                 m_name_random = random.choice(m_name1)
            
            elif m_count >= 4 and m_count <= 6:
                m_name_random = random.choice(m_name2)
                m_hp = int(m_hp * 1.3)
                m_atk = int(m_atk * 1.3)
            
            elif m_count >= 7 and m_count <= 9:
                m_name_random = random.choice(m_name3)
                m_hp = int(m_hp * 1.6)
                m_atk = int(m_atk * 1.6)

            elif m_count % 10 == 0:
                m_name_random = random.choice(m_name_boss)
                m_hp = int(m_hp * 5)
                m_atk = int(m_atk * 3)

            elif m_count >= 10:
                m_name_random = random.choice(m_name3)
                m_hp = int(m_hp * 2)
                m_atk = int(m_atk * 2)
            
            m_stats = {"name" : m_name_random, "hp" : m_hp, "attack" : m_atk}
            m_max_hp = m_stats["hp"]

            print("========= 전투 시작 =========")
            print(f"용사 {p_stats['name']}")
            print(f"레벨 : {level}")
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
                print(f"용사 {p_stats['name']} | 레벨 : {level} | 체력 : {p_stats['hp']} | 공격력 : {p_stats['attack']}")
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
                        time.sleep(0.3)
                        print(f"<<{m_stats['name']}은 큰 피해를 입었다! >>")
                        battle_result = m_stats["hp"] - p_stats["attack"] * 2
                        m_stats["hp"] = battle_result
                        m_stats["hp"] = max(0, m_stats["hp"])
                        time.sleep(0.3)
                        print(f"<< {m_stats['name']}의 현재 체력 : {m_stats['hp']}/{m_max_hp}>>")
                    
                    else:
                        print("<< 용사의 일격! >>")
                        time.sleep(0.3)
                        print(f"<<{m_stats['name']}은 피해를 입었다! >>")
                        battle_result = m_stats["hp"] - p_stats["attack"]
                        m_stats["hp"] = battle_result
                        m_stats["hp"] = max(0, m_stats["hp"])
                        time.sleep(0.3)
                        print(f"<< {m_stats['name']}의 현재 체력 : {m_stats['hp']}/{m_max_hp}>>")

                    if m_stats["hp"] <= 0:
                        time.sleep(0.3)
                        print(f"<< {m_stats['name']}은 쓰러졌다! >>")
                    
                elif p_active == 2:
                    print("<< 용사의 회복! >>")
                    time.sleep(0.3)
                    critical_heal = random.randint(1,100)
                    heal = random.randint(20,150)

                    if critical_heal <= 40:
                        print("<< 기적적인 치유! >>")
                        p_stats["hp"] = min(p_stats["hp"] + (heal * 2), p_max_hp)
                        time.sleep(0.3)
                        print(f"<< 현제 체력 : {p_stats['hp']}/{p_max_hp}>>")

                    else:
                        print("<< 따뜻한 치유! >>")
                        p_stats["hp"] = min(p_stats["hp"] + heal, p_max_hp)
                        time.sleep(0.3)
                        print(f"<< 현제 체력 : {p_stats['hp']}/{p_max_hp}>>")
                
                elif p_active == 3:
                    print("<< 용사의 방어! >>")
                    time.sleep(0.3)
                    block = random.randint(1,100)
                    if block <= 20:
                        print("<< 완벽한 방어! >>")
                        dmz = 0

                    else:
                        print("<< 평범한 방어! >>")
                        dmz = m_stats["attack"] // 2

                else:
                    print("<< 잘못된 입력이에요 용사님! >>")
                    continue
                
                if m_stats["hp"] > 0 and (p_active == 1 or p_active == 2 or p_active == 3):
                    print(f"{m_stats['name']}의 반격!")
                    time.sleep(0.3)
                    m_critical = random.randint(1,100)
                    
                    if m_critical <= 20:
                        print("<< 치명적 일격! >>")
                        time.sleep(0.3)
                        print(f"<< 용사 {a}는 큰 피해를 입었다! >>")
                        m_result = p_stats["hp"] - dmz * 2
                        p_stats["hp"] = m_result
                        p_stats["hp"] = max(0, p_stats["hp"])
                        time.sleep(0.3)
                        print(f"<< 용사{p_stats['name']}의 현재 체력 : {p_stats['hp']}/{p_max_hp}>>")
                                
                    else:
                        print("<< 몬스터의 일격! >>")
                        time.sleep(0.3)
                        print(f"<< 용사 {a}는 피해를 입었다! >>")
                        m_result = p_stats["hp"] - dmz
                        p_stats["hp"] = m_result
                        p_stats["hp"] = max(0, p_stats["hp"])
                        time.sleep(0.3)
                        print(f"<< 용사{p_stats['name']}의 현재 체력 : {p_stats['hp']}/{p_max_hp}>>")

            if p_stats["hp"] <= 0:
                time.sleep(0.3)
                print(f"<< 으악으악! 용사{p_stats['name']}의 눈 앞이 깜깜해졌다! >>")
                print("<< 용사님 다시 도전하시겠어요? >>")
                while True:
                    re_start = int(input("<< 1. 환생        2. 영면 >>\n"))

                    if re_start == 1:
                        time.sleep(0.3)
                        print("<< 눈을 뜨세요 용사님! >>")
                        adventure = False
                        stats_reset = False
                        game_start = False
                        break

                    elif re_start == 2:
                        time.sleep(0.3)
                        print("<< 편안한 휴식을 취하세요 용사님 >>")
                        adventure = False
                        stats_reset = False
                        game_start = False
                        before_start = False
                        break

                    else:
                        print("<< 잘못된 입력이에요 용사님! >>")
                        continue

            elif m_stats["hp"] <= 0:
                time.sleep(0.3)
                exp += 10
                print(f"<< {m_stats['name']}를 물리쳤어요 대단해요 용사님! >>")
                if exp >= 30:
                    exp -= 30
                    level += 1
                    up_h_stats_random = random.randint(10,20)
                    up_a_stats_random = random.randint(3,7)
                    time.sleep(0.3)
                    print("<< 레벨 업! >>")
                    time.sleep(0.3)
                    print(f"<< 체력 + {up_h_stats_random} >>")
                    print(f"<< 공격력 + {up_a_stats_random} >>")
                    p_max_hp = p_max_hp + up_h_stats_random
                    p_stats["hp"] = p_max_hp
                    p_stats["attack"] = p_stats["attack"] + up_a_stats_random
                m_count += 1
                time.sleep(0.3)
                print(f"<< 현재 레벨과 경험치는 {level}|{exp}에요! >>")
                time.sleep(0.3)
                print("<< 다음 적을 쓰러뜨리기 위한 모험을 출발할까요?>>")
                time.sleep(0.3)
                while True:
                    re_start = int(input("<< 1. 나아간다        2. 모험을 끝낸다 >>\n"))

                    if re_start == 1:
                        break

                    elif re_start == 2:
                        print("<< 즐거운 모험이었습니다 용사님! >>")
                        adventure = False
                        stats_reset = False
                        game_start = False
                        before_start = False
                        break

                    else:
                        print("<< 질못된 입력이에요 용사님! >>")
                        continue
