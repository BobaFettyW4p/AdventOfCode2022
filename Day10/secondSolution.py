#reads the puzzle input, and returns it as a list with the final character (carriage return) sliced off
def import_data():
    with open('input.txt','r') as f:
        content = f.readlines()
        return [x[:-1] for x in content]

#This function takes the list created in the import_data() function, along with a target # of cycles
#and calculates what the total_signal_strength is at the cycle in question
def signal_interpretation(data, target):
    cycle, total_signal_strength = 1,1
    for instruction in data:
        #if the line begins 'noop', no position change should be processed
        #increment the cycle and continue
        if instruction[0:4] == 'noop' and cycle < target:
            cycle+=1
        #otherwise the line begins 'addx'; this instruction takes a total
        #of 2 cycles to process, and the amount added doesn't take effect until the END of the second cycle
        #first elif trips on a negative number; subtracts from the total signal strength
        elif cycle < target and instruction[5] == '-':
            cycle+=1
            if cycle == target:
                return total_signal_strength
            else:
                cycle+=1
                total_signal_strength-=int(instruction[6:])
        #this elif functions identically to the above one, except it adds to the signal strength as opposed to subtract
        elif cycle < target:
            cycle+=1
            if cycle == target:
                return total_signal_strength
            else:
                cycle+=1
                total_signal_strength+=int(instruction[5:])
    return total_signal_strength

#this function utilizes the signal_interpretation function, and compares the signal value to the current cycle,
#and writes a solid or blank character depending on whether they overlap
def screen_tracing(end_cycle):
    screen = ''
    SCREEN_LENGTH = 40
    output=[]
    for i in range(0,end_cycle):
        #This sprite variable creates an unpacked list that contains all spaces on screen the sprite occupies.
        #If the screen position currently being written is occupied, write a solid character; otherwise, write a blank character
        sprite = [*range(signal_interpretation(data,i+1)-1,signal_interpretation(data,i+1)+2)]
        if len(screen) in sprite:
            screen+='#'
            if len(screen) == SCREEN_LENGTH:
                output.append(screen)
                screen = ''
        else:
            screen+='.'
            if len(screen) == SCREEN_LENGTH:
                output.append(screen)
                screen = ''
    return output
    
#this function utilizes the signal_interpretation function in order to determine the signal strength at specific cycles
#then calculates the answer to part one
def part_one_answer():
    points = [20,60,100,140,180,220]
    score_points = []
    for breakpoint in points:
        score_points.append(signal_interpretation(data, breakpoint))
    #list comprehension that takes every point in score_points, multiplies it by the target cycle, then sums up every value
    return sum([x*y for x,y in zip(points,score_points)])
    


if __name__ == '__main__':
    data = import_data()
    solution = screen_tracing(240)
    for row in solution:
       print(row)
'''
###...##..###..###..#..#..##..###....##.
#..#.#..#.#..#.#..#.#.#..#..#.#..#....#.
#..#.#....#..#.###..##...#..#.#..#....#.
###..#....###..#..#.#.#..####.###.....#.
#....#..#.#....#..#.#.#..#..#.#....#..#.
#.....##..#....###..#..#.#..#.#.....##..

PCPBKAPJ
'''
