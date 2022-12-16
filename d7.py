import re
import itertools
challenge_input = "d7.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()
l = [i.strip() for i in line_list]
# print(l)
class Elf_Dir():
  
    def __init__(self, name, value):

        self.name = name.split(" ")[1]
        print(self.name)
        self.value = value


commands = []
dirss = []
for i, v in enumerate(l[1: ]):
    if "$" in v:
        # print(i, v)
        # print("yuh")
    # else:
    #     print("nah")
        commands.append(i)
    if "dir" in v:
        dirss.append(i)
# print(commands)
x = 0
y = 0

x = 0
y = 1
for item in commands:
    # print(item)
    start = commands[x]
    stop = commands[y]
    dstart = dirss[x]
    dstop = dirss[y]
    # print(start, stop)
    icommands = itertools.islice(l[1: ], start, stop)
    # idirs = itertools.islice(l[1: ], dstart, stop)
ff = re.compile("\d+\s+\w+.+")
# for d in idirs:
#     print(d)
for e in icommands:
    # print(e)
    if e == "$ ls":
        print(e)
        continue
    # print(e, "!")
    f = ff.match(e)
    
    if f:
        print(f.group(0))


# # for i in line_list[ : commands[1]]:
# #     print(i)