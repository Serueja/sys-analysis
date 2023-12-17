import numpy as np


def task() -> list[float]:
    # Находим все возможные суммы и произведения
    sums = set()
    products = set()
    for i1 in range(1, 7):
        for i2 in range(1, 7):
            sums.add(i1 + i2)
            products.add(i1 * i2)
    sums, products = sorted(sums), sorted(products)

    # Словари для нахождения индексов в таблице по сумме и произведению
    sum_lookup = {s: sums.index(s) for s in sums}
    product_lookup = {p: products.index(p) for p in products}

    # Матрица с количествами комбинаций для заданных суммы и произведения
    counts = np.zeros((len(sums), len(products)))
    for i1 in range(1, 7):
        for i2 in range(1, 7):
            counts[sum_lookup[i1 + i2], product_lookup[i1 * i2]] += 1

    # Матрица с вероятностями комбинаций для заданных суммы и произведения
    probabilities = counts / 36

    # ВЫЧИСЛЕНИЕ H(AB)
    entropy_ab = -np.sum(probabilities * np.log2(probabilities))

    # ВЫЧИСЛЕНИЕ H(A)
    # Матрица вероятностей только для события A
    probabilities_a = np.sum(probabilities, axis=1)
    entropy_a = -np.sum(probabilities_a * np.log2(probabilities_a))

    # ВЫЧИСЛЕНИЕ H(B)
    # Матрица вероятностей только для события B
    probabilities_b = np.sum(probabilities, axis=0)
    entropy_b = -np.sum(probabilities_b * np.log2(probabilities_b))

    # ВЫЧИСЛЕНИЕ H_A(B)
    entropy_a_b = entropy_ab - entropy_a

    # ВЫЧИСЛЕНИЕ I(A,B)
    information_ab = entropy_b - entropy_a_b

    return [round(el, 2) for el in [entropy_ab, entropy_a, entropy_b, entropy_a_b, information_ab]]

print(task())