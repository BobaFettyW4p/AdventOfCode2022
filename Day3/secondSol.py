import string

#This block creates a dictionary 'PRIORITY' populated with the lowercase
#and uppercase letters as the keys, with the corresponding numerical
#PRIORITY as the value
PRIORITY = {}
letters = enumerate(string.ascii_letters)
enum = dict((i+1,j) for i,j in letters)
PRIORITY = dict(zip(enum.values(),enum.keys()))
#variable initialization, used later
rucksacks = []
divided_rucksacks = []
safety_groups = []

def import_rucksack_contents():
    with open('input.txt', 'r') as f:
        contents = f.readlines()
        for rucksack in contents:
            rucksack = rucksack[slice(-1)]
            rucksacks.append(rucksack)
        return rucksacks

def divide_into_compartments(rucksacks):
    for rucksack in rucksacks:
        middle = len(rucksack) // 2
        divided_rucksacks.append([rucksack[:middle],rucksack[middle:]])
    return divided_rucksacks

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

def find_safety_group_badges(safety_groups):
    badges = []
    total_badge_priority = 0
    for group in safety_groups:
        badge = [x for x in group[0] if x in group[1] and x in group[2]]
        badges.append(badge[0])
    for badge_value in badges:
        total_badge_priority += PRIORITY[badge_value]
    return total_badge_priority

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
    import_rucksack_contents()
    #divide_into_compartments(rucksacks)
    #print(f'The elves have a total priority of {find_common_item(divided_rucksacks)}, that\'s a lot of toys!')
    print(create_safety_groups(rucksacks,safety_groups))
    if len(rucksacks)/3 == len(safety_groups):
        print(f'every elf has their buddies, feel free to proceed')
    else:
        print(f'something\'s not right, double check your safety groups to prevent danger!')
    print(f'Since everyone is safe, the total value of their badges is {find_safety_group_badges(safety_groups)}')
