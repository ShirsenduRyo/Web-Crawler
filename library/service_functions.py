import pandas as pd
import concurrent.futures
from datetime import datetime
from library.scrapper import web_scrapper


def current_time():
    return str(datetime.now())[:19]


def searching_ranks(data):
    print(data)
    curr_ranks = []

    #Applying Threading for each row
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(web_scrapper,data)

        for res in results:
            curr_ranks.append(res)

    return curr_ranks

