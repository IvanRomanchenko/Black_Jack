from random import shuffle


user = input("Введите Ваше имя: ")
print(f"\nПривет, {user}! ^^,)")
inp = input("Ну что, поиграем?\ny/n: ")


koloda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
shuffle(koloda)
hand = []


def sum_hand(A=11):
    s = 0
    for i in hand:
        if i == 'J' or i == 'Q' or i == 'K':
            s += 10
        elif i == 'A':
            s += A
        else:
            s += i
    return s

    
if inp == 'y':
    hand.append(koloda.pop())
    
    while True:
        print(f"Ваша 'рука': {hand}.")
        if sum_hand() < 21:
            us = input(f"{user}, хотите взять ещё одну карту?\ny/n: ")
            if us == 'y':
                hand.append(koloda.pop())
            elif us == 'n':
                print(f"Ваш результат: {sum_hand()}")
                break
            
        elif sum_hand() == 21:
            print(f"{user}, Вы собрали 21. Поздравляем!")
            break
        
        elif sum_hand() > 21:
            if 'A' in hand:
                if sum_hand(1) < 21:
                    us = input(f"{user}, хотите взять ещё одну карту?\ny/n: ")
                    if us == 'y':
                        hand.append(koloda.pop())
                    elif us == 'n':
                        print(f"Ваш результат: {sum_hand(1)}")
                        
                elif sum_hand(1) == 21:
                    print(f"{user}, Вы собрали 21. Поздравляем!")
                    break
                
                else:
                    print(f"У Вас больше 21.\n{user}, Вы проиграли!")
                    break
                
            else:
                print(f"У Вас больше 21.\n{user}, Вы проиграли!")
                break



elif inp == 'n':
    print("Зачем тогда запускал игру? О_о")
    
else:
    print("Неверный ввод. Перезапусти программу")
