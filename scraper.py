from requests import get
from bs4 import BeautifulSoup

urls = ["https://www.antoloji.com/ismet-ozel/siirleri/", "https://www.antoloji.com/ismet-ozel/siirleri/ara-/sirala-/sayfa-2/", "https://www.antoloji.com/ismet-ozel/siirleri/ara-/sirala-/sayfa-3/"]
root_url = "https://www.antoloji.com"

scrape_list = {}
for url in urls:
    response = get(url)
    html_page = BeautifulSoup(response.text, 'html.parser')
    poem_container = html_page.find_all('div', attrs={'class': 'list-poem-1'})
    for poem in poem_container:
        scrape_list[poem.a['title']] = poem.a['href']
print(scrape_list)

for title in scrape_list:
    response = get(f"{root_url}{scrape_list[title]}") # returns href
    html_page = BeautifulSoup(response.text, 'html.parser')
    verse_container = html_page.find('div', attrs={'class': 'pd-text'}).findAll('p')
    # print(verse_container)
    with open(f"toplu.txt", "a", encoding='utf-8') as f:
        for verse in verse_container:
            f.write(verse.getText().strip()) # fix blanks
        print(f"{title} done.")