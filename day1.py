import math
def fuel(mass):
    if math.floor(mass/3)-2<=0:
        return 0
    else:
        return fuel(math.floor(mass/3)-2) + math.floor(mass/3)-2

if __name__ == "__main__":
    total_fuel = 0
    string = open('day1.txt').read().split('\n')
    for item in string:
        total_fuel += fuel(int(item))
    print(total_fuel)