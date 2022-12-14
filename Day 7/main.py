class directory:
    '''Class to keep track of of a directory structure.'''

    def __init__(self, directory_name, parent_directory, sub_directories, size):
        self.directory_name = directory_name 
        self.parent_directory = parent_directory
        self.sub_directories = sub_directories
        self.size = size

def read_in_file_to_list(filename):
    with open(filename) as file:
        data = file.readlines()
        return data

def clean_data(non_clean_data):
    cleaned_data = []
    for line in non_clean_data:
        cleaned_data.append(line.strip('\n'))
    return cleaned_data

def determine_directory_structure(instructions):
    # Want to get the directory structure first '/' --> to the bottom.
    # How to structure this? Dicts? Lists? Some sort of graph?
    
    # Commands:
    #   cd <dir_name> : change to this sub directory.
    #   cd .. : go up one directory / move into parent directory
    #   cd / : go to the top-level / root directory.
    #   ls : list all the files & direcotires contained within the current one.
    # Note - all lines with a command on start with $. 
    
    # Directory Dict = "Name" : {"Parent Directory" : "Parent Directory Name", "Subdirectories" : [{directory_dict}], size: 0}

    directory_structure = {'/': {"Parent Directory": None, "Subdirectories": [], size: 0}}
    current_directory = None
    checking_for_files = False

    for line in instructions:
        if checking_for_files == False:
            if line[0] == '$':
                if (line[2:4] == 'cd') & (line[5:len(line)] != '..'):
                    current_directory_name = line[5:len(line)]
                    
                    if line[5:len(line)] == '/':
                        print("Root directory!")
                        
                    else:
                        parent_directory = current_directory
                        new_directory = directory(current_directory_name, parent_directory=parent_directory, sub_directories=[], size=0) 
                        parent_directory.sub_directories.append(current_directory)
                        current_directory = new_directory

                elif (line[2:4] == 'cd') & (line[5:len(line)] == '..'):
                        previous_directory = current_directory
                        current_directory = previous_directory.parent_directory
                        current_directory.size += previous_directory.size

                        # Need to update the size of the parent directory with the size of the sub directory we have just left.
                    
                elif line[2:4] == "ls":
                    checking_for_files = True
        else:
            split_file = line.split(' ')
            try:
                file_size = int(split_file[0])
                current_directory.size += file_size
            except:
                break

    print(current_directory.size)



def determine_directory_size(directory):
    print("Calculating directory size!")


def main():
    data = read_in_file_to_list("data/input.txt")
    cleaned_data = clean_data(data)
    directory_structure = determine_directory_structure(cleaned_data[0:11])    

if __name__ == "__main__":
    main()