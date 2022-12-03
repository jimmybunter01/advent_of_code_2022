def get_input_data(filename):
    with open(filename) as file:
        lines = file.readlines()
        return lines

def get_best_elf(data, elf_number, best_total, best_elf):
    try:
        new_elf_index = data.index('\n')
        current_elf = data[0:new_elf_index]
        current_total = 0
        for string_num in current_elf:
            num = int(string_num.strip('\n'))
            current_total += num
        
        print(elf_number, current_total)
        print()

        if current_total > best_total:
            get_best_elf(data[new_elf_index+1:-1], elf_number+1, current_total, elf_number)
        else:
            get_best_elf(data[new_elf_index+1:-1], elf_number+1, best_total, best_elf) 
            
    except ValueError:
        print("~~~~")
        print(f"Best Elf: {best_elf}, with {best_total} calories!")

def get_top_three_elves(data, elf_number, three_best_totals):
    try:
        new_elf_index = data.index('\n')
        current_elf = data[0:new_elf_index]
        current_total = 0
        for string_num in current_elf:
            num = int(string_num.strip('\n'))
            current_total += num
        
        three_best_dict_length = len(three_best_totals.keys())
        current_elf_dict = {'Elf Number': elf_number, 'Calories': current_total}

        if three_best_dict_length == 0:
            three_best_totals[1] = current_elf_dict

        elif three_best_dict_length == 1:
            if current_total > three_best_totals[1]['Calories']:
                three_best_totals[2] = three_best_totals[1]
                three_best_totals[1] = current_elf_dict
            else:
                three_best_totals[2] = current_elf_dict

        elif three_best_dict_length == 2:
            if (current_total > three_best_totals[2]['Calories']) & (current_total < three_best_totals[1]['Calories']):
                three_best_totals[3] = three_best_totals[2]
                three_best_totals[2] = current_elf_dict
            elif (current_total > three_best_totals[2]['Calories']) & (current_total > three_best_totals[1]['Calories']):
                three_best_totals[3] = three_best_totals[2]
                three_best_totals[2] = three_best_totals[1]
                three_best_totals[1] = current_elf_dict
            else:
                three_best_totals[3] = current_elf_dict
        
        else:
            if (current_total > three_best_totals[3]['Calories']) & (current_total > three_best_totals[2]['Calories']) & (current_total > three_best_totals[1]['Calories']):
                three_best_totals[3] = three_best_totals[2]
                three_best_totals[2] = three_best_totals[1]
                three_best_totals[1] = current_elf_dict
            elif (current_total > three_best_totals[3]['Calories']) & (current_total > three_best_totals[2]['Calories']) & (current_total < three_best_totals[1]['Calories']):
                three_best_totals[3] = three_best_totals[2]
                three_best_totals[2] = current_elf_dict
            elif (current_total > three_best_totals[3]['Calories']) & (current_total < three_best_totals[2]['Calories']):
                three_best_totals[3] = current_elf_dict

        get_top_three_elves(data[new_elf_index+1:-1], elf_number+1, three_best_totals)

    except ValueError:
        overall_total = 0
        for num in range(1, 4):    
            overall_total += three_best_totals[num]['Calories']

        print("~~~~")
        print(f"The Top Three Elves are: {three_best_totals}")
        print(f"Total Number of Calories {overall_total}")


def main():
    data = get_input_data('data/input.txt')
    # get_best_elf(data, 1, 0, 0)
    get_top_three_elves(data, 1, {})

if __name__ == '__main__':
    main()