import sys

def count_fresh(data: str) -> None:
    fresh = 0
    ranges_done = False
    ranges = []
    with open(data, 'r') as file:
        for line in file:
            if not ranges_done:
                if line != "\n":
                    ranges.append([int(line.strip().split("-")[0]),int(line.strip().split("-")[1])])
                else:
                    ranges_done = True
            else:
                id = int(line)
                for range in ranges:
                    if id >= range[0] and id <= range[1]:
                        fresh += 1
                        break

    return fresh

if __name__ == '__main__':

    print("Fresh ingredients: ", count_fresh(sys.argv[1]))
