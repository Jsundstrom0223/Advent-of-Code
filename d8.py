import numpy as np
input = "sample8.txt"
dinput = "d8.txt"

def make_arr(grid):
    array_list = []

    for line in grid:
        chars_in_line = [c for c in line]
        line_array = np.array(chars_in_line)
        array_list.append(line_array)
        tree_array = np.vstack(array_list)
 
    return tree_array

def check_against_right(tree_array, x, y, val, end):
    right_add = 0
    right_scenic = 0
    
    for _ in range(end - y):
        if y == end:
            break

        if tree_array[x, y+1] < val:
            y += 1
            right_add = 1
            right_scenic += 1
        else:
            right_add = 0
            right_scenic += 1
            break
        
    return right_add, right_scenic

def check_against_left(tree_array, x, y, val):
    left_add = 0
    left_scenic = 0
    for _ in range(y):
        if y == 0:
            break

        if tree_array[x, y-1] < val:
            y -= 1
            left_add = 1
            left_scenic += 1
        else:
            left_add = 0
            left_scenic += 1
            break
       
    return left_add, left_scenic

def check_against_top(tree_array, x, y, val):
    top_add = 0
    top_scenic = 0
    for _ in range(x):
        if x == 0:
            break
        
        if tree_array[x-1, y] < val:
            x -= 1
            top_add = 1
            top_scenic += 1
        else:
            top_add = 0
            top_scenic += 1
            break
                
    return top_add, top_scenic

def check_against_bottom(tree_array, x, y, val, end):
    bottom_add = 0
    bottom_scenic = 0
    for _ in range(end - 1):
        if x == end:
            break

        if tree_array[x+1, y] < val:
            x += 1
            bottom_add = 1
            bottom_scenic += 1
        else:
            bottom_add = 0
            bottom_scenic += 1
            break  

    return bottom_add, bottom_scenic

def check_interior(tree_array, total, end):
 
    best = 0
    for ind, val in np.ndenumerate(tree_array):
        check_visibility = True
        x = ind[0]
        y = ind[1]
        if x >= 1 and y < end and y > 0:
            
            bottom_add, bottom_scenic = check_against_bottom(tree_array, x, y, val, end)
            if bottom_add != 0:
                total += bottom_add
                check_visibility = False
               
            top_add, top_scenic = check_against_top(tree_array, x, y, val)
            if top_add != 0:
                if check_visibility:
                    total += top_add
                    check_visibility = False
            
            left_add, left_scenic = check_against_left(tree_array, x, y, val)
            if left_add != 0:
                if check_visibility:
                    total += left_add
                    check_visibility = False
               
            right_add, right_scenic = check_against_right(tree_array, x, y, val, end)
            if right_add != 0:
                if check_visibility:
                    total += right_add
            
            score = (top_scenic * bottom_scenic * left_scenic * right_scenic) 
            if score > best:
                best = score       
           
        if x == end:
            break

    return total, best

def main():
    with open(dinput, "r") as input_file:
        line_list = input_file.readlines()

    grid = [l.strip() for l in line_list]
    len_per_side = len(grid)
    end = len_per_side -1
    total = (len_per_side - 1) * 2 + (len(grid[0]) - 1)* 2

    tree_array = make_arr(grid)
    total, best = check_interior(tree_array, total, end)
    print(f"The number of visible trees is {total}.")
    print(f"The best scenic score is {best}")

if __name__ == '__main__':
    main()