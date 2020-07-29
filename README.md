# Web Crawler

This program aims to generate the rank of a website as per the keyword provided during Google search

# Prerequisites

You need Python 3.7 or above

## Setting API key

To create your application's **API** **key**:

1.Go to the [API Console](https://console.developers.google.com/apis/dashboard?project=web-crawler-276005)

2.From the projects list, select a project or create a new one.

3.If the APIs & services page isn't already open, open the left side menu and select APIs & services.

4.On the left, choose Credentials.

5.Click Create credentials and then select API key.

## Setting Virtual Environment

**virtualenv** is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

To create a **virtual** **environment** follow the steps given [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

* Installing Virtualenv

On macOS and Linux:

`python3 -m pip install --user virtualenv`

On Windows:

`py -m pip install --user virtualenv`

* Creating a virtual environment

On macOS and Linux:

`python3 -m venv env`

On Windows:

`py -m venv env`

* Activating a virtual environment

On macOS and Linux:

`source env/bin/activate`

On Windows:

`.\env\Scripts\activate`

* Leaving the virtual environment

`deactivate`

* Installing packages

Packages necessary are mentioned in requirements.txt file.Now that you’re in your virtual environment you can install packages necessary using the following command:

`pip install -r requirements.txt`

## google_search_ranker.py

This is the main file to be executed in order to save the ranks in the google sheet.

# Description of the functions used in the code


**timer**

A decorator used to calculate the time of execution of the code.


**read_from_file(file)**

Takes file name as input and reads the domain name and keywords from the file.

**update_data(sheet,sheet_data)**

Updates the domain along with present rank as per google search and in the *sheet* with new *sheet_data* 


**web_scrapper(parameters)**

Takes in the *parameters* i.e the domain and keyword to hit the url and crawl the google search page to get the present rank of the domain.

**current_time()**

This function returns the current date and time.


**searching_ranks(data)**

This funtion searches the page for current rank of the domain as per the keyword.


**hit_server(url)**
 
This function sends a get request to the server using user agent.

**get_bs4_data(content)**

Running the html content through BeautifulSoup gives us a BeautifulSoup object
which represents the document as a nested data structure.
 
 **string_search(domain, soup)**
 
This function scrapes out data from google search engine results 
and arranges it into native python lists.


If the link matches with the domain then 
it returns respective rank and token for that domain.

# Authors

* Shirshendu Dhar
* Soumi Chatterjee
* Sukanya Mukherjee 

Mentors 

* Nauman Arif
* Sayema Fatema

