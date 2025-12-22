import sys

def read_red_tiles(data: str) -> list:
    tiles = []
    with open(data, 'r') as file:
        for line in file:
            tiles.append([int(x) for x in line.strip().split(",")])
    return tiles

def find_biggest_rectange(data: str) -> int:
    circuits = []
    distances = {}
    tiles = read_red_tiles(data)
    biggest_area = 0
    for x in range(len(tiles)):
        for y in range(len(tiles)):
            if x != y:
                if tiles[x][0] != tiles[y][0] or tiles[x][1] != tiles[y][1]:
                    area = (abs(tiles[x][0]-tiles[y][0])+1) * (abs(tiles[x][1]-tiles[y][1])+1)
                    biggest_area = area if area > biggest_area else biggest_area
    return(biggest_area)

if __name__ == '__main__':

    print("Area of biggest rectangle: ", find_biggest_rectange(sys.argv[1]))
