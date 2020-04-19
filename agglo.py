import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt


def vectorize(userdict, allskills):
    vectordict = {}
    for name, skills in userdict.items():
        #Create empty vector of 0s
        vector = [0] * len(allskills)
        for i in range(len(allskills)):
            #if user skill is the same as allskills[i] update vector[i]
            for skill in skills:
                if skill == allskills[i]:
                    vector[i] = 1
        vectordict[name] = vector

    # print("USER VECTORS")
    # [print(vec, name) for name,vec in vectordict.items()]
    # print()

    return vectordict

#Creates a cosine similarity matrix
def matrix(vectordict):
    cosmatrix = []
    for user1, vector1 in vectordict.items():
        cosvector = []
        for user2, vector2 in vectordict.items():
            cosvector.append(__cossim(vector1, vector2))
        cosmatrix.append(cosvector)

    return cosmatrix

#Clusters data and outputs a dendrogram
def cluster(cosmatrix, names, clustertype):
    plt.close()
    X = np.array(cosmatrix)

    linked = linkage(X, clustertype)

    labelList = names

    plt.figure(figsize=(12, 9))
    dendrogram(linked,
        color_threshold=2.2,
        orientation='top',
        labels=labelList,
        leaf_rotation=90,
        distance_sort='descending',
        show_leaf_counts=True)

    plt.tight_layout()
    plt.show()

#COSINE SIMILARITY CALCULATIONS
def __dot(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))

def __mag(v):
    total = 0
    for num in v:
        total += num * num

    return math.sqrt(total)
def __cossim(x, y):
    return __dot(x, y) / (__mag(x) * __mag(y))



