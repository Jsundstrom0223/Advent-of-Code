import itertools
from anytree import Node, PreOrderIter, find

challenge_input = "d7.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()

terminal_output = [i.strip() for i in line_list]

outer = Node("outer", short="/", parent=None, total=0, type="dir")

def make_new_target_node(split_val, target):
    
    new_target = split_val[2]
    new_target = Node(new_target, short= new_target, parent=target, total=0, type="dir")
    return new_target

def find_target(terminal_output, target=None, start=None):
    cd_counter = 0
    if start is None:
        start = 0

    for val in (terminal_output[start: ]):
        split_val = val.split(" ")
        if split_val[0] == "$" and split_val[1] == "cd":
            cd_counter += 1
            
            if cd_counter == 1:
                if split_val[2] == "/":
                    new_target = outer
                else:
                    existing_node = find(outer, filter_= lambda node: node.short == split_val[2] and node.parent == target)
                    if existing_node is not None:
                        new_target = existing_node
                    ###not necessary for challenge input, but was necessary for one set of test input
                    else:  
                        new_target = make_new_target_node(split_val, target)
            else:  
                break
   
    return new_target

def slicer(terminal_output, start=None):
    up_a_level = []
    ls_counter = 0
    here = terminal_output[start: ]
  
    for idx, val in enumerate(here):
        split_val = val.split(" ")
        if split_val[1] == "ls":
            ls_counter += 1
            if ls_counter == 1:
                start = idx + 1
            if ls_counter == 2:
                end = idx - 1
                break

        if val == "$ cd ..":
            up_a_level.append(idx)
            for v in reversed(here[: idx]):
                if v!= "$ cd ..":
                    end = idx - (len(up_a_level) - 1)
                    break
                
        if val == terminal_output[-1]:
            end = idx + 1

    sliced = list(itertools.islice(here, start, end))

    return sliced, end, here, up_a_level

def make_new_child_nodes(new_target, sliced):
    for item in sliced:
        sitem = item.split(" ")
        if item == "$ cd ..":
            break

        if sitem[0].isnumeric():
            short_name = sitem[0]
            total = int(sitem[0])
            type = "file"
        else:
            short_name = sitem[1]
            total =0
            type = "dir"
         
        item = Node(item, short=short_name, parent=new_target, total=total, type=type)

def parse_remaining(here, new_target, end, up_a_level):
    new_target = find_target(here, target=new_target, start=end)
    sliced, end, here, up_a_level = slicer(here, start=end)
    make_new_child_nodes(new_target, sliced)
   
    if len(up_a_level) > 0:
        for _ in up_a_level:
            new_target = new_target.parent

    return here, new_target, end, up_a_level

def starter(): 
    new_target = find_target(terminal_output, target=outer)
    sliced, end, here, up_a_level = slicer(terminal_output)
    make_new_child_nodes(new_target, sliced)
    
    count = 0
    for i in terminal_output:
        split_i = i.split(" ")
        if split_i[1] == "ls":
            count += 1

    for _ in range(count - 1):
        here, new_target, end, up_a_level = parse_remaining(here, new_target, end, up_a_level)

def totaler(n):
    for node in n.children:
        if node.type == "dir":
            children = [c for c in node.children]
            for i in children:
                totaler(i)
            total = [c.total for c in node.children]
            node.total = sum(total)
            node.parent.total += node.total 
        else:
            node.parent.total += node.total

    dir_sum = sum([item.total for item in PreOrderIter(outer) if item.type == "dir" and item.total < 100000])
    
    return dir_sum

def dir_to_delete(available_space, free_space_req):
    free_up = free_space_req - (available_space - outer.total)

    dir_to_delete_size = min([item.total for item in PreOrderIter(outer) if item.type == "dir" and item.total > free_up])

    return dir_to_delete_size

starter()
dir_sum = totaler(outer)
dir_to_delete_size = dir_to_delete(70000000, 30000000)

print(f"Sum of directories smaller than 100000 is {dir_sum}")
print(f"Size of directory to delete is {dir_to_delete_size}")