from selenium.webdriver import Edge
from bs4 import BeautifulSoup


driver = Edge('C:\\Users\\cakarst\\IdeaProjects\\Documentation Web Scrapping\\msedgedriver.exe')
driver.get('https://docs.microsoft.com//en-us//sql//t-sql//data-types//date-transact-sql?view=sql-server-ver15')

left_nav_buttons = driver.find_elements_by_class_name('tree-item')
left_nav_button = []
left_nav_button.append(driver.find_element_by_class_name('tree-item'))
page_source = driver.page_source

def click_buttons(buttonList):
    for x in range(len(buttonList)):
        if buttonList[x].is_displayed() and buttonList[x].get_attribute('aria-expanded') == "false":
            driver.execute_script("arguments[0].click();", buttonList[x].find_element_by_class_name('tree-expander'))
            child_list = buttonList[x].find_elements_by_class_name('tree-item')
            print(child_list)
            click_buttons(child_list)
    page_source = driver.page_source

    # click_buttons((new_button_list))
    # time.sleep(1)
    # i+=1
    # print(i)

click_buttons(left_nav_buttons)



bs = BeautifulSoup(page_source, 'html.parser')
html_link = bs.find_all("a")
print(page_source)
print('*' * 50 )
print(bs.prettify())
print('*' * 50 )
print(html_link)
# links = []
# for link in html_link:
#     L_index_location = link.find('href=') + 6
#     R_index_location = link[L_index_location:].find('"')
#     single_link = link[L_index_location:]
#     single_link = link[:R_index_location]
#
#     links.append(single_link)

with open('doc_links.txt', 'w') as file_object:
    for i in html_link:
        file_object.writelines(str(i))

