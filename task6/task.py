import json
import numpy as np


def task(first_string, second_string):
    first_string, second_string = json.load(first_string), json.load(second_string)

    first_string_data, second_string_data = [], []

    for i in range(len(first_string)):
        if isinstance(first_string[i], list):
            for j in range(len(first_string[i])):
                first_string_data.append((i+1))
        else:
            first_string_data.append(i+1)
    
    for i in range(len(second_string)):
        if isinstance(second_string[i], list):
            for j in range(len(second_string[i])):
                second_string_data.append((i+1))
        else:
            second_string_data.append(i+1)
    
    first_string_data, second_string_data = np.array(first_string_data), np.array(second_string_data)
    data = np.array([first_string_data, second_string_data])
    

    sums = data.sum(axis=1)

    
    s = sums.sum()
    
    dif = []
    for el in sums:
        dif.append((s-el) ** 2)
    
    disp = sum(dif)/(len(data) - 1)
    return disp


def main():
    res1 = task(open("Ранжировка А.json"), open("Ранжировка B.json"))
    res2 = task(open("Ранжировка А.json"), open("Ранжировка C.json"))
    
    print(res1 / max(res1, res2))
    print(res2 / max(res1, res2))


if __name__ == "__main__":
    main()