import sys
import itertools


def display_circuits(circuits: list) -> None:
    for index, circuit in enumerate(circuits):
        print(circuit, index)

def read_junction_boxes(data: str) -> list:
    junctions = []
    with open(data, 'r') as file:
        for line in file:
            junctions.append([int(x) for x in line.strip().split(",")])
    return junctions

def both_junctions_in_different_circuit(junction_a: list, junction_b: list, circuits) -> bool:
    
    in_circuit_a, index_a = junction_in_circuits(junction_a, circuits)
    in_circuit_b, index_b = junction_in_circuits(junction_b, circuits)
    if in_circuit_a and in_circuit_b and index_a != index_b:
        circuits[index_a] += circuits[index_b]
        circuits.pop(index_b)
        return True
    return False

def junction_in_circuits(junction: list, circuits: list) -> bool:
    for index, circuit in enumerate(circuits):
        if junction in circuit:
            return True, index
    return False, 0

def distance_pow2(junction_a: list, junction_b: list) -> int:
    distance = 0
    for index, val in enumerate(junction_a):
        distance += pow(abs(junction_a[index] - junction_b[index]),2)
    return int(distance)

def multiply_junctions(data: str, connections: int) -> int:
    circuits = []
    distances = {}
    junctions = read_junction_boxes(data)
    for junc in list(itertools.combinations([index for index, _ in enumerate(junctions)],2)):
        if str(distance_pow2(junctions[junc[0]], junctions[junc[1]])) not in distances:
            distances[str(distance_pow2(junctions[junc[0]], junctions[junc[1]]))] = [junc[0],junc[1]]
    
    sorted_distances = sorted([int(x[0]) for x in distances.items()])
    for index, distance in enumerate([str(x) for x in sorted_distances]):
        print("distance", distance, distances[distance], index)
    input()
    circuit_index = 0
    for index, distance in enumerate([str(x) for x in sorted_distances]):
        print("distance", distance, distances[distance], index)
        if not junction_in_circuits(distances[distance][0], circuits)[0] and not junction_in_circuits(distances[distance][1], circuits)[0]:
            circuits.append([distances[distance][0]])
            circuits[circuit_index].append(distances[distance][1])
            circuit_index += 1
        elif both_junctions_in_different_circuit(distances[distance][0], distances[distance][1], circuits):
            cable_length = junctions[distances[distance][0]][0] * junctions[distances[distance][1]][0]
            if len(circuits) == 1:
                print("breaking")
                break
            circuit_index -= 1
        else:
            if not junction_in_circuits(distances[distance][0], circuits)[0]:
                circuits[junction_in_circuits(distances[distance][1], circuits)[1]].append(distances[distance][0])
            if not junction_in_circuits(distances[distance][1], circuits)[0]:
                circuits[junction_in_circuits(distances[distance][0], circuits)[1]].append(distances[distance][1])
        display_circuits(circuits)
        input()
    return cable_length

if __name__ == '__main__':

    print("Junctions multiplied: ", multiply_junctions(sys.argv[1], 10))
