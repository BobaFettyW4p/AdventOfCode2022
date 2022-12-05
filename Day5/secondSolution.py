from collections import deque

#I separated the input into 2 file, one that was the initial stacks, the other that was the instructions
#this finds the indexes of every stack indicator, and returns a dictionary that contains the stack number (as a string)
#as the key, with the index as the value
def createStacks(stacks):
    with open('initialStacks.txt', 'r') as f:
        content = f.readlines()
        stackPositions = {}
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        for item in content[-1]:
            if item in numbers:
                stackPositions[item] = content[-1].index(item)
                stacks[item] = deque()
        for row in content[::-1]:
            for position, character in enumerate(row):
                if position in stackPositions.values() and character != ' ':
                    #the get_key function is defined below; returns dictionary key when provided value
                     stack = get_key(position, stackPositions)
                     stacks[stack].append(character)
    return stacks

#This is a helper function referenced in the createStacks function
#allows us to reference a dictionary value and receive the corresponding key
def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key

#This imports the instructions text file, and processes it so each row is reduced to a list
#containing each of the numbers in the same order they appear: number of iterations, initial stack, final stack
def importInstructions():
    with open('input.txt','r') as f:
        lines = []
        content = f.readlines()
        for instruction in content:
            temp = []
            digitCapture = ''
            instruction = instruction.replace('move', '')
            instruction = instruction.replace('from','')
            instruction = instruction.replace('to','')
            #this loop is needed to capture numbers of 2 digits (or greater)
            #otherwise, 11 would be represented as 2 (1+1)
            for character in instruction:
                if character.isdigit():
                    digitCapture+=f'{character}'
                else:
                    if len(digitCapture) > 0:
                        temp.append(digitCapture)
                        digitCapture=''
                    continue
            lines.append(temp)
    return lines

#this function takes the 2 variables returned from the data ingress functions above
#processes the stacks by utilizing a function scope deque buffer, which is then added 
# to the destination stack in accordance with the instructions
#function returns the value of the top item on each stack as a single continuous string
def processInstructions(stacks,instructions):
    for instruction in instructions:
        iterations, firstStack, finalStack = instruction[0], instruction[1], instruction[2]
        buffer = deque()
        for i in range(0,int(iterations)):
            buffer.appendleft(stacks[firstStack].pop())
        while len(buffer) > 0:
            stacks[finalStack].append(buffer.popleft())
        
    finalString = ''
    for key in stacks.keys():
        finalString+=stacks[key].pop()
    return finalString

if __name__ == '__main__':
    stacks = {}
    stacks = createStacks(stacks)
    instructions = importInstructions()
    print(f'Our elves are hard at work, the presents on top of the stacks are {processInstructions(stacks,instructions)}') #LLWJRBHVZ

