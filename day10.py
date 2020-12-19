import math

def updateGrid(grid, i, j):
    for p in range(j+1, len(grid[i])):
        if grid[i][p] != '.':
            grid[i][p] += 1
            grid[i][j] += 1
            break
    blockVectors  = []
    for m in range(i+1, len(grid)):
        temp = grid[m].copy()
        for o in range(len(blockVectors)):
            while blockVectors[o][0]<m:
                #update vectors
                blockVectors[o][0] += blockVectors[o][2]
                blockVectors[o][1] += blockVectors[o][3]
            if blockVectors[o][0] == m:
                # mark blocked asteroid
                if blockVectors[o][1] <= len(temp) - 1 and blockVectors[o][1]>=0:
                    temp[blockVectors[o][1]] = '.'
                    #print(blockVectors[0], m, temp, o)
        for n in range(len(grid[m])):
            if temp[n] != '.':
                #need to reduce fractions
                gcd = math.gcd(m-i, n-j)
                blockVectors.append([m, n, int((m-i)/gcd), int((n-j)/gcd)])
                grid[m][n] += 1
                grid[i][j] += 1

    return grid

def findAstroids(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '.':
                grid = updateGrid(grid, i, j)
    return grid

if __name__ == "__main__":
    temp1 = open('day10.txt').read().split('\n')
    grid = []
    for i in temp1:
        temp2 = []
        for j in i:
            if j == '#':
                temp2.append(0)
            else:
                temp2.append(j)
        grid.append(temp2)
    print(grid)
    res = findAstroids(grid)
    most = 0
    for m in grid:
        for n in m:
            if n != '.':
                most = max(most, n)
    print(most)
