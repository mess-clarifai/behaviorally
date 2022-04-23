import os
import yaml


JOB_NUMBERS_FILE = "data/JobNumbers.yaml"


# need to get the values from data/JobNumbers.yaml
# this file was originally written in the notebook notebooks/items-of-interest.ipynb
def __get_job_numbers(k='JobNumber'):
    """as always w/ this, h/t: https://stackoverflow.com/a/1774043
    """
    with open(JOB_NUMBERS_FILE, "r") as f:
        try:
            d = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
    
    return d[k]

ONS_ANALYSIS_JOB_NUMBERS = __get_job_numbers()
