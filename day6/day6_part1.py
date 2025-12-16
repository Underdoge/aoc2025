import sys

def make_calculations(data: str) -> int:
    operands = []
    operators = []
    with open(data, 'r') as file:
        for line in file:
            if line.strip().split()[0] != '+' and line.strip().split()[0] != '*': 
                operands.append([int(x) for x in line.strip().split()])
            else:
                operators.append(line.strip().split())

    results = [1 if x == '*' else 0 for x in operators[0]] 
    for x in range(len(operands[0])):
        for y in range(len(operands)):
            if operators[0][x] == '*':
                results[x] *= operands[y][x]
            else:
                results[x] += operands[y][x]
    
    return sum(results)

if __name__ == '__main__':

    print("Final sum: ", make_calculations(sys.argv[1]))
