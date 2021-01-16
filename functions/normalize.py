def min_max_normalize(lst):
    """
    return normalized list useing min-max normalizxation
    """
    minimum = min(lst)
    maximum = max(lst)
    normalized = [(x-minimum)/(maximum-minimum) for x in lst]
    return minimum, maximum, normalized

def main():
    """
    """
    n_list = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]
    n1_list = min_max_normalize(n_list)
    n2_list = min_max_normalize(n1_list)
    print(n1_list)
    print(n2_list)

if __name__ == "__main__":
    main()