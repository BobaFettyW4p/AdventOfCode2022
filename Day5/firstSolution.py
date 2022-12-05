from collections import deque
import re

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
                     stack = get_key(position, stackPositions)
                     stacks[stack].append(character)
    return stacks

def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key

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

def processInstructions(stacks,instructions):
    for instruction in instructions:
        iterations, firstStack, finalStack = instruction[0], instruction[1], instruction[2]
        for i in range(0,int(iterations)):
            transferValue = stacks[firstStack].pop()
            stacks[finalStack].append(transferValue)
    finalString = ''
    for key in stacks.keys():
        finalString+=stacks[key].pop()
    return finalString

if __name__ == '__main__':
    stacks = {}
    createStacks(stacks)
    instructions = importInstructions()
    print(f'Our elves are hard at work, the presents on top of the stacks are {processInstructions(stacks,instructions)}') #MQSHJMWNH

