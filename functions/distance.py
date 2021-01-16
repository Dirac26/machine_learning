def euclidean_distance(pt1, pt2):
    """
    return euclidean distance between two points
    """
    distance = 0
    for i in range(len(pt1)):
        distance += (pt1[i] - pt2[i]) ** 2
    distance = distance ** 0.5
    return distance

def manhattan_distance(pt1, pt2):
    """
    return manhattan distance between two points
    """
    distance = 0
    for i in range(len(pt1)):
        distance += abs(pt1[i] - pt2[i])
    return distance

def hamming_distance(pt1, pt2):
    """
    return hamming distance between two points
    """
    distance = 0
    for i in range(len(pt1)):
        if pt1[i] != pt2[i]:
            distance += 1
    return distance