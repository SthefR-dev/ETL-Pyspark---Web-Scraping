import requests
from bs4 import BeautifulSoup


URL = "https://www.imdb.com/calendar/?region=PE&type=MOVIE"
def get_pag_content():
    #Encabezados de indentificación
    headers = {
        'User-Agent':'Mozilla/5.0' #
    }
    
    response = requests.get(URL, headers=headers)
    print(response.status_code)
    # print(response.text)
    if response.status_code ==200:
        return response.text
    return None

def create_pag_file_local(content):
    try:
        with open('imdb.html', 'w') as file:
            file.write(content)
    except:
        pass
    
def get_pag_file_local(content):
    content = None
    
    try:
        with open('imdb.html', 'r') as file:
            content = file.read()
    except:
        pass
    return content

def get_local_pag_content():
    content = get_pag_file_local()
    if content:
        return content
    content = get_pag_content()
    create_pag_file_local(content)
    
    return content
    
    
def temp():
    content = get_pag_content()
    
    soup = BeautifulSoup(content,'html.parser')
    
    #print (soup)
    
    li_tags = soup.find_all('li', {
        'data-testid': 'coming-soon-entry',
        'class': 'ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click sc-8c2b7f1f-0 dKSSmX'
    })
    
    for tag in li_tags:
        print(tag, '\n')
    
    
   
if __name__ == '__main__':
   temp()
        