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
    divide_into_compartments(rucksacks)
    print(f'The elves have a total priority of {find_common_item(divided_rucksacks)}, that\'s a lot of toys!')



