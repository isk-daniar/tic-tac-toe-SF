import  random

print("-" * 15, "ДА начнутся КРЕСТИКИ-НОЛИКИ!!!", "-" * 17)
print("-" * 14, "И пусть удача всегда будет с вами!", "-" * 14)


lines = list(range(1, 10))

def print_lines(lines):
    print("-" * 13)
    for i in range(3):
        print("|", lines[0 + i * 3], "|", lines[1 + i * 3], "|", lines[2 + i * 3], "|")
        print("-" * 13)


random_slova =["Ходи давай!!! ", "Давай-давай!!! ", "Go-Go-Goo!!! ", "Не тормази!!! "]


def input_user(player_symbol):
    actions = False
    while not actions:
        player_move = input(random.choice(random_slova) + player_symbol + " =")
        try:
            player_move = int(player_move)
        except:
            print("Туп... Глупый что-ли. Введи число")
            continue
        if player_move >= 1 and player_move <= 9:
            if(str(lines[player_move -1 ]) not in "X0"):
                lines[player_move -1] = player_symbol
                actions = True
            else:
                print("Ну ё-моё, не видишь клетка занета")

        else:
            print("Seriously?, Введи число от 1 до 9")

def chicken_win(lines):
    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for j in win_line:
        if lines[j[0]] == lines[j[1]] == lines[j[2]]:
            return lines[j[0]]
    return False

random_win_slova = ["Win!!!", "Выйграл!!!","Наш победитель!!!"]

def game(lines):
    counter = 0
    win = False
    while not win:
        print_lines(lines)
        if counter % 2 == 0:
            input_user("X")
        else:
            input_user("0")
        counter += 1
        if counter > 4:
            result = chicken_win(lines)
            if result:
                print(result, random.choice(random_win_slova))
                win = True
                break
        if counter == 9:
                print("Ничья!!!")
                break
    print_lines(lines)
game(lines)

input("Нажмите Enter для выхода!")