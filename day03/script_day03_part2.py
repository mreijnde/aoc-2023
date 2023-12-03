# AOC2023 - day03

# read file
with open('day03/day03_input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# find positions of symbols
syms_pos = [(x,y) for (y,line) in enumerate(lines) for (x,c) in enumerate(line) if not (c.isdigit() or c=='.') ]

# extract all numbers and used positions
nums, nums_pos = [], []
for y,line in enumerate(lines):    
    num_str, pos = '', [] # reset state
    for x, c in enumerate(line):
        if c.isdigit():           
            num_str = num_str + c
            pos.append((x,y))
        if num_str and (not c.isdigit() or x==len(line)-1):    
            # complete number found                        
            nums.append(int(num_str))
            nums_pos.append(pos)
            num_str, pos = '', [] # reset state
            
# calculate extended number position including neighborhood
shifts = ((0,0),(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
nums_pos_ext = [[(x+x_shift,y+y_shift) for (x,y) in number_pos for (x_shift,y_shift) in shifts] for number_pos in nums_pos]

# part 1
nums_valid = [nums[i] for (i,num_pos_ext) in enumerate(nums_pos_ext) if set(num_pos_ext) & set(syms_pos)]
print("part1: ", sum(nums_valid))

# part 2
syms_nums = [ [nums[i] for (i,num_pos_ext) in enumerate(nums_pos_ext) if sym_pos in set(num_pos_ext) ] for sym_pos in syms_pos ]
gear_ratios = [nums[0]*nums[1] for nums in syms_nums if len(nums)==2]
print("part2: ", sum(gear_ratios))

