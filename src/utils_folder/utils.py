import pandas

def count_rows(df):
    """
    Parameters
    ----------
        df: input of the function is a dataframe

    Returns
    ----------
        it returns the number of rows there are in the dataframe

    Testing
    -------
        .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}
    """
    return df.shape[0]
