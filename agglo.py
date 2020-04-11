import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

def matrix(vectordict):
    cosmatrix = []
    for user1, vector1 in vectordict.items():
        cosvector = []
        for user2, vector2 in vectordict.items():
            cosvector.append(__cossim(vector1, vector2))
        cosmatrix.append(cosvector)
    return cosmatrix

def cluster(cosmatrix, names, clustertype):
    X = np.array(cosmatrix)

    linked = linkage(X, clustertype)

    labelList = names

    plt.figure(figsize=(10, 7))
    dendrogram(linked,
        orientation='top',
        labels=labelList,
        distance_sort='descending',
        show_leaf_counts=True)

    plt.show()

def __dot(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))
def __mag(v):
    total = 0
    for num in v:
        total += num * num

    return math.sqrt(total)
def __cossim(x, y):
    return __dot(x, y) / (__mag(x) * __mag(y))