import sys
import itertools
import numpy as np
import time

def gaussian_elimination(A, b):
    """
    Solves the system of linear equations Ax = b using Gaussian Elimination.
    
    Parameters:
        A (ndarray): Coefficient matrix (n x n)
        b (ndarray): Constant matrix (n x 1)
    
    Returns:
        x (ndarray): Solution vector
    """
    n = len(b)
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))

    # Forward Elimination
    for i in range(n):
        max_row = np.argmax(abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    # Back Substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:], x[i + 1:])) / augmented_matrix[i, i]

    return x

def read_diagrams(data: str) -> list:
    diagrams = []
    sum_shortest = 0
    start_time = time.perf_counter()
    with open(data, 'r') as file:
        for line in file:
            operands = line.strip().split(" ")
            buttons = []
            answer = [int(x) for x in list(operands[-1][1:-1:].split(","))]
            print(answer)
            for index, operand in enumerate(operands):
                if index > 0 and index < len(operands) - 1:
                    button = [int(x) for x in list("0"*len(answer))]
                    for val in operand[1:-1:].split(","):
                        button[int(val)] = 1
                    #button.reverse()
                    buttons.append(button)
            for button in buttons:
                print(button)
            
            A = np.array(buttons).T
            print(A)
            b = np.array(answer)
            x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
            
            print("sols", np.round(x, 0))
            input()
            
        print("elapsed time:", time.perf_counter() - start_time)
        return sum_shortest

if __name__ == '__main__':

    print("Sum shortest: ", read_diagrams(sys.argv[1]))
