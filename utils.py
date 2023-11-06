# use this variable name to specify code that you like to be executed if the script in question is executed so utils.py we are not gping to want to run this script because we are defining functions to be used by other scriopt
#import tester 



def get_his_data_filename(pair, granularity):
    return f"his_data/{pair}_{granularity}.pkl"

def get_instruments_data_filename():
    return f"instrument.pkl"

if __name__ == "__main__":  ## __name__ is a predefined variable in python
    
    print(get_his_data_filename("EUR_USD", "H1"))