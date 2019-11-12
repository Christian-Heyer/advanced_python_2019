
def find_peaks(list_of_intensities, max_peak = True):
    """Find peaks

    Find local maxima for a given list of intensities. 
    Intensities are defined as local maxima if the 
    intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_intensities (list of floats or ints): a list of
            numeric values

    Returns:
        list of floats: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    max_value = 0
    list_of_maxima = []
    list_of_minima = []
    for pos, element in enumerate(list_of_intensities):
        if pos == 0:
            continue
        if pos == len(list_of_intensities) - 1:
            continue
        if list_of_intensities[pos - 1] < element > list_of_intensities[pos + 1]:
            max_value = element
            list_of_maxima.append(max_value)
        if list_of_intensities[pos - 1] > element < list_of_intensities[pos + 1]:
            min_value = element
            list_of_minima.append(min_value)          
    if max_value:
        return list_of_maxima
    else:
        return list_of_minima

def find_color_peaks(list_of_intensities, max_peak = True):
    intensity_sum = list()
    for color in list_of_intensities:
        intensity_sum.append(sum(color))
    
    print(intensity_sum)
    return find_peaks(intensity_sum, max_peak)
