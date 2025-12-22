import sys
from shapely.geometry import Polygon, Point

def read_red_tiles(data: str) -> list:
    tiles = []
    with open(data, 'r') as file:
        for line in file:
            tiles.append(tuple([int(x) for x in line.strip().split(",")]))
    return tiles

def find_biggest_rectange(data: str) -> int:
    circuits = []
    distances = {}
    tiles = read_red_tiles(data)
    biggest_area = 0
    poly = Polygon(tiles)
    for x in range(len(tiles)):
        for y in range(len(tiles)):
            if x != y:
                if tiles[x][0] != tiles[y][0] or tiles[x][1] != tiles[y][1]:
                    # combine x and y to obtain all corners, which sould be part of the tiles
                    corner_a = Point(tiles[y][0],tiles[x][1])
                    corner_b = Point(tiles[x][0],tiles[y][1])
                    rectangle = Polygon([tiles[x], corner_a, tiles[y], corner_b])
                    if poly.contains(rectangle):
                        area = (abs(tiles[x][0]-tiles[y][0])+1) * (abs(tiles[x][1]-tiles[y][1])+1)
                        biggest_area = area if area > biggest_area else biggest_area
    return(biggest_area)

if __name__ == '__main__':

    print("Area of biggest rectangle: ", find_biggest_rectange(sys.argv[1]))
