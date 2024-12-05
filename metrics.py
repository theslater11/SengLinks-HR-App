import statistics

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
    #Creating a list of numbers in a list until n is reached, saving that list, then creating a new list.
    listo = [data[x:x+n] for x in range(0, len(data), n)]
    print(listo)
    #for loop to save max values from each list in a list of lists to list -> maximums
    for size in listo:
        num = 0
        if max(size) > num:
            num = max(size)
            maximums.append(num)
    return maximums

def window_average(data: list, n: int) -> list:
    '''
    Calculate the average of every 'n' size window.

    ARGS:
    data (list[int]): list of integers representing heart rate samples
    n (int): The size of your window

    RETURNS:
    list[int]: list of averages from each window

    '''
    averages =[]
    lista = [data[x:x+n] for x in range(0, len(data), n)]
    for avs in lista:
        averages.append(sum(avs) // len(avs))
    return averages

def window_stddev(data: list, n: int) -> list:
    '''
    Calculate the standard deviation of every 'n' size window.

    ARGS:
    data (list[int]): list of integers representing heart rate samples
    n (int): The size of your window

    RETURNS:
    list[int]: list of standard deviations from each window
    '''
    stddev = []
    liste = [data[x:x+n] for x in range(0, len(data), n)]
    for sd in liste:
        stddev.append(statistics.stdev(sd))
    return stddev
