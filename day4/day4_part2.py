import sys

def remove_rolls(data: str) -> None:
    total_removed = 0
    rolls_y = []
    with open(data, 'r') as file:
        for line in file:
            rolls_x = list(line.strip())
            rolls_y.append(rolls_x)

    removed = 1
    while removed > 0:
        removed = 0
        for y in range(len(rolls_y)):
            for x in range(len(rolls_x)):
                rolls = 0
                new_y = y + 1
                if new_y < len(rolls_y) and rolls_y[new_y][x] == '@' and rolls_y[y][x] == '@':
                    rolls += 1
                new_x = x + 1
                if new_x < len(rolls_x) and rolls_y[y][new_x] == '@' and rolls_y[y][x] == '@':
                    rolls += 1
                if new_y < len(rolls_y) and new_x < len(rolls_x) and rolls_y[new_y][new_x] == '@' and rolls_y[y][x] == '@':
                    rolls += 1
                new_y = y - 1
                if new_y >= 0 and rolls_y[new_y][x] == '@' and rolls_y[y][x] == '@':
                    rolls += 1
                new_x = x - 1
                if new_x >= 0 and rolls_y[y][new_x] == '@' and rolls_y[y][x] == '@':
                    rolls += 1
                if new_y >= 0 and new_x >= 0 and rolls_y[new_y][new_x] == '@' and rolls_y[y][x] == '@':
                    rolls += 1
                new_x = x - 1
                new_y = y + 1
                if new_y < len(rolls_y) and new_x >= 0 and rolls_y[new_y][new_x] == '@' and rolls_y[y][x] == '@':
                    rolls += 1
                new_x = x + 1
                new_y = y - 1
                if new_x < len(rolls_x) and new_y >= 0 and rolls_y[new_y][new_x] == '@' and rolls_y[y][x] == '@':
                    rolls += 1

                if rolls_y[y][x] == '@' and rolls < 4:
                    rolls_y[y][x] = '.'
                    removed += 1

        total_removed += removed
    
    for yy in range(len(rolls_y)):
        for xx in range(len(rolls_x)):
            print(rolls_y[yy][xx], end="")
        print("")
    print("")
    return total_removed

if __name__ == '__main__':

    print("Removed rolls: ", remove_rolls(sys.argv[1]))
