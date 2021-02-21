from selenium.webdriver import Edge
import time
from bs4 import BeautifulSoup


driver = Edge('C:\\Users\\cakarst\\IdeaProjects\\Documentation Web Scrapping\\msedgedriver.exe')
driver.get('https://docs.microsoft.com//en-us//sql//t-sql//data-types//date-transact-sql?view=sql-server-ver15')

left_nav_buttons = driver.find_elements_by_class_name('tree-item')

def click_buttons(buttonList):
    for x in range(len(buttonList)):
        if buttonList[x].is_displayed() and buttonList[x].get_attribute('aria-expanded') == "false":
            driver.execute_script("arguments[0].click();", buttonList[x].find_element_by_class_name('tree-expander'))
            child_list = buttonList[x].find_elements_by_class_name('tree-item')
            click_buttons(child_list)
            time.sleep(.01)

#######################################################
click_buttons(left_nav_buttons)

bs = BeautifulSoup(driver.page_source, 'html.parser')
for link in bs.find_all(class_ = "tree-item is-leaf"):
    print(link.get('href'))

with open('doc_links.txt', 'w') as file_object:
    for link in bs.find_all(class_="tree-item is-leaf"):
        file_object.write(str(link.get('href') + '\r\n'))

