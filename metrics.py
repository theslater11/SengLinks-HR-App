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
result = window_max([1, 5, 3, 2, 4, 6, 7, 10, 9, 8], 4)

print(result)
    


def window_average(data: list, n: int) -> list:
    averages =[]
    lista = [data[x:x+n] for x in range(0, len(data), n)]
    for avs in lista:
        averages.append(sum(avs) // len(avs))
    return averages

result = window_average([1, 5, 3, 2, 4, 6, 7, 10, 9, 8], 4)

print(result)
    


def window_stddev(data: list, n: int) -> list:
    pass
