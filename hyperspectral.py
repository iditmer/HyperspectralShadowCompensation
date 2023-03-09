import numpy as np

# return the index in a sorted that is nearest to a specified value;
# this function assumes that the search value is somewhere between
# two of the values inside the array and will return 'None' if not
def nearest_index( sorted_array: np.ndarray, search_value: float ) -> int:
    for index in range(len(sorted_array) - 1):
        if sorted_array[index] < search_value and sorted_array[index + 1] > search_value:
            if search_value - sorted_array[index] < sorted_array[index + 1] - search_value:
                return index
            else: return index + 1    
    return None



# converts a row x column x band rater file into a (row * column) x band data matrix
# (each row in the resultant matrix represents the spectral values of one pixel)
def multispectral_raster_to_matrix( raster: np.ndarray ) -> np.ndarray:
    
    if len(raster.shape) != 3: raise ValueError('Input size expected to be rows x columns x bands.')
    
    rows = raster.shape[0]
    cols = raster.shape[1]
    bands = raster.shape[2]
    
    mat = raster.copy()
    return mat.reshape((rows * cols, bands))



# shortcut function for generating approximate RGB image from multispectral data
# assumes input wavelength array is sorted and in nanometers
def multispectral_raster_to_rgb( raster: np.ndarray, sorted_wavelengths: np.ndarray ) -> np.ndarray:
    
    if len(raster.shape) != 3: raise ValueError('Input size expected to be rows x columns x bands.')
    if len(sorted_wavelengths.shape) != 1: raise ValueError('Input wavelength array expected to be one-dimensional.')
    
    r = nearest_index(sorted_wavelengths, 685)
    g = nearest_index(sorted_wavelengths, 535)
    b = nearest_index(sorted_wavelengths, 475)

    if None in [r,g,b]: raise ValueError('Input wavelength array does not cover expected range of visible spectrum.')

    return raster[:,:,[r,g,b]]