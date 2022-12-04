# A = Rock
# B = Paper
# C = Scissors

# X = Loose
# Y = Draw
# Z = Win

# Rock > Scissors
# Scissors > Paper
# Paper > Rock

def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def determine_points(opponent_choice, player_choice):
    loose_points_dict = {
        'A' : 3 # Rock beats Scissors
        , 'B' : 1 # Paper beats Rock  
        , 'C' : 2 # Scissors beats Paper
    }

    draw_points_dict = {
        'A' : 1 # Rock vs Rock
        , 'B' : 2 # Paper vs Paper
        , 'C' : 3 # Scissors vs Scirssors
    }

    win_points_dict = {
        'A': 2 # Rock are beaten by Paper
        , 'B': 3 # Paper are beaten by Scissors
        , 'C': 1 # Scissors are beaten by Rock 
    }

    # Loose
    if (player_choice == 'X'):
        points = loose_points_dict[opponent_choice] + 0
        return points
    
    # Draw
    elif (player_choice == 'Y'):
        points = draw_points_dict[opponent_choice] + 3
        return points
    
    # Win
    elif (player_choice == 'Z'):
        points = win_points_dict[opponent_choice] + 6
        return points

def get_total(data):
    total = 0
    for round in data:
        seperate_inputs = round.split(' ')
        total += determine_points(seperate_inputs[0], seperate_inputs[1].strip('\n'))
    return total

def main():
    data = read_in_file_to_list("../data/input.txt")
    total = get_total(data)
    print(total)

if __name__ == '__main__':
    main()