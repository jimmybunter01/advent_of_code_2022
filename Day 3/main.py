def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def split_lines(line):
    cleaned_line = line.strip('\n')
    halfway = int(len(cleaned_line) / 2)

    first_compartment = cleaned_line[0:halfway]
    second_compartment = cleaned_line[halfway:len(cleaned_line)]

    return first_compartment, second_compartment

def compare_compartments(first_compartment, second_compartment):
    letter_priority = 0
    
    for letter in first_compartment:
        if letter in second_compartment:    
            decimal_letter = ord(letter)
            if decimal_letter > 96:
                letter_priority = decimal_letter - 96
                break
            else:
                letter_priority = decimal_letter - 38
                break
                
    return letter_priority

def compare_three_elves(first_elf, second_elf, third_elf):
    letter_priority = 0

    for letter in first_elf:
        if (letter in second_elf) & (letter in third_elf):
            decimal_letter = ord(letter)
            if decimal_letter > 96:
                letter_priority = decimal_letter - 96
                break
            else:
                letter_priority = decimal_letter - 38
                break

    return letter_priority


def main():
    data = read_in_file_to_list('data/input.txt')
    total = 0
    
    # for rucksack in data:
    #     first_compartment, second_compartment = split_lines(rucksack)
    #     priority = compare_compartments(first_compartment, second_compartment)
    #     total += priority

    data_len = len(data)

    for i in range(0, len(data), 3):
        three_elves = data[i:i+3]
        first_elf = three_elves[0].strip('\n')
        second_elf = three_elves[1].strip('\n')
        third_elf = three_elves[2].strip('\n')            

        total += compare_three_elves(first_elf, second_elf, third_elf)    

    print(total)

if __name__ == '__main__':
    main()