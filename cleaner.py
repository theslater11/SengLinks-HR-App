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
    if len(data) == 0 or "":
        return data
    for rate in data:
        
        rate = int(rate.strip("\n"))
        if rate.isdigit():
            valid_data.append(int(rate))
        else:
            rate = rate
    return valid_data



def filter_outliers(data: list) -> list:
    non_ol =[]
    for rate in data:
        if data == []:
            return []
        if rate <= 30:
            rate = rate
        elif rate >= 250:
            rate = rate
        else:
            non_ol.append(rate)
    return non_ol