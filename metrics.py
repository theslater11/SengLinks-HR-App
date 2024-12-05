def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []
    listo = []
    #Creating a list of numbers in a list until n is reached, then a new list is created and stored. 
    listo.append(data[:n:]) #gotta be a range function
    print(listo)
    #for loop to return max values from each list in a list of lists
    for size in listo:
        num = 0
        if max(size) > num:
            num = max(size)
            maximums.append(num)
    return maximums
result = window_max([1, 5, 3, 2, 4, 6, 7, 10, 9, 8], 4)
print(result)
    


def window_average(data: list, n: int) -> list:
    pass


def window_stddev(data: list, n: int) -> list:
    pass
