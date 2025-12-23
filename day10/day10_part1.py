import sys
import itertools
import time

def all_button_combinations(buttons: list) -> list:
    combinations = []
    for button in range(len(buttons) + 1):
        combinations.extend(itertools.combinations(buttons, button))
    return [list(c) for c in combinations] 

def mod2(combination: list, answer: list) -> bool:
    if len(combination) > 1:
        result = [s % 2 for s in map(sum, zip(*combination))]
    else:
        result = combination[0]
    return answer == result

def read_diagrams(data: str) -> list:
    diagrams = []
    sum_shortest = 0
    start_time = time.perf_counter()
    with open(data, 'r') as file:
        for line in file:
            operands = line.strip().split(" ")
            buttons = []
            for index, operand in enumerate(operands):
                if index == 0:
                    answer = [1 if x == '#' else 0 for x in operand[1:-1:]]
                elif index < len(operands) - 1:
                    button = [int(x) for x in list("0"*len(answer))]
                    for val in operand[1:-1:].split(","):
                        button[int(val)] = 1
                    buttons.append(button)
            all_combinations = all_button_combinations(buttons)
            all_combinations.pop(0)
            winning_combinations = []
            for combination in all_combinations:
                if mod2(combination, answer):
                    winning_combinations.append(combination)
                    if len(combination) <= 2:
                        sum_shortest += len(combination)
                        break
            
            winning_combinations = sorted(winning_combinations, key=len)
            # if shortest answer in the first set of combinations
            if len(winning_combinations) > 0 and len(winning_combinations[0]) <= 2:
                continue
            
            second_combination = list(itertools.combinations(all_combinations, 2))
            for index, combination in enumerate(second_combination):
                second_combination[index] = sum(combination, [])
            second_combination = sorted(second_combination, key=len)
            for combination in second_combination:
                if mod2(combination, answer):
                    winning_combinations.append(combination)
                    # quit when the first answer is found in the second set of combinations
                    break
            winning_combinations = sorted(winning_combinations, key=len)
            sum_shortest += len(winning_combinations[0])
        print("elapsed time", time.perf_counter() - start_time)
        return sum_shortest

if __name__ == '__main__':

    print("Sum shortest: ", read_diagrams(sys.argv[1]))
