# AOC2023 - day03

from numpy import clip

# read file
with open('day03/day03_input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    Ny, Nx = len(lines),  len(lines[0])   

def checkSymbol(x0,y0):
    # check if point (x0,y0) is adjacent to symbol     
    shifts = ((0,0),(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    for shift in shifts:
        y,x = clip(y0+shift[1],0, Ny-1), clip(x0+shift[0],0, Nx-1)
        c = lines[y][x]        
        if c!='.' and not c.isdigit():
            return True
    return False

# extract valid numbers and positions
valid_nums = []
for y,line in enumerate(lines):    
    num_str, sym_check = '', False #reset state
    sym_check = False
    for x, c in enumerate(line):
        if c.isdigit():
            sym_check = sym_check or checkSymbol(x,y)
            num_str = num_str + c
        if num_str and (not c.isdigit() or x==Nx-1):    
            # complete number found            
            if sym_check:
                valid_nums.append(int(num_str))
            num_str, sym_check = '', False #reset state            

print("part1: ", sum(valid_nums))
        
                
        


            
            
            


