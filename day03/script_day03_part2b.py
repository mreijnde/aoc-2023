# AOC2023 - day03
# combined with part1 approach to search locally around numbers in grid to speedup

from numpy import clip
from collections import defaultdict

# read file
with open('day03/day03_input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    Ny, Nx = len(lines),  len(lines[0])   

syms_numids = defaultdict(list) # keep track of numbers adjacent to symbols

def checkSymbol(x0,y0, numid):
    # check if point (x0,y0) is adjacent to symbol + keep track of numid near symbols
    shifts = ((0,0),(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    for shift in shifts:
        y,x = clip(y0+shift[1],0, Ny-1), clip(x0+shift[0],0, Nx-1)
        c = lines[y][x]
        if c!='.' and not c.isdigit():
            syms_numids[(x,y)].append(numid)            
            return True
    return False

# extract valid numbers and positions + keep track of symbol use count
nums, nums_pos = [], []
for y,line in enumerate(lines):    
    num_str, num_pos, sym_check = '', [], False # reset state
    for x, c in enumerate(line):
        if c.isdigit():
            sym_check = sym_check or checkSymbol(x,y, len(nums))          
            num_str = num_str + c
            num_pos.append((x,y))
        if num_str and (not c.isdigit() or x==len(line)-1):    
            # complete number found
            if sym_check:                        
                nums.append(int(num_str))
                nums_pos.append(num_pos)
            num_str, num_pos, sym_check = '', [], False # reset state


print("part1: ", sum(nums))
                       
gears_numids = [ sym_numids for sym_numids in syms_numids.values() if len(sym_numids)==2] 
gears_values = [ nums[ids[0]]*nums[ids[1]] for ids in gears_numids  ]
print("part2: ", sum(gears_values))



            
            
            


