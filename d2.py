from collections import Counter
challenge_input = "d2.txt"

with open(challenge_input, "r") as input_file:
    line_list = input_file.readlines()

RPS = [i.rstrip() for i in line_list]

class Choice():
    outcome_dicts = {}
    
    def __init__(self, symbol):
        self.symbol = symbol
        self.score_for_move = Choice.get_score(symbol)
        (loses, wins) = self.get_outcomes()
        self.outcome_dict = {6: loses, 0: wins}
        Choice.outcome_dicts[self.symbol] = self.outcome_dict
    
    def get_score(move):
        score_dict = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}  
        score = score_dict.get(move)
        return score
        
    def get_outcomes(self):
        WINS_FOR_P2 = [(1, 2), (2, 3), (3, 1)]
        for player_moves in WINS_FOR_P2:
            if player_moves[0] == self.score_for_move:
                loses = player_moves
            if player_moves[1] == self.score_for_move:
                wins = (player_moves[1], player_moves[0])
        return(loses, wins)

def get_round_score(moves):
    me = moves[2]
    elf = moves[0]
    
    desired_outcome = {"X": 0, "Y": 3, "Z": 6}
    score_for_outcome = desired_outcome.get(me)
    
    if score_for_outcome != 3:
        target = Choice.outcome_dicts[elf][score_for_outcome]
        score_for_move = target[1]
        
    if score_for_outcome == 3:
        score_for_move = Choice.get_score(elf)
    
    round_score = score_for_move + score_for_outcome
    return round_score

def part_one(i):
    elf_score = Choice.get_score(i[0])
    my_score = Choice.get_score(i[2])
    both = (elf_score, my_score)
    winners = Choice.outcome_dicts[i[0]]
    
    if my_score == elf_score:
        score = 3
        return score + my_score
    else:
        for k, v in winners.items():
            if both == v:
                return k + my_score

def get_total(RPS, round):
    cnt = Counter()

    for i in RPS:
        cnt[i] += 1

    move_score = {}
    for i in cnt.keys():
        if round == 1:
            score = part_one(i)
        else:
            score = get_round_score(i)
        move_score[i] = score

    all = []
    for k, v in move_score.items():
        per_move = cnt[k] * v
        all.append(per_move)

    print(sum(all))

Rock = Choice("A")
Paper = Choice("B")
Scissors = Choice("C")

total_1 = get_total(RPS, 1)
total_2 = get_total(RPS, 2)
