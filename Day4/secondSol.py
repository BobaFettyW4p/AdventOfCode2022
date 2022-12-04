def import_data(pairs):
    with open('SEDifiedInput.txt', 'r') as f:
        content = f.readlines()
        pairs = [x[:-1] for x in content]
        return pairs

def find_subsets(pairs):
    subsets = [x.split() for x in pairs]
    contained, notContained = [], []
    for pair in subsets:
        pair = [int(x) for x in pair]
        if (pair[0] <= pair[2] <= pair[1]) or (pair[0] <= pair[3] <= pair[1]):
            print(f'{pair} tripped the first conditional.')
            contained.append(pair)
        elif (pair[2] <= pair[0] <= pair[3]) or (pair[2] <= pair[1] <= pair[3]):
            print(f'{pair} tripped the second conditional')
            contained.append(pair)
        else:
            print(f'{pair} tripped the third conditional')
            notContained.append(pair)
    return len(contained)
            
def test(list):
    if list[0] <= list[2] and list[1] >= list[3]:
        print('first conditional tripped')
    elif list[0] >= list[2] and list[1] <= list[3]:
        print('second conditional tripped')
    else:
        print('third conditional tripped')

if __name__ == '__main__':
    pairs =[]
    pairs = import_data(pairs)
    print(find_subsets(pairs))
    #prifind_subsets(pairs)
    #print(test([4,4,3,34]))
