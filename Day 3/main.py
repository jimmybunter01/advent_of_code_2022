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

# Lowercase Letter We Take 96
# Uppercase Letter We Take 38

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

def main():
    data = read_in_file_to_list('data/input.txt')
    total = 0
    for rucksack in data:
        first_compartment, second_compartment = split_lines(rucksack)
        priority = compare_compartments(first_compartment, second_compartment)
        total += priority
    print(total)

if __name__ == '__main__':
    main()