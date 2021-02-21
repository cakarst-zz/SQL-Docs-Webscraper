from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError

link = ''
try:
    html = urlopen(link)
except HTTPError as e:
    print("link is broken")
except ValueError as v:
    print("invalid Link")
