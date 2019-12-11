def intCodeComputer(nums):
    start = str(nums[0])
    opcode = int(start[-2:])
    param_mode = start[:-2][::-1]
    opPos = 0
    values = [0,0,0,0,0]
    while opcode != 99:
        if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
            num_params = 2
        elif opcode == 3:
            num_params = 0
        elif opcode == 4:
            num_params = 1
        else:
            print("Error in valid opCode")
            return
        for i in range(num_params):
            if i>len(param_mode)-1:
                values[i] = nums[nums[opPos + i + 1]]
            elif int(param_mode[i]) == 0:
                values[i] = nums[nums[opPos+i+1]]
            else:
                values[i] = nums[opPos+i+1]
        if opcode == 1:
            storePos = nums[opPos + 3]
            nums[storePos] = values[0] + values[1]
            opPos += 4
        elif opcode == 2:
            storePos = nums[opPos + 3]
            nums[storePos] = values[0] * values[1]
            opPos += 4
        elif opcode == 3:
            num = int(input("input: "))
            storePos = nums[opPos+1]
            nums[storePos] = num
            opPos += 2
        elif opcode == 4:
            print(values[0])
            opPos += 2
        elif opcode == 5:
            if values[0] != 0:
                opPos = values[1]
            else:
                opPos += 3
        elif opcode == 6:
            if values[0] == 0:
                opPos = values[1]
            else:
                opPos += 3
        elif opcode == 7:
            storePos = nums[opPos + 3]
            if values[0]<values[1]:
                nums[storePos] = 1
            else:
                nums[storePos] = 0
            opPos += 4
        elif opcode == 8:
            storePos = nums[opPos + 3]
            if values[0] == values[1]:
                nums[storePos] = 1
            else:
                nums[storePos] = 0
            opPos += 4
        else:
            print(opPos)
            print("Error invalid opcode")
            return
        pCtr = str(nums[opPos])
        opcode = int(pCtr[-2:])
        param_mode = pCtr[:-2][::-1]
    return nums

if __name__ == "__main__":
    arr = open('day5.txt').read().strip(' ').split(',')
    nums = []
    for i in arr:
        nums.append(int(i))
    intCodeComputer(nums)