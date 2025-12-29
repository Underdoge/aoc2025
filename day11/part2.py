import sys

def paths(instructions: dict, idx: int, path: dict) -> int:
    ins_list = list(instructions.keys())
    print(ins_list[idx], instructions[ins_list[idx]], path)
    if instructions[ins_list[idx]][0] != 'out' and "dac" not in path and "fft" not in path:
        if ins_list[idx] not in path:
            count = paths(instructions, ins_list.index(instructions[ins_list[idx]][0]), path)
            if len(instructions[ins_list[idx]]) > 1:
                for output in instructions[ins_list[idx]][1:]:
                    count += paths(instructions, ins_list.index(output), path)
            path[ins_list[idx]] = count
        else:
            print("already went")
            count = path[ins_list[idx]]
        return count
    else:
        path[ins_list[idx]] = "out"
        print("path", path)
        if "dac" in path and "fft" in path:
            return 1
        else:
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
    return paths(instructions, idx, {})

if __name__ == '__main__':

    print("Different paths: ", get_all_paths(sys.argv[1]))

