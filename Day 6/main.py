from sys import setrecursionlimit
setrecursionlimit(100000)

def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def no_of_chars_before_first_packet_marker(input_string,first_char_index=0, end_char_index=14):
    if len(set(input_string[first_char_index:end_char_index])) == len(input_string[first_char_index:end_char_index]):
        print(end_char_index)
    else:
        first_char_index += 1
        end_char_index += 1
        no_of_chars_before_first_packet_marker(input_string, first_char_index, end_char_index)

def main():
    data = read_in_file_to_list('data/input.txt')
    no_of_chars_before_first_packet_marker(data[0])

if __name__ == "__main__":
    main()
