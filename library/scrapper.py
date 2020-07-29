from library.utils import *
from library.url_matcher import string_search



def web_scrapper(parameters):
    """
        Assigning parameters to
        their respective use
    """
    domain = parameters[0]
    keyword = parameters[1]

    # Formating the keyword to use it in url
    keyword = keyword.replace(' ','+')

    url=f"https://google.com/search?q={keyword}&num=100"
    resp = hit_server(url)
    if resp.status_code == 200:
        soup = get_bs4_data(resp.content)


        """
            Using the company domain provided to check
            if it appears in the list or not
        """
        rank,token = string_search(domain,soup)
        if not token:
            rank = 'n/a'
        print(domain,':',rank)



    else:
        print("sorry!")
        rank = "Error Encountered"

    return rank