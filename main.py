import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_blobs


# def generate_linearly_separable_data(m, margin):
def generate_linearly_separable_data(m, margin):

    X, y = make_blobs(
        n_samples=m, centers=2, n_features=2, center_box=(0, 10), random_state=21338859
    )

    data = np.empty(shape=(m, 4))
    data[:, 0] = 1
    data[:, (1, 2)] = X
    data[:, 3] = y

    return data


if __name__ == "__main__":
    number_of_samples = 100
    margin = 0.5
    # X, y = generuj_zbior_danych_separowalny_liniowo(m, margin)
    # X

    # data = generate_linearly_separable_data(number_of_samples, margin)

    # plt.scatter(data[:, 1], data[:, 2], c=data[:, 3])
    # plt.show()

    X = [1, 2, 3]
    y = [4, 5, 6]
    print(np.dot(X, y))

