import sys


def show_path(manifold):
    for line in manifold:
        print("".join(line))

def read_manifold(data: str) -> list:
    manifold = []
    with open(data, 'r') as file:
        for line in file:
            manifold.append(list(line.strip()))
    return manifold

def paths(manifold: list, y: int, x: int, path: dict) -> int:
    while y + 1 < len(manifold):
        if manifold[y][x] == "S":
            if str([y+1,x]) not in path:
                manifold[y+1][x] = "|"
            y += 1
        elif manifold[y][x] == "^":
            count = 0
            if str([y+1,x-1]) not in path:
                manifold[y+1][x-1] = "|"
                count += paths(manifold, y+1, x-1, path)
                path[str([y+1,x-1])] = count
           # else:
            #    return path[str([y+1,x-1])] 
            if str([y+1,x+1]) not in path:
                manifold[y+1][x+1] = "|"
                count += paths(manifold, y+1, x+1, path)
                path[str([y+1,x+1])] = count
           # else:
            #    return path[str([y+1,x+1])] 
            return count
        elif manifold[y][x] == '|':
            if y + 1 < len(manifold):
                if manifold[y+1][x] == '.':
                    if str([y+1,x]) not in path:
                        manifold[y+1][x] = '|'
                    else:
                        print("already in path middle")
                y += 1
    show_path(manifold)
    return 1

def count_paths(data: str) -> int:
    manifold = read_manifold(data)

    for line in manifold:
        print("".join(line))
    
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if manifold[y][x] == 'S':
                path_count = paths(manifold, y, x, {})
                print("paths:",path_count)
                break
    
    return path_count

if __name__ == '__main__':

    print("Path count: ", count_paths(sys.argv[1]))
