import sys

def read_manifold(data: str) -> list:
    manifold = []
    splits = 0
    with open(data, 'r') as file:
        for line in file:
            manifold.append(list(line.strip()))
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if manifold[y][x] == "S":
                manifold[y+1][x] = "|"
            elif manifold[y][x] == "^" and manifold[y-1][x] == '|':
                manifold[y+1][x-1] = "|"
                manifold[y+1][x+1] = "|"
                splits += 1
            elif manifold[y][x] == '|':
                if y+1 < len(manifold) and manifold[y+1][x] == '.':
                    manifold[y+1][x] = '|'
    return manifold

def paths(manifold: list, y: int, x: int, path: dict) -> int:
    while y + 1 < len(manifold):
        if manifold[y][x] == '|':
            if y + 1 < len(manifold):
                y += 1
        elif manifold[y][x] == "^":
            count = 0
            if str([y,x]) not in path:
                count += paths(manifold, y+1, x-1, path)
                count += paths(manifold, y+1, x+1, path)
                path[str([y,x])] = count
                return count
            else:
                count += path[str([y,x])]
            return count
    return 1

def count_paths(data: str) -> int:
    manifold = read_manifold(data)

    # for line in manifold:
    #     print("".join(line))
    
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if manifold[y][x] == 'S':
                path_count = paths(manifold, y+1, x, {})
                break
    
    return path_count

if __name__ == '__main__':

    print("Path count: ", count_paths(sys.argv[1]))
