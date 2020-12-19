import math
from itertools import permutations

def findCombo_feedback(nums, phase_settings, thrusters):
    maxThrust = -1
    perms = list(permutations(phase_settings))
    for i in perms:
        opPos = [0]*thrusters
        out = 0

        tamps = []
        for p in range(thrusters):
            tamps.append(nums[:])
        opCode = '-1'
        tphase_settings = list(i)
        while out != None:
            for j in range(thrusters):
                if tphase_settings:
                    phase_setting = tphase_settings.pop(0)
                    out, opPos[j], opCode = intCodeComputer(opPos[j], tamps[j], out, phase_setting)
                else:
                    out, opPos[j], opCode = intCodeComputer(opPos[j], tamps[j], out, None)
            if out != None:
                res = out
        if res>maxThrust:
            maxThrust = res

    return maxThrust

def findCombo(nums, phase_settings, instruction, thrusters):
    maxThrust = -1
    out = -1
    perms = list(permutations(phase_settings))
    print(perms)
    for i in perms:
        for j in range(thrusters):
            tnums = nums
            if j == 0:
                out = intCodeComputer(0, tnums, instruction, i[0])
            else:
                out = intCodeComputer(0, tnums, out, i[j])
        if out>maxThrust:
            maxThrust = out
    return maxThrust

def intCodeComputer(opPos, nums, instruction, phase_setting):
    start = str(nums[opPos])
    opcode = int(start[-2:])
    param_mode = start[:-2][::-1]
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
            if phase_setting:
                num = phase_setting
                phase_setting = None
            else:
                num = instruction
            storePos = nums[opPos+1]
            nums[storePos] = num
            opPos += 2
        elif opcode == 4:
            opPos +=2
            return values[0], opPos, str(nums[opPos])[-2:]
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
            print("Error invalid opcode")
            return
        pCtr = str(nums[opPos])
        opcode = int(pCtr[-2:])
        param_mode = pCtr[:-2][::-1]
    return None, '99', '99'

if __name__ == "__main__":
    arr = open('day7.txt').read().strip(' ').split(',')
    nums = []
    for i in arr:
        nums.append(int(i))
    phase_settings = [5,6,7,8,9]
    print(findCombo_feedback(nums, phase_settings, len(phase_settings)))