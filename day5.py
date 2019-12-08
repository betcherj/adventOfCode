def intCodeComputer(nums):
    opcode = nums[0]
    opPos = 0
    while opcode != 99:
        if opcode == 1:
            pos1 = nums[opPos + 1]
            pos2 = nums[opPos + 2]
            storePos = nums[opPos + 3]
            nums[storePos] = nums[pos1] + nums[pos2]
            opPos += 4
        elif opcode == 2:
            pos1 = nums[opPos + 1]
            pos2 = nums[opPos + 2]
            storePos = nums[opPos + 3]
            nums[storePos] = nums[pos1] * nums[pos2]
            opPos += 4
        elif opcode == 3:
            num = int(input())
            storePos = nums[opPos+1]
            nums[storePos] = num
            opPos += 2
        elif opcode == 4:
            output =
        else:
            print("Error invalid opcode")
            return

        opcode = nums[opPos]
    return nums

if __name__ == "__main__":
