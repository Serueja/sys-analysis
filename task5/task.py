import numpy as np

def flatten_e_list(expert_list):
    indexes = []
    flatten_values = []
    position = 0
    
    for i in range(len(expert_list)):
        if isinstance(expert_list[i], int):
            expert_list[i] = [expert_list[i]]
        for j in range(len(expert_list[i])):
            indexes.append(position)
            flatten_values.append(expert_list[i][j])
        position += 1

    return flatten_values, indexes

def create_matrix_from_e(expert_list):
    flatten_values, indexes = flatten_e_list(expert_list)
            
    matrix = []
    for i in range(len(flatten_values)):
        row = [0] * len(flatten_values)
        matrix.append(row)

    for i in range(len(indexes)):
        for j in range(len(indexes)):
            if indexes[flatten_values.index(i + 1)] <= indexes[flatten_values.index(j + 1)]:
                matrix[i][j] = 1

    return matrix

def calculate_nonequal_kernel(matrix_1, matrix_2):
    matrix_1 = np.array(matrix_1)
    matrix_2 = np.array(matrix_2)

    kernel = np.multiply(matrix_1, matrix_2)
    kernel_T = np.multiply(matrix_1.T, matrix_2.T)

    kernel_res = np.logical_or(kernel, kernel_T).astype(np.int32)
    result = []
    
    for i in range(len(kernel_res)):
        for j in range(len(kernel_res[i])):
            if kernel_res[i][j] == 0:
                    pair = sorted([i + 1, j + 1])
                    if pair not in result:
                        result.append(pair)
    
    conc_result = []

    visited = []
    for i in range(len(result)):
        visited.append(0)

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            set_1 = set(result[i])
            set_2 = set(result[j])

            if set_1.intersection(set_2):
                visited[i] = 1
                visited[j] = 1
                conc_result.append(list(set_1.union(set_2)))

        if result[i] not in conc_result and visited[i] == 0:
            conc_result.append(result[i])

    return conc_result

def is_value_in_kernel(value, kernel):
    for cluster in kernel:
        if value in cluster:
            return (True, cluster)
    return (False, [])

def expected_result(expert_1, expert_2, kernel):
    result = []

    for i in range(len(expert_1)):
        if isinstance(expert_1[i], int): 
            expert_1[i] = [expert_1[i]]
        for j in range(len(expert_2)):
            if isinstance(expert_2[j], int):
                expert_2[j] = [expert_2[j]]

            expert_1_set = set(expert_1[i])
            expert_2_set = set(expert_2[j])
            for value in expert_1[i]:
                flag, cluster = is_value_in_kernel(value, kernel)
                if flag:
                    if cluster not in result:
                        result.append(cluster)
                        break
            
            inter = expert_1_set.intersection(expert_2_set)
            if inter and not flag:
                if len(inter) > 1:
                    result.append(list(inter))
                else:
                    result.append(inter.pop())

    print(result)

def perform_task():
    expert_A = [[1], [2, 3, 4], [5, 6, 7], 8, 9, 10]
    expert_B = [[1, 2, 3], [4, 5], 6, 7, 9, [8, 10]] 
    expert_C = [1, 4, 3, 2,6,[5,7,8],[9,10]]
    matrix_A = create_matrix_from_e(expert_A)
    matrix_B = create_matrix_from_e(expert_B)
    matrix_C = create_matrix_from_e(expert_C)
    kernel_AB = calculate_nonequal_kernel(matrix_A, matrix_B)
    kernel_BC = calculate_nonequal_kernel(matrix_B, matrix_C)

    expected_result(expert_A, expert_B, kernel_AB)

if __name__ == '__main__':
    perform_task()