from itertools import count

import numpy as np
import pandas as pd
import fuzzywuzzy as fuzz

# TODO fix this hacky mess
def get_upc_mappings(a, b, threshold=75):
    """ 2 dfs -> upc mappings
    """
    d = {}
    d_ = {}

    for i, row in a.iterrows():  # each row will correspond to an item. need to look up UPC 10 digit
        upc = row['UPC 10 digit']  # the hard-coded strings are pathetic!!!
        match, score = fuzz.process.extractOne(upc, b['upc'].values)

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


def infer_report_dates(data, target_column='REPORT', periods=156, frequency='w', start_date='3/31/2019'):
    T = 156  # total number of reports
    report_dates = {}
    t_0 = pd.to_datetime(start_date)  # just from looking at the Index page from their report spreadsheet.
    for i in count(start=data[0]):  # start with the first value to be more agnostic to different indexing schemes
        t_i = t_0 + pd.Timedelta(i, unit='w')  # period t_i
        report_dates[float(i)] = t_i
        if i-1 == T:
            break

    
    date_map = lambda t: report_dates.get(t)

    infered_dates = [date_map(t) for t in data]
    infered_dates = pd.to_datetime(infered_dates)

    return infered_dates
    
