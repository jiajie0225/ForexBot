# use this variable name to specify code that you like to be executed if the script in question is executed so utils.py we are not gping to want to run this script because we are defining functions to be used by other scriopt
#import tester 

import datetime as dt
from dateutil.parser import *


def get_his_data_filename(pair, granularity):
    return f"his_data/{pair}_{granularity}.pkl"

def get_instruments_data_filename():
    return f"instrument.pkl"

def time_utc(): #
    return dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc) #Modified to add timezone

def get_utc_dt_from_string(date_str): # allow us to take on timestring without timezone and read it as a date and return with UTC timezone
    d = parse(date_str)
    return d.replace(tzinfo=dt.timezone.utc)


if __name__ == "__main__":  ## __name__ is a predefined variable in python
    
    print(get_his_data_filename("EUR_USD", "H1"))