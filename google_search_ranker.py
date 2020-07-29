

from library.service_functions import *
from library.gspread_funcs import *
from library.decorators import *


@timer
def main_function():

    #Reading from the csv file
    file = "TEST SHEET"
    #data = read_file(file)
    data, datafile, file_obj = read_from_file(file)

    # datetime object containing current date and time
    curr_time = current_time()

    #Extract the data from Gspread File
    rank_for_this_session = searching_ranks(data)
    print(rank_for_this_session)

    #update the Gspread file file

    """
        Columns name for the current session
        (Time of execution of the file)
    """
    column_name = "Ranks on :" + curr_time

    #Getting the Current rank from
    datafile[column_name] = rank_for_this_session
    update_data(file_obj,datafile)


main_function()
