
import re
import itertools
challenge_input = "sample.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()
l = [i.strip() for i in line_list]
# print(l)

class Elf_Dir():
    def __init__(self, full_name, name, children=None):
        self.name = name 
        self.full_name = full_name
        self.chilren = children
        print(f"FULL NAME {self.full_name}, NAME {self.name}")


command_idxs = [i for i,v in enumerate(l) if v[0] == "$"]
dir_list = []
for i, v in enumerate(l):
    item = v.split(" ")
    if item[0] == "dir":
        dir_list.append(item[1])
        item[1] = Elf_Dir(v, item[1])
dir_list.insert(0, "/")
