def inputData():
    with open('input.txt','r') as f:
        data = f.read()
    return data

def  interpretSignal(radioSignal):
    for position, character in enumerate(radioSignal):
        string = radioSignal[position:position+4]
        print(f'testing {string}')
        for broadcast in string:
            if string.count(broadcast) != 1:
                print(f'count of {broadcast} is {string.count(broadcast)}. Moving on.')
                break
            elif broadcast == string[-1]:
                return position+4  

if __name__ == '__main__':
    radioSignal = inputData()
    print(f'Signal Analysis complete. First stack of packet marker is at {interpretSignal(radioSignal)}') # 1542
