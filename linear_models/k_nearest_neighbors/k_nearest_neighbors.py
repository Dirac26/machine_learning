import sys
import os

from pathlib import Path
from matplotlib import pyplot as plt

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append('/'.join(script_path.split('/')[:-2]))
from functions import distance, normalize


class KNearestNeighbors:
    """
    class that generates k nearest neighbor model with logistic rating
    """
    def __init__(self):
        """
        init function
        """
        self.k = 1
        self.dataset = {}
        self.labels = {}

    def fit(self, dataset, labels):
        """
        set the data set and its lables for the model
        """
        self.dataset = dataset
        self.labels = labels
        self.minimum = []
        self.maximum = []
        for ind in range(len((self.dataset[list(self.dataset.keys())[0]]))):
            self.normalize_features(self.dataset, ind)
    
    def predict(self, unknown):
        """
        predect the label for all unknowns in unknown dict
        """
        for title in unknown:
            for ind in range(len((unknown[list(unknown.keys())[0]]))):
                unknown[title][ind] = (unknown[title][ind] - self.minimum[ind]) / (self.maximum[ind] - self.minimum[ind])
        print(unknown)
        unknown_labels = {}
        for title in unknown:
            neighbors = self.k_neighbors(unknown[title], self.dataset, self.k)
            unknown_labels[title] = self.rate(neighbors, self.labels)
        return unknown_labels

    def normalize_features(self, data_dict, ind):
        """
        """
        pre_norm_list = []
        for title in data_dict:
            pre_norm_list.append(data_dict[title][ind])
        mini, maxi, norm_list = normalize.min_max_normalize(pre_norm_list)
        self.minimum.append(mini)
        self.maximum.append(maxi)
        for i, title in enumerate(data_dict):
            data_dict[title][ind] = norm_list[i]

    def k_neighbors(self, unknown, dataset, k):
        """
        generate the closest neighbors list
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
        generate rating for the new unknown
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

movies = {'1': [1, 1],
          '2': [2, 2],
          '3': [3, 4]}
labels = {'1': 1,
          '2': 1,
          '3': 0}
unknown = {'4': [2, 5]}
model = KNearestNeighbors()
model.fit(movies, labels)
print(model.predict(unknown))