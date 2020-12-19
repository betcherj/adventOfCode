import math

def findOre(final_eles, recipies):
    oreCount = 0
    for key in final_eles:
        val = final_eles[key] # required
        ore_produced = recipies[key][1][1]
        multiplier = math.ceil(val/recipies[key][0])
        oreCount += ore_produced*multiplier
    return oreCount

def findIngredients4(next_req, recipies, requirements, materials):

    if not next_req:
        return findOre(requirements, recipies)

    substrates = recipies[next_req[0]][1:]

    ammount_produced = recipies[next_req[0]][0]

    #Bc pythons lists are stupid
    t_substrates = []
    t_ammount_produced = ammount_produced
    for j in range(len(substrates)):
        t_substrates.append(substrates[j][1])
    while ammount_produced < next_req[1]:
        ammount_produced += t_ammount_produced
        for i in range(len(substrates)):
            substrates[i][1] += t_substrates[i]

    for item in substrates:
        if item[0] in list(materials.keys()) and item[1] <= materials[item[0]]:
            materials[item[0]] = materials[item[0]] - item[1]
            if materials[item[0]] == 0:
                del materials[item[0]]
        else:
            if ammount_produced > next_req[1]:
                if item[0] in list(materials.keys()):
                    materials[item[0]] = materials[item[0]] + item[1]-next_req[1]
                else:
                    materials[item[0]] = item[1]-next_req[1]
            if item[0] in list(requirements.keys()):
                requirements[item[0]] = requirements[item[0]] + item[1]
            else:
                requirements[item[0]] = item[1]

    return req_Fuel






def findIngredients3(recipies, requirements, materials):
    if len(requirements) == 1 and "ORE" in list(requirements.keys()):
        return requirements["ORE"]
    else:
        new_reqs = {}
        new_materials = {}
        print(requirements, materials)
        for key, val in requirements.items():
            if key == "ORE":
                continue
            if key in list(materials.keys()):
                if val<=materials[key]:
                    materials[key] = materials[key] - val
                    if materials[key] == 0:
                        del materials[key]
            substrates = recipies[key][1:]
            ammount_produced = recipies[key][0]
            if ammount_produced<val:
                ammount_produced = ammount_produced*2
                for i in range(len(substrates)):
                    substrates[i][1] = substrates[i][1] * 2
            if ammount_produced>val:
                if key in list(materials.keys()):
                    materials[key] = materials[key] + ammount_produced-val
                else:
                    materials[key] = ammount_produced-val
            for item in substrates:
                if item[0] in list(new_reqs.keys()):
                    new_reqs[item[0]] = new_reqs[item[0]] + item[1]
                else:
                    new_reqs[item[0]] = item[1]
        return findIngredients3(recipies, new_reqs, new_materials)


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
            vals.append([temp3[1], int(temp3[0])])
        recipies[key] = vals
    print(recipies)
    final_eles = findIngredients4(['FUEL',1], recipies, {}, {})
    print(final_eles)
