import sys
import os

from matplotlib import pyplot as plt

sys.path.insert(0, '../..')

import distance

class KNearestNeighbors:
    """
    """
    def __init__(self):
        """
        """
        self.k = 3
        self.dataset = {}
        self.labels = {}

    def fit(self, dataset, labels):
        """
        """
        self.dataset = dataset
        self.labels = labels
    
    def predect(self, unknown):
        """
        """
        unknown_labels = {}
        for title in unknown:
            neighbors = self.k_neighbors(title, self.dataset, self.k)
            unknown_labels[title] = self.rate(neighbors, self.labels)
        return unknown_labels

    def k_neighbors(self, unknown, dataset, k):
        """
        """
        distances = []
        for title in dataset:
            point = dataset[title]
            distance_to_point = distance.euclidean_distance(point, unknown)
            distances.append([distance_to_point, title])
        distances.sort()
        neighbors = distances[0:k]
        return neighbors

    def rate(self, neighbors, labels):
        """
        """
        num_good = 0
        num_bad = 0
        for neighbor in neighbors:
            title = neighbor[1]
            if labels[title] == 0:
                num_bad += 1
            elif labels[title] == 1:
                num_good += 1
        if num_good > num_bad:
            return 1
        else:
            return 0

    def ploter(self):
        """
        """
        pass

movies = {'1': (1, 1),
          '2': (2, 2),
          '3': (3, 3)}
labels = {'1': 1,
          '2': 1,
          '3': 0}
unknown = {'4': (1, 2)}
model = KNearestNeighbors()
model.fit(movies, labels)
print(model.predect(unknown))