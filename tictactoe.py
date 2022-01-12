def main ():
    current_player = "X"
    numlist = create_num()

    while winner(numlist) != True :
        board(numlist)
        move(current_player, numlist)
        current_player = next_player(current_player)
    board(numlist)
    print(f"PLAYER {next_player(current_player)} WINS") 
    print(f"Good game. Thanks for playing!") 


def create_num():
    digits = []
    for num in range(9):
        digits.append(num+1)
    return digits

def board(num):
    print()
    print(f"{num[0]}|{num[1]}|{num[2]}")
    print('-+-+-')
    print(f"{num[3]}|{num[4]}|{num[5]}")
    print('-+-+-')
    print(f"{num[6]}|{num[7]}|{num[8]}")
    print()

def next_player(current):
    if current == "O":
        return "X"
    elif current == "X":
        return "O"

def move(player, digits):
    desired_move = int(input(f"{player}'s turn to choose a square (1-9): "))
    digits[desired_move - 1] = player

def winner(num):
    return (num[0] == num[1] == num[2] or
            num[3] == num[4] == num[5] or
            num[6] == num[7] == num[8] or
            num[0] == num[3] == num[6] or
            num[1] == num[4] == num[7] or
            num[2] == num[5] == num[8] or
            num[0] == num[4] == num[8] or
            num[2] == num[4] == num[6])

if __name__ == "__main__":
    main()