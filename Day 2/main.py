# A / X = Rock
# B / Y = Paper
# C / Z = Scissors

# Rock > Scissors
# Scissors > Paper
# Paper > Rock

def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def determine_points(opponent_choice, player_choice):
    point_dict = {'X': 1, 'Y': 2, 'Z': 3}
    points = point_dict[player_choice]

    if ((opponent_choice == 'A') & (player_choice == 'X')) | ((opponent_choice == 'B') & (player_choice == 'Y')) | ((opponent_choice == 'C') & (player_choice == 'Z')):
        return points + 3 
    elif (opponent_choice == 'A') & (player_choice == 'Y'):
        return points + 6
    elif (opponent_choice == 'B') & (player_choice == 'Z'):
        return points + 6
    elif (opponent_choice == 'C') & (player_choice == 'X'):
        return points + 6
    else:
        return points + 0

def get_total(data):
    total = 0
    for round in data:
        seperate_inputs = round.split(' ')
        total += determine_points(seperate_inputs[0], seperate_inputs[1].strip('\n'))
    return total

def main():
    data = read_in_file_to_list("data/input.txt")
    total = get_total(data)
    print(total)

if __name__ == '__main__':
    main()