
import string
challenge_input = "d3.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()

rucksack_list = [line.rstrip() for line in line_list]
lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

def part1_duplicate_finder(rl):
    duplicated_items = []

    for line in rl:
        compartment_1 = [item for item in line[ :(len(line) // 2)]]
        compartment_2 = [item for item in line[(len(line) // 2): ]]
        s = set(compartment_1).intersection(compartment_2)
        for i in s:
            duplicated_items.append(i)

    return duplicated_items

def part2_duplicate_finder(rl):
    badges = []
    
    for i in range(0, len(rl), 3):
        elf_group = rl[i: i +3]  
        s1 = set(elf_group[0]).intersection(elf_group[1])
        s2 = set(s1).intersection(elf_group[2])
        for i in s2:
            badges.append(i)

    return badges

def make_priority_dict(alphabet_list1, alphabet_list2):
    count = 0
    alphabet_list1.extend(alphabet_list2)
    priority_dict = dict()

    for letter in alphabet_list1:
        count += 1
        priority_dict[letter] = count
            
    return(priority_dict)

def get_priority(items, priority_dict):
    total = []
    
    for item in items:
        a = priority_dict.get(item)
        total.append(a)
 
    return sum(total)

###PART 1:
duplicated_items = part1_duplicate_finder(rucksack_list)
priority_dict = make_priority_dict(lower_alphabet, upper_alphabet)
p1_total = get_priority(duplicated_items, priority_dict)

###PART 2 MODIFICATIONS:
badges = part2_duplicate_finder(rucksack_list)
p2_total = get_priority(badges, priority_dict)
