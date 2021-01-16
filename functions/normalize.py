def min_max_normalize(lst):
    """
    return min max and normalized list using min-max normalizxation
    """
    minimum = min(lst)
    maximum = max(lst)
    normalized = [(x-minimum)/(maximum-minimum) for x in lst]
    return minimum, maximum, normalized

def z_score_normalize(lst):
    """
    return mean and var values with the normalized list using z_score
    """
    mean = sum(lst)/len(lst)
    dis = [(x - mean) ** 2 for x in lst]
    var = (sum(dis)/len(lst)) ** .5
    normalized = [(x - mean)/var for x in lst]
    return mean, var, normalized

def main():
    """
    the main function
    """
    n_list = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]
    n1_list = min_max_normalize(n_list)
    n2_list = min_max_normalize(n1_list)
    print(n1_list)
    print(n2_list)

if __name__ == "__main__":
    main()