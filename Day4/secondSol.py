#imports from the file modified appropriately with SED and generates the dataset to work with
def import_data(pairs):
    with open('SEDifiedInput.txt', 'r') as f:
        content = f.readlines()
        pairs = [x[:-1] for x in content]
        return pairs

#This function iterates over our sets and looks for overlaps
def find_subsets(pairs):
    #list comprehension to convert our dataset into a 2D list
    subsets = [x.split() for x in pairs]
    #for better memory efficiency, we could initialize an integer instead of a list, then increment it when we find a match, then return the contained int
    #as opposed to the length of a list
    contained, notContained = [], []
    for pair in subsets:
        #this converts each item from a string of a number into an integer for proper comparison
        pair = [int(x) for x in pair]
        #these if statements check if both values in the first range are either greater or less than both values in the second range
        #if they are, there is no overlap; otherwise, there is
        #this could probably be done also via unpackign the ranges and make comparisons between two separate lists as well
        if (pair[0] <= pair[2] <= pair[1]) or (pair[0] <= pair[3] <= pair[1]):
            print(f'{pair} tripped the first conditional.')
            contained.append(pair)
        elif (pair[2] <= pair[0] <= pair[3]) or (pair[2] <= pair[1] <= pair[3]):
            print(f'{pair} tripped the second conditional')
            contained.append(pair)
        #if the numbers in the first list are not both larger or smaller than both numbers in the second list, they are not overlapping at all
        #this variable isn't necessary per se, but was a handy troubleshooting tool (if contained +notContained did not equal the total number of lines in the file, something was wrong)
        #could be removed for increased memory efficiency
        else:
            print(f'{pair} tripped the third conditional')
            notContained.append(pair)
    return len(contained)
            
if __name__ == '__main__':
    pairs =[]
    pairs = import_data(pairs)
    print(find_subsets(pairs)) # 837
    #prifind_subsets(pairs)
    #print(test([4,4,3,34]))
