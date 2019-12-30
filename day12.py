def findPreviousState(moons):
    pastStates = {}
    steps = 0
    while True:
        length = len(pastStates)
        item = ''
        pos = moons[0].copy()
        pos.append(moons[1].copy())
        for i in pos:
            for j in i:
                item += str(j) + '*'
        pastStates[item] = 'here'
        if len(pastStates) == length:
            return steps
        if steps == 4686774924:
            print('missed it')
        elif steps == 4686774924/2:
            print('halfway')
        elif steps == 4686774924/10:
            print('one tenth of the way')
        moons = findVelocities(moons)
        moons = findPositions(moons)
        steps +=1
    return -1


def findPositions(moons):
    positions = moons[0].copy()
    velocities = moons[1].copy()
    for i in range(len(positions)):
        for j in range(3):
            positions[i][j] += velocities[i][j]
    return [positions, velocities]

def findVelocities(moons):
    positions = moons[0].copy()
    velocities = moons[1].copy()
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            for p in range(3): #One of each vector
                if positions[i][p] > positions[j][p]:
                    velocities[i][p] -= 1
                    velocities[j][p] +=1
                elif positions[i][p] < positions[j][p]:
                    velocities[i][p] += 1
                    velocities[j][p] -= 1
    return [positions, velocities]

def stateEnergy(moons):
    positions = moons[0].copy()
    velocities = moons[1].copy()
    stat_energy = 0
    for i in range(len(positions)):
        pot = 0
        kin = 0
        for j in range(3):
            pot += abs(positions[i][j])
            kin += abs(velocities[i][j])
        stat_energy +=  (pot* kin)
    return stat_energy

def stepThrough(moons, steps):
    for i in range(steps):
        #print("At Step " , i, " : " + str(moons))
        moons = findVelocities(moons)
        moons = findPositions(moons)
    print(moons)
    return stateEnergy(moons)


if __name__ == "__main__":
    arr = open('day12.txt').read().strip(' ').split('\n')
    moons = ([], [])
    for i in arr:
        temp = []
        for j in i.split(','):
            temp.append(int(j))
        moons[0].append(temp)
        moons[1].append([0,0,0])
    print(moons)
    print(findPreviousState(moons))
    #print(stepThrough(moons, 4686774924))

