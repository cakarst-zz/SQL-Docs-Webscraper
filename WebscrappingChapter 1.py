from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('https://docs.microsoft.com/en-us/sql/t-sql/data-types/date-transact-sql?view=sql-server-ver15')
html = urlopen('https://docs.microsoft.com/en-us/sql/t-sql/data-types/bit-transact-sql?view=sqlallproducts-allversions')

bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.prettify())

TokenList = bs.find_all('token')

# print(bs.find('token'))

# for i in TokenList:
    # print('+'*50)
    # print(i)


with open('doc_links.txt', 'w') as file_object:
    file_object.write(link)

