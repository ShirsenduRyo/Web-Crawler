import requests
from bs4 import BeautifulSoup


def hit_server(url):
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    headers = {"user-agent" : user_agent}
    return requests.get(url,headers=headers)


def get_bs4_data(content):
    return BeautifulSoup(content, "html.parser")

