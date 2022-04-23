import pandas as pd
from numpy import random as rng


# I'm redoing this because returning a dict isn't a useful as combining aggregating the dataframes 
def behaviorally_reports(doc, row_offset=7, as_dicts=False) -> pd.DataFrame:
    d = pd.read_excel(doc, sheet_name=None)
    assert 'Index' in d.keys(), f"This doesn't look like the right type of spreadsheet: {doc}"
    
    _ = d.pop('Index')  # hack way to get rid of the index table

    dfs = []

    for k, df in d.items():
        df.columns = df.iloc[row_offset-1].values
        _df = df.iloc[row_offset:,].copy()  # using -1 to try and preserve the headers
        _df['REPORT'] = k
        d[k] = _df

        dfs.append(_df)

    if as_dicts:
        return dfs

    return pd.concat(dfs)


def sample_behaviorally_reports(doc, row_offset=7) -> pd.DataFrame:
    d = pd.read_excel(doc, sheet_name=None)
    assert 'Index' in d.keys(), f"This doesn't look like the right type of spreadsheet: {doc}"    
    _ = d.pop('Index')  # hack way to get rid of the index table
    k = rng.choice(list(d.keys()))
    df = d[k]
    df.columns = df.iloc[row_offset-1].values
    _df = df.iloc[row_offset:,].copy()  # using -1 to try and preserve the headers
    _df['REPORT'] = k

    return _df
