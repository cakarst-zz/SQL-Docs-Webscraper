from bs4 import BeautifulSoup
html_source = '''
    <div>
       <p class="test1">hello world</p>
        <p class="test2"hello world</p>
         <p class="test3">hello world</p>
          <p class="test4">hello world</p>
    </div>   
'''

soup = BeautifulSoup(html_source, 'html.parser')
find_by_class = soup.find_all(class_="test1")
print(find_by_class)