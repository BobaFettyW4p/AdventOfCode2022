def import_data():
    with open('input.txt','r') as f:
        content = f.readlines()
        return [x[:-1] for x in content]

def parse_data(data):
    directories = {}
    files_within = {}
    pwd = ''
    for line in data:
        if line[0]=='$':
            pwd = parse_command(line, pwd, directories, files_within)
        elif line[:3] == 'dir':
            directories[pwd].append(f'{pwd}/{line[4:]}')
        else:
            total_size = ''
            for character in line:
                if character != ' ':
                    total_size=f'{total_size}{character}'
                else:
                    total_size = int(total_size)
                    files_within[pwd]+=int(total_size)
                    break
    return directories, files_within

                

def parse_command(line, pwd, directories, files_within):
    if line[2:4] == 'cd':
        if line[5:7] == '..':
            pwd = find_parent_folder(pwd, directories)
        else:
            pwd = f'{pwd}/{line[5:]}'
            if pwd not in directories.keys():
                directories[pwd] = []
                files_within[pwd] = 0
    return pwd

def find_parent_folder(pwd, directories):
    for key,values in directories.items():
        for value in values:
            if pwd == value:
                return key
    return ''

def get_total_folder_size(directories, files_within):
    total_folder_size = {}
    for key, values in sorted(directories.items(), reverse=True):
        totalSum = 0
        for value in values:
            totalSum += files_within[value]
        total_folder_size[key] = totalSum
    for key in files_within.keys():
        files_within[key]+=total_folder_size[key]
    return files_within

def find_sufficiently_small_folders(files_within):
    solution = 0
    for key in sorted(files_within.keys(), reverse=True):
        #print(f'checking directory {key}: size {files_within[key]}')
        if files_within[key] <= 100000:
            solution+= files_within[key]
            #print(f'add {key} with value {files_within[key]} to solution. running total: {solution}')
    return solution


if __name__ == "__main__":
    data = import_data()    
    directories, files_within = parse_data(data)
    #print(f'directory tree is {directories}, directory sizes are {files_within}')
    #files_within = get_total_folder_size(directories, files_within)
    #print(files_within)
    print(files_within)
    files_within = get_total_folder_size(directories, files_within)
    print(find_sufficiently_small_folders(files_within))
