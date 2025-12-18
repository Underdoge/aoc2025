import sys

def count_splits(data: str) -> int:
    manifold = []
    splits = 0
    paths = 1
    with open(data, 'r') as file:
        for line in file:
            manifold.append(list(line.strip()))
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if manifold[y][x] == "S":
                manifold[y+1][x] = "|"
                print("start")
            elif manifold[y][x] == "^":
                if manifold[y-1][x] == '|':
                    manifold[y+1][x-1] = "|"
                    manifold[y+1][x+1] = "|"
                    splits += 1
                    paths *= 2
                else:
                    paths /= 2
            elif manifold[y][x] == '|':
                if y+1 < len(manifold) and manifold[y+1][x] == '.':
                    manifold[y+1][x] = '|'

    
    for line in manifold:
        print("".join(line))
    return paths

if __name__ == '__main__':

    print("path count: ", count_splits(sys.argv[1]))
