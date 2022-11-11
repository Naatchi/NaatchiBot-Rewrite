import numpy as np

from sklearn.neighbors import BallTree
from sklearn.base import BaseEstimator

def softmax(x):
    probability = np.exp(-x)
    return probability/sum(probability)

class NeighborSampler(BaseEstimator):
    def __init__(self, k=8, temperature=1.2):
        self.k = k
        self.temperature = temperature

    def fit(self, X, y):
        self.tree_ = BallTree(X)
        self.y_ = np.array(y)

    def predict(self, X, random_state=None):
        distances, indecies = self.tree_.query(X, return_distance = True, k = self.k)
        result = []
        dist = []
        for distance, index in zip(distances, indecies):
            result.append(np.random.choice(index, p = softmax(distance * self.temperature)))
            dist.append(distance)

        return self.y_[result], dist
