def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def compare_assignment_pairs(data):
    count = 0
    for assigment_pair in data:
        pair_one, pair_two = assigment_pair.split(',')
        lower_bound_pair_one, upper_pound_pair_one = pair_one.split('-')
        lower_bound_pair_two, upper_pound_pair_two = pair_two.split('-')
        
        # Check if Pair One is Contained within Pair Two
        if (int(lower_bound_pair_one) >= int(lower_bound_pair_two)) & (int(upper_pound_pair_one) <= (int(upper_pound_pair_two))):
            print("One is within Two!")
            count += 1

        # Check if Pair Two is Contained within Pair One
        elif (int(lower_bound_pair_two) >= int(lower_bound_pair_one)) & (int(upper_pound_pair_two) <= (int(upper_pound_pair_one))):
            print("Two is within One!")
            count += 1


    return count


def main():
    data = read_in_file_to_list('data/input.txt')
    count = compare_assignment_pairs(data)
    print(count)

if __name__ == '__main__':
    main()