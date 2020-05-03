from random import shuffle
from time import sleep



user = input("Введите Ваше имя: ")
print(f"\nПривет, {user}! ^^,)")


i = 0
while True:
    i+=1 # счётчик итераций цикла
    if i == 1:
        inp = input("Ну что, поиграем?\ny/n: ")
    else:
        inp = input("\n\nИграем?\ny/n: ")
        

    koloda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4 # ОДНА колода
    shuffle(koloda)
    hand = []
    d_hand = []
    sum_hand_player = 0


    def sum_hand(A=11, hand=hand):
        ''' Считает "руку". Позволяет (взамен функции "sum()") оставить вывод "карт-картинок", а не их числовой эквивалент '''

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
        hand.append(koloda.pop())

        d_hand.append(koloda.pop())
        d_hand.append(koloda.pop())

        
        while True:
            ''' Ход игрока. '''
            
            print(f"\nВаша 'рука': {hand}.")
            print(f"'Рука' Вашего оппонента: {[d_hand[0],]}")
            
            if sum_hand() < 21:
                us = input(f"{user}, хотите взять ещё одну карту?\ny/n: ")
                if us == 'y':
                    hand.append(koloda.pop())
                    
                elif us == 'n':
                    print(f"Ваш результат: {sum_hand()}\n\n")
                    sum_hand_player = sum_hand()
                    break

                else:
                    print("Неверный ввод! Попробуй ещё раз.")
                
            elif sum_hand() == 21:
                print(f"{user}, Вы собрали 21. Поздравляем!\n\n")
                sum_hand_player = sum_hand()
                break
            
            elif sum_hand() > 21:
                if 'A' in hand:
                    if sum_hand(1) < 21:
                        us = input(f"{user}, хотите взять ещё одну карту?\ny/n: ")
                        if us == 'y':
                            hand.append(koloda.pop())
                            
                        elif us == 'n':
                            print(f"Ваш результат: {sum_hand(1)}\n\n")
                            sum_hand_player = sum_hand(1)
                            break

                        else:
                            print("Неверный ввод! Попробуй ещё раз.")
                        
                    elif sum_hand(1) == 21:
                        print(f"{user}, Вы собрали 21. Поздравляем!\n\n")
                        sum_hand_player = sum_hand(1)
                        break
                    
                    else:
                        print("У Вас больше 21.\n\n")
                        sum_hand_player = sum_hand(1)
                        break
                    
                else:
                    print("У Вас больше 21.\n\n")
                    sum_hand_player = sum_hand()
                    break


        while True:
            ''' Играет компьютер. Сравнение и вывод арезультатов. '''

            if sum_hand_player > 21:
                print(f"Жадность фраера сгубила! :)\n{user}, Вы проиграли. Повезёт в следующий раз! ;)")
                break
            
            elif sum_hand(11, d_hand) == sum_hand_player or sum_hand(1, d_hand) == sum_hand_player:
                print("\n\nНичья!\nПопробуйте ещё раз!")
                print(f"'Рука' Вашего оппонента: {d_hand}")
                break
                
            elif sum_hand(11, d_hand) > sum_hand_player:
                if sum_hand(11, d_hand) <= 21:
                    print(f"\n\n{user}, Вы проиграли. Повезёт в следующий раз! ;)")
                    print(f"'Рука' Вашего оппонента: {d_hand}")
                    break

                elif sum_hand(11, d_hand) > 21:
                    print(f"\n\nУдача на Вашей стороне!\n{user}, Вы выиграли!\n'Рука' Вашего оппонента: {d_hand}.\nПродолжайте в том же духе! ;)")
                    break 

            elif sum_hand(11, d_hand) < sum_hand_player or sum_hand(1, d_hand) < sum_hand_player:
                print(f"'Рука' Вашего оппонента: {d_hand}.")
                print("Оппонент тянет карту.")
                sleep(2)
                d_hand.append(koloda.pop())


    elif inp == 'n':
        print("До скорого! ^^,)")
        break

    else:
        print("Неверный ввод! Попробуй ещё раз.")







''' by
          Ivan Romanchenko
                             03.05.2020 '''
