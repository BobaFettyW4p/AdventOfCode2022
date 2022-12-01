def import_data(data):
    with open('inputfile.txt', 'r') as f:
        content = f.readlines()
        for row in content:
            data.append(row)
        return data


def calculate_load(data, elves):
    load = 0
    for package in data:
        package = package[slice(-2)])
        if len(package) == 0:
            elves.append(load)
        else:
            package = int(package)
            load+=package
    return elves


def find_highest(loads):
    pass

if __name__ == '__main__':
    elves = []
    data =[]
    import_data(data)
    calculate_load(data, elves)
    print(elves)
    #find_highest()
