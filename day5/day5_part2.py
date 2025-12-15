import sys

def count_fresh(data: str) -> None:
    fresh_ids = 0
    ranges_done = False
    ranges = []
    with open(data, 'r') as file:
        for line in file:
            if not ranges_done:
                if line != "\n":
                    ranges.append([int(line.strip().split("-")[0]),int(line.strip().split("-")[1])])
                else:
                    ranges_done = True
            if ranges_done:
                break

    removed = True
    while removed:
        removed = False
        for index in range(len(ranges)):
            for index_loop in range(len(ranges)):
                if index != index_loop and ranges[index][1] >= ranges[index_loop][0] and ranges[index][1] <= ranges[index_loop][1]:
                    new_start = ranges[index][0] if ranges[index][0] < ranges[index_loop][0] else ranges[index_loop][0]
                    to_remove = [ranges[index], ranges[index_loop]]
                    to_append = [new_start, ranges[index_loop][1]]
                    for delete_range in to_remove:
                        ranges.remove(delete_range)
                    ranges.append(to_append)
                    removed = True
                    break
            if removed:
                break

    for range_ids in ranges:
        fresh_ids += range_ids[1] - range_ids[0] + 1

    return fresh_ids

if __name__ == '__main__':

    print("Fresh ingredient ids: ", count_fresh(sys.argv[1]))
