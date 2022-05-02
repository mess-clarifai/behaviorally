import os
import yaml


JOB_NUMBERS_FILE = "data/JobNumbers.yaml"

## NOTE See notebooks/analysis.ipynb for complete documentation
# I'm bringing in the full set of things here, because the significantly reduced dimensionality admits a greater
# analytical utility to the previously omitted metrics-of-interest
KEY_CONDITIONALS = [
    'Image Name',
    'Image ID',
    'Product',  
    'Category Name',
    'Sub-Category Name',
    'REPORT',
]

KEY_METRICS = [
    'Dollar Sales',  # using this as the key analytical category, given the price effects
    # 'Dollar Sales % Change vs YA',  # removing the 'temporal' categories for now to simplify the analysis
    'Unit Sales',
    # 'Unit Sales % Change vs YA',
    'Unit Share of Category',
    # 'Unit Share of Category Year Ago',
    'Unit Share of SubCategory',
    # 'Unit Share of SubCategory Year Ago',
    'Price per Unit',  # correlation simpy doesn't make sense here
    # 'Price per Unit % Change vs YA',  # correlation simply doesn't make sense here.
]

TO_NORMALIZE = [
    # 'Raw ONS Line and Pack',  # norm x?
    'Dollar Sales',  # using this as the key analytical category, given the price effects
    'Unit Sales',
    'Price per Unit',  # correlation simpy doesn't make sense here
]

# NOTE This is all worthless now that they have identified the key images.
## need to get the values from data/JobNumbers.yaml
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

IMAGES_OF_INTEREST = [
    'AD905_LINE1.jpg',
    'AD112_LINE1A.jpg',
    'AD456_PACK5.jpg',
    'L2362_LINE1.jpg',
    'AC296_LINE1.jpg',
    'AB031_LINE1.jpg',
    'AB220_LINE1A.jpg',
    'L2310_LINE1.jpg',
    'AD386_PACK1.jpg',
    'AC808_LINE1.jpg',
    'L1874_LINE1.jpg',
    'AB653_LINE1.jpg',
    'AC904_LINE1.jpg',
    'AD411_LINE1.jpg',
    'AD387_PACK1.jpg',
    'AD474_LINE1.jpg',
    'AD719_LINE1.jpg',
    'AB111_LINE1.jpg',
    'AD517_LINE1.jpg',
    'L2403_LINE1.jpg',
    'AB219_LINE1.jpg',
    'AB474_LINE1.jpg',
    'AD230_LINE1.jpg',
    'AD457_LINE1.jpg',
    'AC624_LINE1.jpg',
    'AD087_LINE1.jpg',
    'AD692_LINE1.png',
    'L1501_LINE1.jpg',
    'AD296_PACK1.jpg',
    'AD445_PACK1.jpg',
    'AB185_LINE1.jpg',
    'L2331_LINE1.jpg',
    'AD518_LINE1.jpg',
    'AD216_LINE1.jpg',
    'AD275_PACK1.jpg',
    'AD145_PACK1.jpg',
    'AD513_LINE1.jpg',
    'AD324_LINE1.jpg',
    'AC870_LINE1.jpg',
    'AC856_LINE1.jpg',
    'AD672_LINE1.jpg',
    'AB249_LINE1.jpg',
    'L2115_LINE1.jpg',
    'AD083_LINE1.jpg',
    'AD615_LINE1.jpg',
    'AD507_LINE1A.jpg',
    'AD644_LINE1.jpg',
    'AD697_LINE1.jpg',
    'AD437_LINE1.jpg',
    'AC638_PACK1.jpg',
    'AD549_LINE2.jpg',
]
