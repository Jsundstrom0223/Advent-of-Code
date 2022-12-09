import re

challenge_input = "d4.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()

pair_list = [i for i in line_list]

def set_maker(n):     
    numbers = re.findall("\d+", n)

    one = [i for i in range(int(numbers[0]), int(numbers[1])+ 1)]
    two = [i for i in range(int(numbers[2]), int(numbers[3])+1)]
    elf_1 = set(one)
    elf_2 = set(two)

    subsets = part_1_subset_checker(elf_1, elf_2)
    any_overlap = part_2_overlap_checker(elf_1, elf_2)
    return subsets, any_overlap

def part_1_subset_checker(elf_1, elf_2):
    elf_1_is_subset = elf_1.issubset(elf_2)   
    elf_2_is_subset = elf_2.issubset(elf_1)

    if elf_1_is_subset or elf_2_is_subset:
        return 1
    else:
        return 0

def part_2_overlap_checker(elf_1, elf_2):
    elf_1_is_subset = elf_1.issubset(elf_2)   
    elf_2_is_subset = elf_2.issubset(elf_1)

    if elf_1_is_subset or elf_2_is_subset:
        return 1
    else:
        any_intersection = elf_1.isdisjoint(elf_2)
        if any_intersection:
            return 0
        else:
            return 1

i = map(set_maker, pair_list)
results_list = list(zip(*i))

subset_total = sum(results_list[0])
overlap_total = sum(results_list[1])

print(subset_total, overlap_total)