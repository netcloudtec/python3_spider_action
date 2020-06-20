# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 下载第一章内容
    # target = "https://www.xsbiquge.com/15_15338/8549128.html"
    # req = requests.get(url=target)
    # req.encoding = 'utf-8'
    # html = req.text
    # bs = BeautifulSoup(html, 'lxml')
    # texts = bs.find('div', id='content')
    # print(texts)
    # print(texts.text.strip().split('\xa0'*4))

    # 下载整本小说
    server = 'https://www.xsbiquge.com'
    target = 'https://www.xsbiquge.com/15_15338/'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    chapters = bs.find('div', id='list')
    chapters=chapters.find_all('a')
    for chapter in chapters:
        url=chapter.get('href')
        print(chapter)
        print(server+url)


