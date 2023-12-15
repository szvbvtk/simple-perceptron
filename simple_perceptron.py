# def generate_data(m, margin):
# data = np.empty(shape=(m, 4))
# data[:, 0] = 1
# data[:, (1, 2)] = np.random.uniform(-1, 1, size=(m, 2))
# data[:, 3] = np.sign(data[:, 1] ** 2 + data[:, 2] ** 2 - margin)

# return data


# def generate_linearly_separable_data(m, margin):
#     data = np.empty(shape=(m, 4))
#     data[:, 0] = 1
#     data[:, (1, 2)] = np.random.uniform(-100, 100, size=(m, 2))
#     data[:, 3] = np.sign(data[:, 1] + data[:, 2] - margin)

#     return data


# def generate_linearly_separable_data(m, margin):
#     X, y = make_classification(
#         n_samples=m,
#         n_features=2,
#         n_informative=2,
#         n_redundant=0,
#         random_state=42,
#         n_clusters_per_class=1,
#         class_sep=margin,
#     )
#     # X, y = make_blobs(n_samples=m, centers=2, n_features=2, center_box=(0, 10))
#     X, y = make_classification(
#         n_features=2,
#         n_redundant=0,
#         n_informative=2,
#         n_clusters_per_class=1,
#         n_classes=2,
#         n_samples=m,
#         class_sep=margin,
#     )


#     data = np.empty(shape=(m, 4))
#     data[:, 0] = 1
#     data[:, (1, 2)] = X
#     data[:, 3] = y

#     return data
# import numpy as np

# x = np.array([-1, 1, 1, -1, -1, 1, 1, -1, -1])
# y = np.array([-1, -1, 1, 1, -1, -1, 1, 1, -1])

# print(x != y)
# print(np.flatnonzero(x != y))
