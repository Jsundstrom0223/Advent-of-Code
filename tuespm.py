import re
import itertools
from collections import defaultdict
challenge_input = "d7.txt"
callenge_input = "sample.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()
l = [i.strip() for i in line_list]

elf_dic= defaultdict(list)

class Elf_Dir():
    
    def __init__(self, name, index, value=None):
        if name != "outer":
            n = name.split(" ")
            nname = n[1]
        else:
            nname = "/"
        self.name = nname
        self.index = index
        self.value = 0

    def find_dir_out_one_level(current):
        for k,v in elf_dic.items():
            if current in v:
                new_thing = k
                print(new_thing)
                return new_thing

lscommands = []
cdcommands = []
other = []
dirss = []
dir_list = []
for i, v in enumerate(l):
    sv = v.split(" ")
    if sv[1] == "ls":
        lscommands.append(i)
 
    if sv[1] == "cd":
        if sv[2] == "/":
            dir_list.append(sv[2])
        else:
            cdcommands.append(i)
    elif "dir" in v:
        
        dv = v.split(" ")
        # elf_dic[dv] = []
        dir_list.append(dv[1])
        v = Elf_Dir(v, i)
        dirss.append(i)
        # dir_list.append

    if sv[0] != "$":
        other.append(i)
    elf_dic = dict.fromkeys(dir_list)
print(elf_dic, 59, "!!!")
print("LS", lscommands)
# for e in dirss:
#     print(l[e])
print(dir_list)

ff = re.compile("\d+\s+\w+.+")
counter = 0
def make_it_chunky(x, y):
    
    start = lscommands[x] - 1
    # print(len(lscommands), y)
    # print(len(l))
    if y < len(lscommands):
        stop = lscommands[y] -1
    else:
        stop = None

    # print(start, stop, "!!!!!!!!!!!!!!")
    idirs = itertools.islice(l, start, stop)
    return list(idirs)
  
def command_handler(idirs):
        ll = []

        changed_to = idirs[0]
        which_dir = changed_to.split(" ")[2]
       
        
        command = idirs[1]

        # print(f" CHANGED TO {changed_to}, NAME OF CD {which_dir}, COMMAND {command}, !")
        idirs.remove(command)
       
        if command == "$ ls":
            idirs.remove(changed_to)      
            for item in idirs:
                if item == "$ cd ..":
                    break
           
                split_dir_file_name = item.split(" ")
                if split_dir_file_name[1] in dir_list:
                    to_add = split_dir_file_name[1]
               
                else:
                    # print(split_dir_file_name, "SHOULD NOT BE DIR")
                    to_add = int(split_dir_file_name[0])
                ll.append(to_add)
           
            elf_dic[which_dir] = ll
        return elf_dic
    
def replacer():
        #            
    for k, v in elf_dic.items():
        # print(k, v)
        for i in v:
            if i in elf_dic.keys():
                # print(f"{i} in {k}")
                aa = v.index(i)
                # print(aa)
                    
                v.insert(aa, {i: elf_dic[i]})
                v.pop(aa + 1)
                # print(v, "\n")
          
                # print("NO!", i)
    # print(elf_dic)
            # if changed_to in v:
            #     print(k, v, changed_to, "@@@@@@@@@@@@@@")
            # else:
            #     print(v)
                # print(split_dir_file_name)
                # print(sitem, "?", changed_to, "?", which_dir, "********************")

               
                #     # elf_dic[to_add].append("")
                #     # elf_dic[which_dir].append(split_dir_file_name[1])
                # else:
                #     to_add = split_dir_file_name[0]
                #     # print(to_add, "!!!!")
                    
                # elf_dic[which_dir].append(to_add)
                # print(sitem[1], "_______________", which_dir, elf_dic.items())

def handle_inner_dirs():
    for k,v in elf_dic.items():
        for item in v:
            if item in dir_list:
                
                here = v.index(item)
                print(item, k, here)
                print(elf_dic[item])
                v.pop(here)
                v.insert(here, {item: elf_dic[item]})
                # print(elf_dic.items())
            # else:
            #     print(k, "********")
    print("126")
            #     for oh in v:
            #         if oh == split_dir_file_name[1]:
            #             print(split_dir_file_name[1], elf_dic[k], "!!!!!!!!!!!!")
                # else:
                #     print(split_dir_file_name[1], "nh")
#                     else:
#                         print(sitem[1], elf_dic.keys())
#                 if sitem[0].isdigit():
#                     add_item = int(sitem[0])
#                     print("DIG", sitem, which_dir)
#                 if add_item not in elf_dic[which_dir]:
#                     elf_dic[which_dir].append(add_item)
#                     # print("ADDED", sitem, ssthing)
#                 # else:
#                 #     break    
#             # print(ll)
#             # for ee in ll:
                
