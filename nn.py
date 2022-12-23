import re
import itertools
from collections import defaultdict
from anytree import Node, RenderTree, findall, PreOrderIter, find_by_attr
challenge_input = "d7.txt"
callenge_input = "sample.txt"

with open(callenge_input, "r") as input_file:
    line_list = input_file.readlines()
l = [i.strip() for i in line_list]

# class ElfNode:
#     def __init__(self, full_name, files=None):
#         self.full_name = full_name
#         print("!!!!!!!!!!!", self.full_name)
#         if not self.full_name == "/":
#             self.short_name = self.full_name.split(" ")[1]
#         else:
#             self.short_name = "outer"
#         if files:
#             self.files = files
#         print(self.short_name, "NAME")
#         print(f"FULL NAME {self.full_name}, KIDS {self.children}")

# class MixedNode(ElfNode, NodeMixin):
#     def __init__(self, parent=None, children=None):
#         super(MixedNode, self).__init__()
       
#         if parent:
#             self.parent = parent
#             print(f"PARENT {parent.full_name}")
#         if children:
#             self.children = children
#             # print(self.children, "!!!!")
#         # if files:
#         #     self.files = files
      


                # print(splite)
        # print(RenderTree(root)._byattr())

# # elf_dic= defaultdict(list)
# def find_dir_out_one_level(current):
#     for k,v in elf_dic.items():
#         if current in v:
#             new_thing = k
#             print(new_thing)
#             return new_thing

def split_and_list(l):
    print("HERE")
    lscommands = []
    other = []
    dir_idxs = []
    dir_list = []
    cdcommands = []

    for i, v in enumerate(l):
        sv = v.split(" ")

        if sv[1] == "ls":
            lscommands.append(i)
    
        if sv[1] == "cd":
            if sv[2] == "/":
                dir_list.append(sv[2])
                dir_idxs.append(i)
            cdcommands.append(i)

        if sv[0] == "dir":
            dir_list.append(v)
            dir_idxs.append(i)
    
        if sv[0] != "$":
            other.append(i)

        elf_dic = dict.fromkeys(dir_list)

    print("DIR", dir_list)
    return lscommands, cdcommands, dir_idxs, other, dir_list, elf_dic

lscommands, cdcommands, dir_idxs, other, dir_list, elf_dic = split_and_list(l)
# print("OTHER", other, "!!!")
print("LS", lscommands)
# print("CD", cdcommands)
# print("DIR INDEXES", dir_idxs)

# print(elf_dic)

    # print("HERE", root.children)
# print(DirNodes.root.getattr())
# print(Node.outer.children)
print()
    
def make_tree(dir_list):
   
    for e in dir_list:
        # print("E", e)
        if e == "/":
            outer = Node("/", parent=None)
        else:
            # print(splite, "!!!!!!!!!!")
            splite = Node(e, parent=outer)
            # print(splite.path, "{PPPPP")
            # print(node.name)
    # print(RenderTree(outer))

    # print(bb, "!!!")
    return outer

    # print(outer.children, "KIDS")
    # style=AsciiStyle()


outer = make_tree(dir_list)
print(RenderTree(outer))
print(outer.children)
# print(a.parent)
def make_it_chunky(x, y):
    
    start = lscommands[x] - 1
    if y < len(lscommands):
        stop = lscommands[y] -1
    else:
        stop = None
    print(start, stop, l[start], l[stop])
    idirs = itertools.islice(l, start, stop)
    return list(idirs)

idirs = make_it_chunky(0, 1)
# idirs.insert(0, "$ cd a")
# print("IDIRS", idirs)
  

def parser(idirs, outer):
    adder = []
    command = idirs[0].split(" ")
    if idirs[1] == "$ ls":
        print("JAAJJAJAJA")
    idirs.pop(1)
    idirs.pop(0)
    target = command[2]
    if target == "/":
        target = outer
    # print(target, "@")
    # for pre, node in RenderTree(outer):
    #     print(pre, node, "?????????????")
    bb = [node.name for node in PreOrderIter(outer)]
    # print(outer.children, bb, "BBBBBBB")

        # print(spliti, "SPLITI!!!")
   

    for i in idirs:
    ####need to account for switching dirs if cd, otherwise successfully making new kids for items not in tree
    #         print(i)
    #         print("$$$$$$")
    #         idirs.remove(i)
    #         print(idirs)

        here = i.split(" ")[0] 

        hh = [node.name for node in outer.children if node.name == i]
        if i not in hh:
            print("FFF", i)
            here = i.split(" ")[0]
            i = Node(here, parent=target)
        else:
            print("YYYY", i)
            
    print(RenderTree(outer))

    print("DONE")

parser(idirs, outer)

def totaler(o, kt):

    try:
        for i in elf_dic[o]:
            
                if i not in elf_dic.keys():
                    print(i, type(i), "!!!!!!!!!!!", o)
                
                    kt = kt + i
                  
                else:
                    kt = totaler(i, kt)
                    print(i, "_________________")
    except TypeError:
        print(f"O!!!! {o}, i {i} {type(o)} {type(i)} HERE")

        if kt < 100000:
            return kt
        else:
            return 0

def checker():
    ll = []
    bb = 0
    for i in l:
        si = i.split(" ")
        if si[0] == "dir" and si[1] not in ll:
            bb += 1
            ll.append(si[1])
    return ll

def executer():
    checker()
  
    x = 0 
    y = 1
    
    for i in lscommands:

        idirs = make_it_chunky(x, y)  
        command_handler(idirs)
        x += 1
        y += 1
  
