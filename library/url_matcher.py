def string_search(domain, soup):

    """
        Initializing rank,token.
        This should be returned if
        no result is obtained
    """

    rank = -1
    token = False

    """
        Algorithm that scrapes out data from
        google search engine results and
        arranges it into native python lists
    """

    # <div class="r">...</div>
    # has all the results hence taking out it
    # and looping over all the classes

    for i, g in enumerate(soup.find_all('div', class_='r')):
        anchors = g.find_all('a')

        if anchors:
            link = anchors[0]['href']
            if domain == link:
                """
                    If we get a match,
                    update the rank and token,
                    and break
                """

                rank = i + 1
                token = True
                break

    return rank,token
