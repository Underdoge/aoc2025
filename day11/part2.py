import sys

def paths(instructions: dict, idx: int, visited: set = None, all_paths: dict = None) -> int:
    if visited is None:
        visited = set()
    if all_paths is None:
        all_paths = {}
    
    ins_list = list(instructions.keys())
    current_node = ins_list[idx]
    
    if current_node in visited:
        return 0
    
    visited.add(current_node)
    
    node = (current_node, "dac" in visited, "fft" in visited)
    if node in all_paths:
        return all_paths[node]
    
    if instructions[ins_list[idx]][0] != 'out':
        count = paths(instructions, ins_list.index(instructions[ins_list[idx]][0]), visited.copy(), all_paths)
        if len(instructions[ins_list[idx]]) > 1:
            for output in instructions[ins_list[idx]][1:]:
                count += paths(instructions, ins_list.index(output), visited.copy(), all_paths)
        all_paths[node] = count
        return count
    else:
        if "dac" in visited and "fft" in visited:
            all_paths[node] = 1
            return 1
        else:
            all_paths[node] = 0
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
            idx = index
    return paths(instructions, idx, None, {})

if __name__ == '__main__':

    print("Different paths: ", get_all_paths(sys.argv[1]))

