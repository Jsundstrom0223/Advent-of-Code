challenge_input = "aoc_2022_d1.txt"

with open(challenge_input, "r") as input_file:
    cal_list = input_file.readlines()

cal_list = [e.rstrip() for e in cal_list]

elf_cal_totals = []

def elf_checker(cal_list):
    stop = ""
    if stop in cal_list:
        end_elf = cal_list.index(stop)
    else:
        return
            
    elf_cal_totals.append(sum([int(k) for k in cal_list[ : end_elf]]))
    
    if end_elf < len(cal_list):
        cal_list = cal_list[(end_elf + 1): ]
        elf_checker(cal_list)

    elf_cal_totals.sort(reverse=True)
    highest_cals = elf_cal_totals[0]
    top_three_totals = sum(elf_cal_totals[0: 3])

    return(highest_cals, top_three_totals)
 
highest_cals, top_three_totals = elf_checker(cal_list)
print(highest_cals, top_three_totals)
