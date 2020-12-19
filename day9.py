def intCodeComputer(opPos, nums):
    position = str(nums[opPos])
    opcode = int(position[-2:])
    param_mode = position[:-2][::-1]
    values = [0,0,0,0,0]
    relative_base = 0
    while opcode != 99:
        if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
            num_params = 2
        elif opcode == 3:
            num_params = 0
        elif opcode == 4 or opcode == 9:
            num_params = 1
        else:
            print("Error in valid opCode")
            return

        print(nums[opPos:opPos+num_params])
        param_mode = param_mode + '0000'
        for i in range(num_params):
            # if i>len(param_mode)-1:
            #     values[i] = nums[nums[opPos+i + 1]]
            if int(param_mode[i]) == 0:
                values[i] = nums[nums[opPos+i+1]]
            elif int(param_mode[i]) == 1:
                values[i] = nums[opPos+i+1]
            elif int(param_mode[i]) == 2:
                values[i] = nums[nums[opPos+i+1]+relative_base]
                #print('here', nums[values[i]])
            else:
                print("Error: Param mode not supported")
                return
        if opcode == 1:
            storePos = values[2]
            nums[storePos] = values[0] + values[1]
            opPos += 4
        elif opcode == 2:
            storePos = values[2]
            nums[storePos] = values[0] * values[1]
            opPos += 4
        elif opcode == 3:
            num = int(input('input: '))
            storePos = values[0]
            nums[storePos] = num
            opPos += 2
        elif opcode == 4:
            opPos +=2
            print(values[0])
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
            storePos = values[2]
            if values[0]<values[1]:
                nums[storePos] = 1
            else:
                nums[storePos] = 0
            opPos += 4
        elif opcode == 8:
            storePos = values[2]
            if values[0] == values[1]:
                nums[storePos] = 1
            else:
                nums[storePos] = 0
            opPos += 4
        elif opcode == 9:
            relative_base+=values[0]
            opPos += 2
        else:
            print("Error invalid opcode")
            return
        pCtr = str(nums[opPos])
        opcode = int(pCtr[-2:])
        param_mode = pCtr[:-2][::-1]
    return 'done'


if __name__ == "__main__":
    arr = open('day9.txt').read().strip(' ').split(',')
    nums = [0]*10000000
    for i in range(len(arr)):
        nums[i] = int(arr[i])
    print(intCodeComputer(0, nums))