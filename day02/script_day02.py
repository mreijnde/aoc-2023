# AOC2023 - day02

def score_part1(line):
    max_count = {'red': 12, 'green': 13, 'blue':14}
    gamenr = int(line.split(':')[0].split(' ')[1])
    for group in line.split(':')[1].strip(' \n').split(';'):
        for valuekeyelem in group.split(','):
            elem = valuekeyelem.strip().split(' ')
            value,key = int(elem[0]), elem[1]
            if value > max_count[key]:
                return 0
    return gamenr


def score_part2(line):
    count = {'red': 0, 'green': 0, 'blue':0}
    gamenr = int(line.split(':')[0].split(' ')[1])
    for group in line.split(':')[1].strip(' \n').split(';'):
        for valuekeyelem in group.split(','):
            elem = valuekeyelem.strip().split(' ')
            value,key = int(elem[0]), elem[1]
            if value > count[key]:
                count[key] = value    
    return count['red'] * count['green'] * count['blue']



# read file
with open('day02/day02_input.txt') as f:
    lines = f.readlines()


# calc
score_part1 = sum(map(score_part1, lines))
print("part1: ", score_part1)

score_part2 = sum(map(score_part2, lines))
print("part2: ", score_part2)


