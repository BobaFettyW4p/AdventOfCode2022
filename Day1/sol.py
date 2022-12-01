def import_data(data):
    with open('inputfile.txt', 'r') as f:
        content = f.readlines()
        for row in content:
            data.append(row)
        return data


def calculate_load(data, elves):
    load = 0
    for package in data:
        package = package[slice(-1)]
        if len(package) == 0:
            elves.append(load)

            load = 0
        else:
            package = int(package)
            load+=package
    return elves

def find_highest(elves):
    max = 0
    for elf in elves:
        if elf > max:
            max = elf
    return max

if __name__ == '__main__':
    elves = []
    data =[]
    import_data(data)
    calculate_load(data, elves)
    print (f'The highest number of calories is {find_highest(elves)}')
