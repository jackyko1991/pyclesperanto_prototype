from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import generate_touch_matrix
from .._tier1 import count_touching_neighbors
from .._tier1 import replace_intensities

@plugin_function(categories=['label measurement', 'map'])
def local_maximum_touching_neighbor_count_map(source : Image, destination : Image = None) -> Image:
    """Takes a label map, determines which labels touch and replaces every 
    label with the number of touching neighboring labels.

    Parameters
    ----------
    source : Image
    destination : Image, optional
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_touchingNeighborCountMap
    """
    from .._tier1 import set_column
    from .._tier2 import maximum_of_touching_neighbors

    touch_matrix = generate_touch_matrix(source)
    number_of_touching_neighbors_vector = count_touching_neighbors(touch_matrix)

    local_maximum_vector = maximum_of_touching_neighbors(number_of_touching_neighbors_vector, touch_matrix)

    # ignore how many objects touch the background
    set_column(number_of_touching_neighbors_vector, 0, 0)
    replace_intensities(source, local_maximum_vector, destination)
    return destination
