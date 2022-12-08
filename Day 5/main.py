def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def parse_stacks(raw_stacks):
    parsed_stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    # If there is no crate there are 4 '' in it's place unless the missing/blank crate is in stack 9.
    # In stack 9 the last '' is replace with a \n.

    for row in raw_stacks:
        stack = 1
        index = 0
        split_row = row.split(' ')
        enumerated_row = list(enumerate(split_row, start=index))
        potential_crate = enumerated_row[index][1]

        while stack < 10:
            potential_crate = enumerated_row[index][1]
            if (potential_crate != '') & (potential_crate != '\n'):
                 crate = potential_crate.strip("\n")
                 parsed_stacks[stack].append(crate)
                 stack += 1
                 index += 1
            elif (potential_crate == '') & ((enumerated_row[index+3][1] == '') | (enumerated_row[index+3][1] == '\n')):
                 stack += 1
                 index += 4
    
    return parsed_stacks
                
def parse_instructions(raw_instructions):
    parsed_instructions = []

    for instruction in raw_instructions:
        split_instruction = instruction.split(' ')
        no_of_crates = int(split_instruction[1])
        stack_from = int(split_instruction[3])
        stack_to = int(split_instruction[5])

        parsed_instructions.append([no_of_crates, stack_from, stack_to])
    
    return parsed_instructions

def sort_the_stacks(stacks, instructions):
    stacks_to_sort = stacks

    for instruction in instructions:
        no_of_crates = instruction[0]
        stack_from = instruction[1]
        stack_to = instruction[2]

        for i in range(1, no_of_crates+1):
            crate_to_move = stacks[stack_from].pop(0)
            stacks_to_sort[stack_to].insert(0, crate_to_move)

    sorted_stacks = stacks_to_sort

    return sorted_stacks

def main():
    data = read_in_file_to_list('data/input.txt')
    raw_stacks = data[0:9]
    raw_instructions = data[10:len(data)+1]
    parsed_stacks = parse_stacks(raw_stacks)
    parsed_instructions = parse_instructions(raw_instructions)
    sorted_stacks = sort_the_stacks(parsed_stacks, parsed_instructions)
    
    for i in range(1,10):
        print(sorted_stacks[i][0].strip('[').strip(']'), end='')

if __name__ == '__main__':
    main()