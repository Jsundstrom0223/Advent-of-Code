from collections import defaultdict
import copy
import re

challenge_input = "d5.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()

def make_crate_dict(line_list):
    instructions = []
    index_character_tuples = []
    d = defaultdict(list)

    for i in line_list:
        if i.startswith("move"):
            instructions.append(i.strip())
        else:
            ###loop through lines, creating a tuple of (index, character) for each character in each line
            for index, char in enumerate(i):
                index_character_tuples.append((index, char))
    for k, v in index_character_tuples:
        d[k].append(v)
    
    ###restructure dictionary so that each key is a stack # and value is a list of crates in that stack
    crate_dict = {}
    for character_list in d.values():
        for item in character_list:
            if item.isdigit():
                stack_number = item
                character_list.remove(stack_number)
                crate_dict[stack_number] = [a for a in character_list if not a.isspace()]
    
    return(crate_dict, instructions)

def part_1_crate_mover(crates_to_move, from_here, to_here):
    moving = from_here[0: crates_to_move]

    for i in range(crates_to_move):
        from_here.pop(0)
    for i in moving:
        to_here.insert(0, i)

def part_2_crate_mover(crates_to_move, from_here, to_here):
    moving = from_here[0: crates_to_move]

    for i in range(crates_to_move):
        from_here.pop(0)
    for i in reversed(moving):
        to_here.insert(0, i)

def parse_instructions(crates, instruction):
    nums = re.findall("\d+", instruction)
    crates_to_move = int(nums[0])
    from_here = crates[nums[1]]
    to_here = crates[nums[2]]

    return crates_to_move, from_here, to_here, crates   

def main():
    crate_dict, instructions = make_crate_dict(line_list)
    part_2_crate_dict = copy.deepcopy(crate_dict)

    for i in instructions:
        crates_to_move, from_here, to_here, crate_dict = parse_instructions(crate_dict, i)
        part_1_crate_mover(crates_to_move, from_here, to_here)

        crates_to_move, from_here, to_here, part_2_crate_dict = parse_instructions(part_2_crate_dict, i)
        part_2_crate_mover(crates_to_move, from_here, to_here)

    final = []
    final2 = []

    for i in crate_dict.values():
        final.append(i[0])
    for i in part_2_crate_dict.values():
        final2.append(i[0])

    crates_on_top = "".join(final)
    part_2_crates_on_top = "".join(final2)
    print(crates_on_top, part_2_crates_on_top)

if __name__ == '__main__': 
    main()