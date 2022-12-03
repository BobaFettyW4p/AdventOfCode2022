import string

#This block creates a dictionary 'PRIORITY' populated with the lowercase
#and uppercase letters as the keys, with the corresponding numerical
#PRIORITY as the value
PRIORITY = {}
letters = enumerate(string.ascii_letters)
#the dictionary comprehension in line 10 creates the appropriate relationship between each letter and the appropriate number, but they are reversed
#The PRIORITY dictionary is the enum dictionary, but with the keys and values swapped
enum = dict((i+1,j) for i,j in letters)
PRIORITY = dict(zip(enum.values(),enum.keys()))

#imports dataset from the file, adds each line to the rucksacks list
def import_rucksack_contents():
    with open('input.txt', 'r') as f:
        contents = f.readlines()
        for rucksack in contents:
            rucksack = rucksack[slice(-1)]
            rucksacks.append(rucksack)
        return rucksacks

#divides each item from the rucksacks list into a list of 2 equal lengths
def divide_into_compartments(rucksacks):
    for rucksack in rucksacks:
        middle = len(rucksack) // 2
        divided_rucksacks.append([rucksack[:middle],rucksack[middle:]])
    return divided_rucksacks

#this function populates the safety_groups list as a 2D list, each containing
#3 items from the rucksacks list
def create_safety_groups(rucksacks, safety_groups):
    group_of_three = []
    for elf in rucksacks:
        group_of_three.append(elf)
        if len(group_of_three) == 3:
            safety_groups.append(group_of_three)
            group_of_three = []
            continue
        else:
            continue
    return safety_groups

#this function accepts the 2D safety_groups list, finds the common item among them (signifying the safety badge)
#then adds up the associated priorities to yield the answer for part 2 
def find_safety_group_badges(safety_groups):
    badges = []
    total_badge_priority = 0
    for group in safety_groups:
        #this list comprehension finds the "badge" (common item in all 3 lists)
        #the badge can appear multiple times, so we only want to add the first instance to the list
        badge = [x for x in group[0] if x in group[1] and x in group[2]]
        badges.append(badge[0])
    for badge_value in badges:
        total_badge_priority += PRIORITY[badge_value]
    return total_badge_priority

#This function yielded the solution to part 1; took the 2D list containing both halves of each rucksack
#found the common item between them, then added up the corresponding priority of this item
def find_common_item(divided_rucksacks):
    solution = 0
    for rucksack in divided_rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1]:
                solution += PRIORITY[item]
                break;
            else:
                continue
    return solution

if __name__ == '__main__':
    rucksacks = []
    divided_rucksacks = []
    safety_groups = []
    import_rucksack_contents()
    #divide_into_compartments(rucksacks)
    #print(f'The elves have a total priority of {find_common_item(divided_rucksacks)}, that\'s a lot of toys!')
    create_safety_groups(rucksacks, safety_groups)
    if len(rucksacks)/3 == len(safety_groups):
        print(f'every elf has their buddies, feel free to proceed')
        print(f'Since everyone is safe, the total value of their badges is {find_safety_group_badges(safety_groups)}')
    else:
        print(f'something\'s not right, double check your safety groups to prevent danger!')
