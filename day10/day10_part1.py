import sys
import itertools
import numpy as np

def all_button_combinations(buttons: list) -> list:
    combinations = []
    for button in range(len(buttons) + 1):
        combinations.extend(itertools.combinations(buttons, button))
    return [list(c) for c in combinations] 

def mod2(combination: list, answer: list) -> bool:
    if len(combination) > 1:
        result = sum(combination) % 2
    else:
        result = combination
    return np.array_equal(answer, result)

def read_diagrams(data: str) -> list:
    diagrams = []
    sum_shortest = 0
    with open(data, 'r') as file:
        for line in file:
            operands = line.strip().split(" ")
            print(operands)
            buttons = []
            for index, operand in enumerate(operands):
                if index == 0:
                    answer = np.array([1 if x == '#' else 0 for x in operand[1:-1:]])
                    print(answer, "<--")
                elif index < len(operands) - 1:
                    button = [int(x) for x in list("0"*len(answer))]
                    for val in operand[1:-1:].split(","):
                        button[int(val)] = 1
                    buttons.append(np.array(button))
            for button in buttons:
                print(button)
            print("")
            all_combinations = all_button_combinations(buttons)
            all_combinations.pop(0)
            for combination in all_combinations:
                print(combination)
            print("")
            input()
            # test first set of combinations
            winning_combinations = []
            for combination in all_combinations:
                if mod2(combination, answer):
                    sum_shortest += len(combination)
                    winning_combinations.append(combination)
                    if len(combination) <= 3:
                    #    break
            if len(winning_combinations) > 0:
                winning_combinations = sorted(winning_combinations, key=len)
                if len(winning_combinations[0]) <= 3:
                    sum_shortest += len(winning_combinations[0])
                    print("found shortest in first iteration", len(winning_combinations[0]))
                    print("")
            #        continue
             
            second_combination = list(itertools.combinations(all_combinations, 2))
            for combination in second_combination:
                print(combination)
                input()
            print("")
            input()
            

            for combination in second_combination:
                combination = sum(combination, [])
                if mod2(combination, answer):
                    winning_combinations.append(combination)
                    if len(combination) <= 3:
                        print("found shortest in second iteration fast", len(combination))
                        break
            winning_combinations = sorted(winning_combinations, key=len)
            sum_shortest += len(winning_combinations[0])
            print("shortest combination", winning_combinations[0], len(winning_combinations[0]))
            print("")
        print("sum shortest", sum_shortest)
        return sum_shortest

if __name__ == '__main__':

    print("Sum shortest: ", read_diagrams(sys.argv[1]))