#             #     elf_dic[ssthing].append(ee)
#             # print(thing, "THING DICT", elf_dic[ssthing], "\n")
#             for k, v in elf_dic.items():
#                 if which_dir in v:
#                     print("\n", k, v, which_dir, elf_dic[which_dir], "HERE !@$")
#             #         aa = v.index(ssthing)
#             #         # print(aa)
                    
#             #         v.insert(aa, {ssthing: elf_dic[ssthing]})
#             #         v.pop(aa + 1)
#             #         # print(v)
                    
#         #     return elf_dic[thing]
                
# #       
#         # if c[0] == "cd":
#         #     if c[1] == "..":
#         #         new = Elf_Dir.find_dir_out_one_level(thing)
#         #         print(f" NEW 97 in COMMAND HANDLER {new}")
                
#         #     else:
#         #         new = c[1]
#         #         print(f" NEW 101 in COMMAND HANDLER {new}")
#         #         return new
#         # # print(elf_dic[thing], thing, "ELF DIC")
#         # print(f" C 103 IN COMMAND HANDLER {c}")
#         # return 
#         # print(elf_dic)
        # print(elf_dic.values())

kt = 0
newd = defaultdict(list)
lll = []
##works
def totaler(o, kt):
    print("TOP!!!", o) 
    # print(f"KEY {o} VALS {elf_dic[o]}")
    # for k in elf_dic:
    for i in elf_dic[o]:
        # print(o, 215)
        # print(i)
        if i not in elf_dic.keys():
            # print(f"i {i} not in VALS of {o}")
            kt = kt + i
            # print(f"TOTAL {kt} of KEY {o}")
        else:
            # print(f"v {i} in VALS, \n, \n")
            kt = totaler(i, kt)
            # kt = kt + i
        # for i in v:
        #     print(f"i on 189 {i} in {v}")
        # print(v)
    #     print(v)
            # print(f"TOTAL {kt} of KEY {o}")
    if kt < 100000:
        return kt
    else:
        return 0
    # # print(elf_dic.values())
    #     # if v in elf_dic.keys():
    #         print(f"V {v} in VALS")
    #     else:
    #         print(f"v {v} not in VALS")

      
    # print(o)
    # print(elf_dic.keys())
            # print(f"{i} in keys")
        # else:
        #     print(f"{i} in keys")
    #     print(i, "I", 140)
    #     kt = kt + i
    #     print(kt)
    # else:
    #     print(i, 143)
    #     kt = totaler(i, kt)
    #     print(kt)
    
    # except:
    #     print("ya done fucked up", i, o)
        # return None
big = []      
# def ntotaler(o, kt):
#     print("TOP!!!", o, kt)    
#     for i in :
#         if i not in elf_dic.keys():
#             kt = kt + i
#         else:
#             kt = totaler(i, kt)
#     return kt

def checker():
    ll = []
    bb = 0
    for i in l:
        si = i.split(" ")
        # print(si)
        if si[0] == "dir" and si[1] not in ll:
            bb += 1
            ll.append(si[1])
            print(si[1])
    print(bb)
    return ll

def executer():
  
    x = 0 
    y = 1
    
    for i in lscommands:

        idirs = make_it_chunky(x, y)  

        command_handler(idirs)
        
  
        x += 1
        y += 1
    print("NEXT:", elf_dic)
    # handle_inner_dirs()
    # handle_inner_dirs()

    
#     print(elf_dic.items(), "^^^^^^^^^^^^^^^^^^^^^^")
#     a = []
#     for k in elf_dic.keys():
#         print(k)
#         a.append(k)
#     print(len(a))
#     # for i in elf_dic.values():
#     #     for e in i:
#     #         print(e, type(e))
#     # idirs = make_it_chunky(x, y)  

#     # command_handler(idirs)
#     # x += 1
#     # y += 1
#     # idirs = make_it_chunky(x, y)  
#     # print(x, y, "!!!!!!!!!!")
#     # command_handler(idirs)
#     # x += 1
#     # y += 1
#     # idirs = make_it_chunky(x, y)  
#     # # print(idirs)
#     # # print("HHH!")
   
#     # command_handler(idirs)
    hhh = 0
# #     # # # print(elf_dic.items())
    for k, v in elf_dic.items():
        # print("K!:", k, v, "\n")
        hhh += totaler(k, 0) 
    print(hhh)
        
        
        # hhh += totaler(k, 0)
        # hhh = totaler(k, 0)
        # print(k)
        # print(hhh)
#         # break
   

# # h = checker()
executer()
# print(h[1])
# print(elf_dic[h[1]])
# hh = totaler(h[1], 0)
# print(hh)