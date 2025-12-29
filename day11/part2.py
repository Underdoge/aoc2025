import sys

def paths(instructions: dict, idx: int, visited: set = None, memo: dict = None) -> int:
    if visited is None:
        visited = set()
    if memo is None:
        memo = {}
    
    ins_list = list(instructions.keys())
    current_node = ins_list[idx]
    
    if current_node in visited:
        return 0
    
    visited.add(current_node)
    
    memo_key = (current_node, "dac" in visited, "fft" in visited)
    if memo_key in memo:
        return memo[memo_key]
    
    if instructions[ins_list[idx]][0] != 'out':
        count = 0
        count += paths(instructions, ins_list.index(instructions[ins_list[idx]][0]), visited.copy(), memo)
        if len(instructions[ins_list[idx]]) > 1:
            for output in instructions[ins_list[idx]][1:]:
                count += paths(instructions, ins_list.index(output), visited.copy(), memo)
        memo[memo_key] = count
        return count
    else:
        if "dac" in visited and "fft" in visited:
            memo[memo_key] = 1
            return 1
        else:
            memo[memo_key] = 0
            return 0

def read_instructions(data: str) -> list:
    instructions = {}
    with open(data, 'r') as file:
        for line in file:
            instruction = line.strip().split(" ")
            instructions[instruction[0][:-1:]] = [x for x in instruction[1:]]

    return instructions

def get_all_paths(data: str) -> int:
    instructions = read_instructions(data)
    idx = 0
    for index, key in enumerate(list(instructions.keys())):
        if key == "svr":
            print("found", index)
            idx = index
    return paths(instructions, idx, None, {})

if __name__ == '__main__':

    print("Different paths: ", get_all_paths(sys.argv[1]))

