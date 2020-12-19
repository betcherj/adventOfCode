import string
printable = string.printable
possibleKeys = printable[10:36]
possibleDoors = printable[36:62]
# 1) get keys available from current state,
# 2) add possible key locations to list of states
# 3) repeat

def getAvailbleKeys( grid, visited, pos, steps):
    keys = []
    visited[pos[0]][pos[1]] = 1
    steps +=1
    val = grid[pos[0]][pos[1]]
    if val == '.' or val == '@':
        pass
    elif val in possibleDoors:
        if val.lower() in keys:
            grid[pos[0]][pos[1]] = '.'
        else:
            return keys
    else:
        #val is a key
        keys.append(val)
        keys.append(pos)
        keys.append(steps)
        grid[pos[0]][pos[1]] = '.'
        return keys

    right = grid[pos[0]][pos[1]+1]
    left = grid[pos[0]][pos[1]-1]
    down = grid[pos[0]+1][pos[1]]
    up = grid[pos[0]-1][pos[1]]
    if right != '#' and not visited[pos[0]][pos[1]+1]:
        keys.extend(getAvailbleKeys( grid.copy(), visited.copy(), [pos[0],pos[1]+1], steps))
    if left != '#' and not visited[pos[0]][pos[1]-1]:
        keys.extend(getAvailbleKeys( grid.copy(), visited.copy(), [pos[0],pos[1]-1], steps))
    if down != '#' and not visited[pos[0]+1][pos[1]]:
        keys.extend(getAvailbleKeys( grid.copy(), visited.copy(), [pos[0]+1,pos[1]], steps))
    if up != '#' and not visited[pos[0]-1][pos[1]]:
        keys.extend(getAvailbleKeys(grid.copy(), visited.copy(), [pos[0]-1,pos[1]], steps))
    return keys

def navigateMaze(grid, visited, start):
    keys = getAvailbleKeys(grid.copy(), visited.copy(), start, -1)
    
    return keys

if __name__ == "__main__":
    printable = string.printable

    temp1 = open('day18.txt').read().split('\n')
    grid = []
    start = None
    visited = []
    for i in range(len(temp1)):
        temp2 = []
        temp3 = []
        for j in range(len(temp1[i])):
            if temp1[i][j] == '@':
                start = [i, j]
            temp3.append(0)
            temp2.append(temp1[i][j])
        visited.append(temp3)
        grid.append(temp2)
    print(grid)
    print(navigateMaze(grid, visited, start))