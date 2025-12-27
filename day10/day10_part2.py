import sys
import time
import pulp


def min_button_presses(buttons, target):
    problem = pulp.LpProblem("MinButtonPresses", pulp.LpMinimize)

    params = [pulp.LpVariable(f"p_{x}", lowBound=0, cat="Integer") for x in range(len(buttons))]
    problem += pulp.lpSum(params), "TotalButtonPresses"
    for y in range(len(target)):
        problem += (pulp.lpSum(buttons[x][y] * params[x] for x in range(len(buttons))) == target[y])

    status = problem.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[status] != "Optimal":
        return None, None

    presses = [int(v.value()) for v in params]
    
    return sum(presses), presses


def read_diagrams(data: str) -> list:
    sum_shortest = 0
    start_time = time.perf_counter()
    with open(data, 'r') as file:
        for line in file:
            operands = line.strip().split(" ")
            buttons = []
            target = [int(x) for x in list(operands[-1][1:-1:].split(","))]
            for index, operand in enumerate(operands):
                if index > 0 and index < len(operands) - 1:
                    button = [int(x) for x in list("0"*len(target))]
                    for val in operand[1:-1:].split(","):
                        button[int(val)] = 1
                    buttons.append(button)
            
            min_presses, _ = min_button_presses(buttons, target)
            sum_shortest += min_presses

             
        print("elapsed time:", time.perf_counter() - start_time)
        return sum_shortest

if __name__ == '__main__':

    print("Sum shortest: ", read_diagrams(sys.argv[1]))
