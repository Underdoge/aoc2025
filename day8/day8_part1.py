import sys
from math import dist

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
    for index, circuit in enumerate(circuits):
        if junction_a in circuit:
            index_a = index
            break
        else:
            index_a = None
    for index, circuit in enumerate(circuits):
        if junction_b in circuit:
            index_b = index
            break
        else:
            index_b = None
     
    if index_a and index_b and index_a != index_b:
        circuits.append(circuits[index_a] + circuits[index_b])
        if index_b > index_a:
            circuits.pop(index_b)
            circuits.pop(index_a)
        else:
            circuits.pop(index_a)
            circuits.pop(index_b)
        return True
    return False

def junction_in_circuits(junction: list, circuits: list) -> bool:
    for index, circuit in enumerate(circuits):
        if junction in circuit:
            return True, index
    return False, 0

def multiply_junctions(data: str, connections: int) -> int:
    circuits = []
    distances = {}
    junctions = read_junction_boxes(data)
    for y in range(len(junctions)):
        for x in range(len(junctions)):
            if junctions[y] != junctions[x]:
                if str(dist(junctions[y], junctions[x])) not in distances:
                    distances[str(dist(junctions[y], junctions[x]))] = [junctions[y],junctions[x]]
    sorted_distances = sorted([float(x[0]) for x in distances.items()])
    circuit_index = 0
    for distance in [str(x) for x in sorted_distances]:
        if not junction_in_circuits(distances[distance][0], circuits)[0] and not junction_in_circuits(distances[distance][1], circuits)[0]:
            circuits.append([distances[distance][0]])
            circuits[circuit_index].append(distances[distance][1])
            circuit_index += 1
        elif both_junctions_in_different_circuit(distances[distance][0], distances[distance][1], circuits):
            circuit_index -= 1
        else:
            if not junction_in_circuits(distances[distance][0], circuits)[0]:
                circuits[junction_in_circuits(distances[distance][1], circuits)[1]].append(distances[distance][0])
            if not junction_in_circuits(distances[distance][1], circuits)[0]:
                circuits[junction_in_circuits(distances[distance][0], circuits)[1]].append(distances[distance][1])
    result = 1
    display_circuits(sorted(circuits, key=len, reverse=True)[:4])
    for circuit in sorted(circuits, key=len, reverse=True)[:4]:
        result *= len(circuit)
    return result

if __name__ == '__main__':

    print("Junctions multiplied: ", multiply_junctions(sys.argv[1], 10))
