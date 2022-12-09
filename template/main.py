def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def main():
    data = read_in_file_to_list("data/input.txt")

if __name__ == '__main__':
    main()