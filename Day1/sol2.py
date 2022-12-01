#This function iterates through the txt with the ingest data
#and appends the value of each line to the data list (begins empty)
def import_data(data):
    with open('inputfile.txt', 'r') as f:
        content = f.readlines()
        for row in content:
            data.append(row)
        return data

#This function starts with the data imported from the import_data function
#and determines the full load each individual elf is carrying
def calculate_load(data, elves):
    load = 0
    for package in data:
        #this slices off the carriage return present at the end of every line
        package = package[slice(-1)]
        #once the carriage return line is over, we've reached our base case
        #the value of load is the total load the elf is carrying, add it to our array
        #and repeat the process
        if len(package) == 0:
            elves.append(load)
            load = 0
        #else case adds current package to load and continues iterating
        else:
            package = int(package)
            load+=package
    return elves

#This function was used in part 1 to determine the highest total load
#it iterates over the elves array and finds the highest value
def find_highest(elves):
    max = 0
    for elf in elves:
        if elf > max:
            max = elf
    return max
#This function was used in part 2
#It uses the elves array plus a second top_three array initialized to [0,0,0]
#iterates over the array and updates the top three
def find_highest_three(elves, top_three):
    for elf in elves:
        #This doesn't have to be a loop, with the way this is set up, only the first item can ever be tripped. A better way would be to compare to index 0, update if needed and resort the array
        for position, load in enumerate(top_three):    
            #if tripped, this means the current elf's load is in the top 3 and needs to be added to it
            #We have to sort the array afterwards because we want to ensure that if a new value is added, only the lowest is dropped off
            if elf > load:
                print(f'{elf} is greater than {load}, add it to the top three')
                top_three[position] = elf
                top_three.sort()
                break
            else:
                continue
    return top_three

if __name__ == '__main__':
    elves = []
    data =[]
    top_three = [0,0,0]
    import_data(data)
    calculate_load(data, elves)
    find_highest_three(elves, top_three)
    #This provided our solution from part 1
    #print(f'The highest number of calories is {find_highest(elves)}')
    #provides the correct answer (confirmed via the website)
    print(f'the 3 heaviest elves are carrying a total number of {sum(top_three)} calories')
