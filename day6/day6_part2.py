import sys

def make_calculations(data: str) -> int:
    operands = []
    operators = []
    with open(data, 'r') as file:
        for line in file:
            if line.strip().split()[0] != '+' and line.strip().split()[0] != '*': 
                operands.append(line[:len(line)-1:])
            else:
                operators = line[:len(line)-1:]
    
    results = [1 if x == '*' else 0 for x in operators.strip().split()]
    result_index = len(results) - 1
    operand_stack = []
    for x in range(len(operands[0])-1, -1, -1):
        new_num = ""
        for y in range(len(operands)):
            if operands[y][x] != " ":
                new_num += operands[y][x]
        if new_num != "":
            operand_stack.append(int(new_num))
        if operators[x] != " " and y == len(operands) -1:
            if operators[x] == '+':
                for number in operand_stack:
                    results[result_index] += number
            else:
                for number in operand_stack:
                    results[result_index] *= number
            operand_stack = []
            result_index -= 1
        
    return sum(results)


if __name__ == '__main__':

    print("Final sum: ", make_calculations(sys.argv[1]))
