import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = "https://www.dmzj.com/info/yaoshenji.html"
    re = requests.get(url=target)
    bs = BeautifulSoup(re.text, 'lxml')
    list_con_li = bs.find('ul', class_="list_con_li")
    comic_lsit = list_con_li.find_all('a')
    chapter_name = []
    chapter_urls = []
    for comic in comic_lsit:
        href = comic.get('href')
        name = comic.text
        chapter_name.insert(0, name)
        chapter_urls.insert(0, href)
    print(chapter_name)
    print(chapter_urls)
