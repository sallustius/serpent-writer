""" Various utilities"""

from numpy import array


def lim_check(lista, low, high, messaggio):
    """
    Function to check range of variable lista

    Parameters
    ----------
    lista: int, float, list, or np.array
        list to be bounded
    low: float
        lower limit
    high: float
        top limit
    messaggio: string
        Message to be desplayed in case of error

    Raises
    -------
    ValueError:
        When lista's entries are not in the validity range
    """
    if isinstance(lista, (int, float)):
        if not (low < lista < high):
            raise ValueError(messaggio)
        return
    lista = array(lista)
    low_bound = lista < low
    high_bound = lista > high
    if low_bound.any() or high_bound.any():
        raise ValueError(messaggio)


def dim_check(dims):
    """
    Checks if there are inconsistencies in the matrix dimensions

    Parameters
    ----------
    dims: np.array
        Array dimensions

    Raises
    ----------
    ValueError:
    If negative or zero dimensions
    ValueError:
    If the matrix is rectangular
    """
    if dims[0] == 0 or dims[1] == 0:
        raise ValueError('Fission Matrix has Zero Dimensions')
    elif dims[0] != dims[1]:
        raise ValueError('The Fission Matrix is Rectangular')


def str2vec(iterable, of=float, out=array):
    """
    Convert a string or other iterable to vector.

    Parameters
    ----------
    iterable: str or iterable
        If string, will be split with ``split(splitAt)``
        to create a list. Every item in this list, or original
        iterable, will be iterated over and converted accoring
        to the other arguments.
    of: type
        Convert each value in ``iterable`` to this data type.
    out: type
        Return data type. Will be passed the iterable of
        converted items of data dtype ``of``.

    Returns
    -------
    vector
        Iterable of all values of ``iterable``, or split variant,
        converted to type ``of``.

    Examples
    --------
    ::

        >>> v = "1 2 3 4"
        >>> str2vec(v)
        array([1., 2., 3., 4.,])

        >>> str2vec(v, int, list)
        [1, 2, 3, 4]

        >>> x = [1, 2, 3, 4]
        >>> str2vec(x)
        array([1., 2., 3., 4.,])

    """
    vec = (iterable.split() if isinstance(iterable, str)
           else iterable)
    return out([of(xx) for xx in vec])
