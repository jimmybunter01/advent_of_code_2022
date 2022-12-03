def get_input_data(filename):
    with open(filename) as file:
        lines = file.readlines()
        return lines

def split_elves_to_list(data, elf_number, best_total, best_elf):
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
            split_elves_to_list(data[new_elf_index+1:-1], elf_number+1, current_total, elf_number)
        else:
            split_elves_to_list(data[new_elf_index+1:-1], elf_number+1, best_total, best_elf) 
            
    except ValueError:
        print("~~~~")
        print(f"Best Elf: {best_elf}, with {best_total} calories!")

def main():
    data = get_input_data('data/input.txt')
    split_elves_to_list(data, 1, 0, 0)

if __name__ == '__main__':
    main()