challenge_input = "2021_practice_input.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()

depth_list = [int(depth) for depth in line_list]

###Part 1
def depth_checker(depth_list):
    
    depth_increase = 0
    old_depth = depth_list[0]
    for value in depth_list[1: ]:
        
        if value > old_depth:  
            depth_increase += 1
        old_depth = value

    print(depth_increase)

###Part 2
sum_list = []
def depth_window_checker(depth_list):
    
    for index, value in enumerate(depth_list[ : -2]):    
        window_sum = sum([value, depth_list[index + 1], depth_list[index + 2]])
        sum_list.append(window_sum)

    depth_checker(sum_list)

depth_checker(depth_list)
depth_window_checker(depth_list)

