from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import time

def find_link_metadata (link):
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("headless")
    driver = Edge(options = options)

    row_dict = {}
    row_dict['title'] = ''
    row_dict['Is_link_broken'] = 0
    row_dict['Is_SQL_Server'] = 0
    row_dict['Is_SQL_DB'] = 0
    row_dict['Is_SQL_MI'] = 0
    row_dict['Is_Synapse'] = 0
    row_dict['Is_PDW'] = 0
    row_dict['Is_Other'] = 0
    row_dict['author'] = ''
    row_dict['updated_at'] = '2000-01-01 01:01 PM'
    row_dict['link']=link

    try:
        html = urlopen(link)
    except HTTPError as e:
        row_dict.update(Is_link_broken = 1)
        return row_dict
    except ValueError as v:
        print("invalid Link")
        return None
    except:
        return None
    driver.get(link)
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    # print(bs.prettify())
    # print('*' * 1000)

    row_dict = {}
    row_dict['title'] = ''
    row_dict['Is_link_broken'] = 0
    row_dict['Is_SQL_Server'] = 0
    row_dict['Is_SQL_DB'] = 0
    row_dict['Is_SQL_MI'] = 0
    row_dict['Is_Synapse'] = 0
    row_dict['Is_PDW'] = 0
    row_dict['Is_Other'] = 0
    row_dict['author'] = ''
    row_dict['updated_at'] = '2000-01-01 01:01 PM'
    row_dict['link']=link

    try:
        html = urlopen(link)
    except HTTPError as e:
        row_dict.update(Is_link_broken = 1)
        return row_dict

    try:
        title= bs.find('title')
        row_dict.update(title = title.text)
    except AttributeError as e:
        row_dict.update(title = 'Unable To Find')

    try:
        tokens = bs.find_all('token')
        services = []
        for token in tokens:
            services.append(token.text)

        for i in services:
            if i == 'SQL Server (all supported versions) ':
                row_dict.update(Is_SQL_Server = 1)
            elif i == 'Azure SQL Database':
                row_dict.update(Is_SQL_DB= 1)
            elif i == 'Azure SQL Managed Instance':
                row_dict.update(Is_SQL_MI = 1)
            elif i == 'Azure Synapse Analytics':
                row_dict.update(Is_Synapse = 1)
            elif i == 'Parallel Data Warehouse':
                row_dict.update(Is_PDW = 1)
            else:
                row_dict.update(Is_Other = 1)
    except AttributeError as e:
        row_dict.update(Is_SQL_Server = -1)
        row_dict.update(Is_SQL_DB= -1)
        row_dict.update(Is_SQL_MI = -1)
        row_dict.update(Is_Synapse = -1)
        row_dict.update(Is_PDW = -1)
        row_dict.update(Is_Other = -1)

    try:
        meta = bs.find_all('meta')
        for i in meta:
            if i.get('name') =='ms.author':
                row_dict.update(author=i.get('content'))
            if i.get('name') =='updated_at':
                row_dict.update(updated_at= i.get('content'))
    except AttributeError as e:
        row_dict.update(author='Unkown')
        row_dict.update(updated_at= '1900-01-01')

    return row_dict


rows = []

with open('Small_Links','r') as links:
    for link in links:
        row_dict = find_link_metadata(link)
        if row_dict != None:
            rows.append(row_dict)
            print(row_dict)

table = pd.DataFrame.from_records(rows)

print(table.to_string())
table.to_excel('output.xlsx')