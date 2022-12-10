def import_data():
    with open('input.txt','r') as f:
        content = f.readlines()
        return [x[:-1] for x in content]

def signal_interpretation(data, target):
    cycle = 1
    total_signal_strength = 1
    for instruction in data:
        print(f'processing {instruction}')
        if instruction[0:4] == 'noop' and cycle < target:
            print(f'incrementing cycle from {cycle} to {cycle+1}')
            cycle+=1
        elif cycle < target and instruction[5] == '-':
            print(f'incrementing cycle from {cycle} to {cycle+1}')
            cycle+=1
            if cycle == target:
                print(f'target cycle reached, returning {total_signal_strength}')
                return total_signal_strength
            else:
                cycle+=1
                total_signal_strength-=int(instruction[6:])
                print(f'incrementing signal strength to {total_signal_strength} after cycle {cycle}')
        elif cycle < target:
            print(f'incrementing cycle from {cycle} to {cycle+1}')
            cycle+=1
            if cycle == target:
                print(f'target cycle reached, returning {total_signal_strength}')
                return total_signal_strength
            else:
                cycle+=1
                total_signal_strength+=int(instruction[5:])
                print(f'incrementing signal strength to {total_signal_strength} after cycle {cycle}')
    return total_signal_strength


def part_one_answer():
    points = [20,60,100,140,180,220]
    score_points = []
    for breakpoint in points:
        print(f'adding signal_interpretation(data,breakpoint) to points')
        score_points.append(signal_interpretation(data, breakpoint))
    return sum([x*y for x,y in zip(points,score_points)])
    


if __name__ == '__main__':
    data = import_data()
    print(part_one_answer()) #14320
    #signal_interpretation(data, 5)

