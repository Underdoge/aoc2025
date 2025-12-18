import sys

def count_splits(data: str) -> int:
    manifold = []
    splits = 0
    with open(data, 'r') as file:
        for line in file:
            manifold.append(list(line.strip()))
    for y in range(len(manifold)):
        for x in range(len(manifold[0])):
            if manifold[y][x] == "S":
                manifold[y+1][x] = "|"
                print("start")
            elif manifold[y][x] == "^" and manifold[y-1][x] == '|':
                manifold[y+1][x-1] = "|"
                manifold[y+1][x+1] = "|"
                splits += 1
            elif manifold[y][x] == '|':
                if y+1 < len(manifold) and manifold[y+1][x] == '.':
                    manifold[y+1][x] = '|'

    
    for line in manifold:
        print("".join(line))
    return splits

if __name__ == '__main__':

    print("Split count: ", count_splits(sys.argv[1]))
