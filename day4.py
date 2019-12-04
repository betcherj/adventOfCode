input = ['124075','580769']


def inceasing2(num):
    found = False
    dCount = 0
    for i in range(1,len(num)):
        if int(num[i-1]) > int(num[i]):
            return False
        elif int(num[i-1]) == int(num[i]):
            dCount +=1
        else:
            if dCount == 1:
                found = True
            else:
                dCount = 0
    if not found and dCount != 1:
        return False
    return True

def combos2(input):
    ctr = 0
    for j in range(int(input[0]), int(input[1])):
        if inceasing2(str(j)):
            ctr += 1
    return ctr

def inceasing(num):
    temp = set()
    temp.add(num[0])
    for i in range(1,len(num)):
        temp.add(num[i])
        if int(num[i-1]) >int(num[i]):
            return False
    if len(temp) >= len(num):
        return False
    return True


def combos(input):
    ctr = 0
    for j in range(int(input[0]), int(input[1])):
        if inceasing(str(j)):
            ctr += 1
    return ctr



if __name__ == "__main__":
    #part1
    print(combos(input))
    #part2
    print(combos2(input))
