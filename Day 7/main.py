def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def determine_directory_size(directory):
    print("Calculating directory size!")


def main():
    data = read_in_file_to_list("data/input.txt")
    print(data)

if __name__ == "__main__":
    main()