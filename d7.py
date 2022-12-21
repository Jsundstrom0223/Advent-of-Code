# import re
# import itertools
# challenge_input = "d7.txt"

# with open(challenge_input, "r") as input_file:
#     line_list = input_file.readlines()
# l = [i.strip() for i in line_list]
# # print(l)
# elf_dic = {}
# class Elf_Dir():
    
#     def __init__(self, name, value=None):

#         self.name = name
#         # print(self.name)
#         self.value = 0
#         elf_dic[self.name] = [self.value]


# lll = {}
# commands = []
# dirss = []
# for i, v in enumerate(l):
#     if "$" in v:
#         # print(i, v)
#         # print("yuh")
   
#         # print("nah")
        
#         #     print(v, "!!!!")
#         # else:
#         commands.append(i)
 
#     elif v == "$ cd /":
#         # dirss.append(i)
#         v = Elf_Dir("outer")

#     elif "dir" in v:
#         dirss.append(i)
#         v = Elf_Dir(v)

# # print(Elf_Dir.elf_dir_list)
# # print(commands)

# # print(elf_dic)
# x = 1 
# y = 2
# # counter = 0
# # for k,v in lll.items():
# #     if v == "$ ls":
# #         print(k)
# #     icommands = itertools.islice(l[1: ], start, stop)

# ff = re.compile("\d+\s+\w+.+")
# def make_it_chunky(x, y):
    
#     for item in l:
#         # print(item)
#         start = commands[x]
#         # print(start)
#         s = start - 1
#         if s == 0:
#             outer = True
#         else:
#             outer = False
#         stop = commands[y]
#         dstart = dirss[x]
#         dstop = dirss[y]
#     # print(dstart, dstop, "!!")
#     # print(start, stop)
#     # icommands = itertools.islice(l, dstart, dstop)
#     idirs = itertools.islice(l, start, stop)
#     return list(idirs), start, outer

# class Elf_Dir():
#     def __init__(self, name, slist):
#         self.name = name
#         self.value = slist


# slist = []
# idirs, start, outer = make_it_chunky(x, y)  

# if outer:
#     thing = "outer"
#     command = idirs[0]
# else:
#     thing = idirs[0]
#     command = idirs[1]
# print(thing, command, "!")
# if command == "$ ls":
           
#         all = [item for item in idirs if not item.startswith("$")]

# idirs.remove(command)

# ff = re.compile("\d+\s+\w+")

# for o, item in enumerate(idirs):

#     sitem = item.split(" ")
#     if sitem[0] == "dir":
#         if o + 1 < len(idirs):
#             checker = idirs[o + 1]
#             print(item, "!!!!!!!!!!")
#             f = ff.match(checker)
#             if f:
#                 print(f.group(0), "?????")
#                 elf_dic[item].append(checker)
#                 print(elf_dic[item], "AAAAA")
        
# # print(slist)
    
#     if sitem[1] == "cd":
#         dir_name = sitem[2]
    
a = [1, 2, 3]
b = [7, 8, 9]
c = zip(a, b)
print(list(c))
