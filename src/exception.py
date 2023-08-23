import sys #For exceptions


def error_message(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #Execution info
