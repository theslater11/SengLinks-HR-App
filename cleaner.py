def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    valid_data = []
    #early return
    if len(data) == 0 or "":
        return data
    #looping through and stripping, then appending as an int if it isdigit
    for rate in data:
        rate = rate.strip()
        if rate.isdigit():
            valid_data.append(int(rate))
        else:
            rate = rate
    return valid_data



def filter_outliers(data: list) -> list:
    '''
    Filter all outliers from list, values over 250 and under 30

    Args:
        data (list[int]): list of integers representing heart rate samples.

    Returns:
        list[int]: list of integers, with all outliers removed
    '''
    
    non_ol = []
    #filter loop to remove outliers
    if data == []:
            return []
    for rate in data:
        if rate <= 30 or rate >= 250:
            rate = rate 
        else:
            non_ol.append(rate)
    return non_ol