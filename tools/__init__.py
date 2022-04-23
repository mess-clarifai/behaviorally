import numpy as np
from fuzzywuzzy import process


# TODO fix this hacky mess
def get_upc_mappings(a, b, threshold=75):
    """ 2 dfs -> upc mappings
    """
    d = {}
    d_ = {}

    for i, row in a.iterrows():  # each row will correspond to an item. need to look up UPC 10 digit
        upc = row['UPC 10 digit']  # the hard-coded strings are pathetic!!!
        match, score = process.extractOne(upc, b['upc'].values)

        if score >= threshold:
            d[match] = upc
            d_[upc] = match

    return d, d_


def desc_stats(a, center=np.mean, verbose=False):
    """thank you past me...
    """
    c = center(a)
    _min = np.min(a)
    _max = np.max(a)
    _mean = np.mean(a)
    _median = np.median(a)
    _std = np.std(a)
    
    if verbose: print(f"min: {_min}\nmax: {_max:.2f}\nmedian{'*' if np.isclose(_median, c) else ''}: {_median:.2f}\nmean{'*' if np.isclose(_mean, c) else ''}: {_mean:.2f}\nstd: {_std:.2f}")

    # return np.min(a), c, np.max(a)

    return {
        'min': _min,
        'max': _max,
        'mean': _mean,
        'median': _median,
        'std': _std,
    }
