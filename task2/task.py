import numpy as np

def task(matrix_csv):
    lines = matrix_csv.split("\n")
    matrix = []
    
    for i in range(len(lines)):
        matrix.append(list(map(int, lines[i].split(","))))

    H = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            p = matrix[i][j] / (len(matrix) - 1)
            if p>0: 
                H = H - p * np.log2(p)

    return H