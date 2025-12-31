import sys

def available_shapes(shapes: list, region: dict) -> (list, list):
    available = []
    available_num = []
    for key in region.keys():
        for idx, number in enumerate(region[key]):
            if number > 0:
                tile_lines = []
                for line in shapes[idx]:
                    tile_lines.append([1 if x == '#' else 0 for x in line])
                available.append(tile_lines)
                available_num.append(number)
    return available, available_num

def real_area(shape: list) -> int:
    area = 0
    for line in shape:
        for block in line:
            area += block
    return area

def fit_test(shapes: list, region: dict) -> bool:
    available, num = available_shapes(shapes, region)
    shapes_area = 0
    for idx, shape in enumerate(available):
        shapes_area += num[idx]*real_area(shape)
    dimensions = region_size(region)
    return shapes_area <= dimensions[0]*dimensions[1]

def region_size(region: dict) -> list:
    for idx, size in enumerate(region.keys()):
        return [int(x) for x in size.split("x")]

def test_presents(data: str) -> (list, list):
    shapes = []
    shape_count = 6
    regions = []
    with open(data, 'r') as file:
        for line in file:
            if line[0].isdigit() and int(line[0]) < 6 and line[1] == ":":
                read_shapes = 3
                shape = []
            elif line != "\n" and read_shapes > 0 and shape_count >= 0:
                shape.append(line.strip())
                read_shapes -= 1
                if read_shapes == 1:
                    shapes.append(shape)
                    shape_count -= 1
            elif line != "\n":
                regions.append({line.strip()[:line.index(":")] : [int(x) for x in line.strip()[line.index(":")+2:].split(" ")]})

    fit_number = 0

    for region in regions:
        fit_number += 1 if fit_test(shapes, region) else 0
    return fit_number

if __name__ == '__main__':

    print("How many fit: ", test_presents(sys.argv[1]))

