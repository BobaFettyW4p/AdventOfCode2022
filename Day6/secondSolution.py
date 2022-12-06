#imports our data set, returns it as a string
def inputData():
    with open('input.txt','r') as f:
        data = f.read()
    return data

#This actually solves our problem. Iterates over our dataset, and for each character, generates a candidate
#start of message marker. This start of message marker is tested and if it passes, the index of the last item 
#in the candidate is returned
def  interpretSignal(radioSignal):
    for position, character in enumerate(radioSignal):
        #this string is the candidate start of message marker
        string = radioSignal[position:position+14]
        for broadcast in string:
            #if the count is greater than 1, the character appears more than once, and thus the candidate fails
            if string.count(broadcast) != 1:
                break
            #if we have reached the last item in the candidate, it is guaranteed to pass, return the appropriate index
            elif broadcast == string[-1]:
                return position+14  

if __name__ == '__main__':
    radioSignal = inputData()
    print(f'Signal Analysis complete. The start of message marker ends at {interpretSignal(radioSignal)}') #3153
