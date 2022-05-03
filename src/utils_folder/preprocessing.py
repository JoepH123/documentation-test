import pandas

def return_nr_columns(df):
    """
    Parameters
    ----------
        df: input of the function is a dataframe

    Returns
    ----------
        Returns the number of columns of the dataframe

    Testing
    -------
        .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}
    """
    return len(df)