
def hops_to(tree, node, tgt):
    if node == tgt:
        return 0
    else:
        for i in tree[node]:
            if in_descendants(tree, i, tgt):
                return 1 + hops_to(tree, i, tgt)

def closest_ancestor(tree, node, tgt1, tgt2):
    for i in tree[node]:
        if in_descendants(tree, i, tgt1) and in_descendants(tree, i, tgt2):
            return closest_ancestor(tree, i, tgt1, tgt2)
    return node

def in_descendants(tree, node, tgt):
    if node == tgt:
        return True
    elif node not in list(tree.keys()):
        return False
    else:
        found = False
        for i in tree[node]:
            found = in_descendants(tree, i, tgt) or found
        return found


def make_tree(arr):
    tree = {}
    for item in arr:
        key, value = item.split(')')
        tree.setdefault(key, []).append(value)
    return tree

def count_orbits(tree, node, length):
    if node not in list(tree.keys()):
        return length
    else:
        res = length
        for branch in tree[node]:
            res += count_orbits(tree, branch, length+1)
        return res




if __name__ == "__main__":
    arr = open('day6.txt').read().strip(' ').split('\n')
    tree = make_tree(arr)
    print(count_orbits(tree, 'COM', 0))
    node = closest_ancestor(tree,'COM', 'YOU', 'SAN')
    print(hops_to(tree, node, 'YOU') + hops_to(tree, node, 'SAN')-2) #Minus 2 bc we count connections and problem deals with moving orbits
