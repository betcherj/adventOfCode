import math

def findOre(final_eles, recipies):
    oreCount = 0
    for key in final_eles:
        val = final_eles[key] # required
        ore_produced = recipies[key][1][1]
        multiplier = math.ceil(val/recipies[key][0])
        oreCount += ore_produced*multiplier
    return oreCount

def findIngredients2(recipies):
    requirements = {'FUEL': 1}
    final_eles = {}
    while len(requirements) > 0:
        temp_requirements = {}
        for key in requirements:
            val = requirements[key]
            for item in recipies[key][1:]:
                multiplier = math.ceil(val/recipies[key][0])
                if item[0] == "ORE":
                    if key in list(final_eles.keys()):
                        final_eles[key] = final_eles[key] + val
                    else:
                        final_eles[key] = val
                else:
                    if item[0] in list(temp_requirements.keys()):
                        temp_requirements[item[0]] = temp_requirements[item[0]] + item[1] * multiplier
                    else:
                        temp_requirements[item[0]] = item[1] * multiplier
        requirements = temp_requirements
    return findOre(final_eles, recipies)



def findIngredients(recipies):
    requirements = ['FUEL']
    req_ammounts = {'FUEL' : 1}
    oreCount = 0
    while len(requirements)>0:
        print(requirements, req_ammounts)
        chem_desired = requirements.pop(0)
        ammount_desired= req_ammounts[chem_desired]
        req_ammounts.__delitem__(chem_desired)
        for i in recipies[chem_desired][1:]:
            chem_required = i[0]
            ammount_required = i[1]
            multiplier = ammount_desired
            if chem_required == "ORE":
                chem_produced = recipies[chem_desired][0]
                temp = ammount_required*math.ceil(ammount_desired/chem_produced)
                oreCount += temp
                print(temp, chem_desired, ammount_desired, ammount_required)
            else:
                if chem_required in list(req_ammounts.keys()):
                    req_ammounts[chem_required] = req_ammounts[chem_required] + ammount_required*multiplier
                else:
                    requirements.append(chem_required)
                    req_ammounts[chem_required] = ammount_required*multiplier
    return oreCount



if __name__ == "__main__":
    arr = open('day14.txt').read().split('\n')
    requirements = 'FUEL'
    recipies = {}
    for i in range(len(arr)):
        temp = arr[i].split('=>')
        tkey = temp[1].strip(' ').split(' ')
        key = tkey[1]
        temp2 = temp[0].split(',')
        vals = [int(tkey[0])]
        for j in temp2:
            temp3 = j.strip(' ').split(' ')
            vals.append((temp3[1], int(temp3[0])))
        recipies[key] = vals
    print(recipies)
    print(findIngredients2(recipies))
