import sys


def show_path(manifold):
    print("".join(manifold[len(manifold)-1]))

def read_manifold(data: str) -> list:
    manifold = []
    with open(data, 'r') as file:
        for line in file:
            manifold.append(list(line.strip()))
    return manifold

def paths(manifold: list, y: int, x: int) -> int:
    while y + 1 < len(manifold): 
        if manifold[y][x] == "S":
            manifold[y+1][x] = "|"
            y += 1
        elif manifold[y][x] == "^":
            manifold[y+1][x-1] = "|"
            left = paths(manifold, y+1, x-1)
            manifold[y+1][x+1] = "|"
            right = paths(manifold, y+1, x+1)
            return left + right
        elif manifold[y][x] == '|':
            if y + 1 < len(manifold):
                if manifold[y+1][x] == '.':
                    manifold[y+1][x] = '|'
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
                path_count = paths(manifold, y, x)
                print("paths:",path_count)
                break
    
    return path_count

if __name__ == '__main__':

    print("Path count: ", count_paths(sys.argv[1]))
