import numpy as np

def calculate_area(r):
    """
    Calculates the area of a circle.

    Parameters
    ----------
    r : float or array
        The radius of a single circle or multiple circles

    Returns
    -------
    area : float or array
        The calculated area/s
    
    Examples
    --------
    >>> calculate_area(1)
    3.141592653589793
    """
    if np.any(r < 0):
        raise ValueError("'r' should be non-negative")
        
    area = np.pi * r **2
    return area


def calculate_circ(r):
    """
    Calculates the circumference of a circle.

    Parameters
    ----------
    r : float or array
        The radius of a single circle or multiple circles

    Returns
    -------
    circ : float or array
        The calculated circumference/s
    """
    circ = 2 * np.pi * r
    return circ