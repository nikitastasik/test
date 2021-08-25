name_player_one = input('Игрок 1 введите свое имя: ')
print(f'Привет, {name_player_one}')
name_player_two = input('Игрок 2 введите свое имя: ')
print(f'Привет, {name_player_two}')
count_sticks = int(input('Введите количество палочек '))
print(f'Кол-во палочек в игре: {count_sticks}')
print("You wanna play? Let's play")

from random import *
#who goes first
first_player, second_player = False, False
if randint(0, 1) == 1:
    second_player = True
    print(f'Первым ходит {name_player_two}')
else:
    first_player = True
    print(f'Первым ходит {name_player_one}')

#conditions for moves
while count_sticks > 0:
    if first_player == True:
        act_count_sticks = int(input(f'{name_player_one}, тяни от одной до трех палочек '))
        count_sticks -= act_count_sticks
        print(f'Палочек осталось: {count_sticks}')
        first_player = False
        second_player = True
        if count_sticks == 1:
            print(f'{name_player_two} loser ahah')
            break
    else:
        act_count_sticks = int(input(f'{name_player_two}, тяни от одной до трех палочек '))
        count_sticks -= act_count_sticks
        print(f'Палочек осталось: {count_sticks}')
        first_player = True
        second_player = False
        if count_sticks == 1:
            print(f'{name_player_one} loser ahah')
            break