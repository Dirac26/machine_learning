import sys
import os

from pathlib import Path
from matplotlib import pyplot as plt

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(script_path.split('\\')[:-2])+'\\functions')
import distance, normalize

class KNearestNeighborsReg:
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
        self.normalization_method = 'min_max'


    def fit(self, dataset, labels):
        """
        set the data set and its lables for the model
        """
        self.dataset = dataset
        self.labels = labels
        self.normalization_n = []
        self.normalization_d = []
        for ind in range(len((self.dataset[list(self.dataset.keys())[0]]))):
            self.normalize_features(self.dataset, ind)

    def predict(self, unknown):
        """
        predect the label for all unknowns in unknown dict
        """
        for title in unknown:
            for ind in range(len((unknown[list(unknown.keys())[0]]))):
                unknown[title][ind] = (unknown[title][ind] - self.normalization_n[ind]) / (self.normalization_d[ind])
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
        if self.normalization_method == 'min_max':
            mini, maxi, norm_list = normalize.min_max_normalize(pre_norm_list)
            self.normalization_n.append(mini)
            self.normalization_d.append(maxi - mini)
        elif self.normalization_method == 'z_score':
            mean, var, norm_list = normalize.z_score_normalize(pre_norm_list)
            self.normalization_n.append(mean)
            self.normalization_d.append(var)
        elif self.normalization_method == 'none':
            norm_list = pre_norm_list[:]
            self.normalization_n.append(0)
            self.normalization_d.append(1)
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
        num = 0
        den = 0
        for neighbor in neighbors:
            lable = self.labels[neighbor[1]]
            dest_to_neighbor = neighbor[0]
            num += lable / dest_to_neighbor
            den += 1 / dest_to_neighbor
        return num/den

    def get_normalization(self):
        """
        """
        print('Use change_normalization method to set the normalization method to use')
        print('min_max')
        print('z_score')
        print('none')
        print (f'the model uses {self.normalization_method} normalization now')
        return self.normalization_method

    def change_normalization(self, arg):
        if arg == 'min_max':
            self.normalization_method = 'min_max'
        elif arg == 'z_score':
            self.normalization_method = 'z_score'
        elif arg == 'none':
            self.normalization_method = 'none'
        else:
            print('unknown normalization method')

    def ploter(self):
        """
        """
        pass

movies = {'1': [1, 1],
          '2': [2, 2],
          '3': [3, 4]}
labels = {'1': 5,
          '2': 8,
          '3': 7}
unknown = {'4': [2, 4]}
model = KNearestNeighborsReg()
model.change_normalization('none')
print(model.get_normalization())
model.fit(movies, labels)
print(model.predict(unknown))