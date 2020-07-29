import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd

def read_from_file(file):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.\
                    from_json_keyfile_name(
                    'client_secret.json', scope)

    client = gspread.authorize(creds)

    # Find the workbook by name and open the first sheet
    sheet = client.open(file).sheet1

    #Converting the data in sheet to dataframe
    dataframe = pd.DataFrame(sheet.get_all_records())

    #Filtering only the required first 2 columns
    domain_list = dataframe.iloc[:,0]
    keyword_list = dataframe.iloc[:, 0]

    #Zipping up the data
    req_data = zip(domain_list,keyword_list)

    return req_data,dataframe, sheet


def update_data(sheet,sheet_data):
    sheet.update([sheet_data.columns.values.tolist()] + sheet_data.values.tolist())