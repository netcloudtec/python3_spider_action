import requests
import os
import re
from bs4 import BeautifulSoup
from contextlib import closing
from tqdm import tqdm
import time

if __name__ == '__main__':
    # 创建保存目录
    save_dir = '妖神记'
    if save_dir not in os.listdir('./'):
        os.mkdir(save_dir)
    target_url = "https://www.dmzj.com/info/yaoshenji.html"
    # 获取动漫章节链接和章节名
    r = requests.get(url=target_url)
    # 解析
    bs = BeautifulSoup(r.text, 'lxml')
    list_con_li = bs.find('ul', class_="list_con_li")
    # 找到所有的 超链接 a
    cartoon_list = list_con_li.find_all('a')
    chapter_names = []  # 存储超链接的章节名称
    chapter_urls = []  # 存储超链接的 herf 的属性值
    for cartoon in cartoon_list:
        href = cartoon.get('href')
        name = cartoon.text
        # 集合中插入元素 每次遍历都是插入到第一个index中 因为目录是从后往前排的
        chapter_names.insert(0, name)
        chapter_urls.insert(0, href)
    # 下载漫画 tqdm添加下载进度
    for i, url in enumerate(tqdm(chapter_urls)):
        download_header = {
            'Referer': url
        }
        name = chapter_names[i]
        # 去掉.
        while '.' in name:
            name = name.replace('.', '')
        chapter_save_dir = os.path.join(save_dir, name)# 路径拼接
        if name not in os.listdir(save_dir):
            os.mkdir(chapter_save_dir)
            # 获取具体章节的url
            r = requests.get(url=url)
            html = BeautifulSoup(r.text, 'lxml')# 解析
            script_info = html.script
            #re.findall 正则表达式 匹配到数字13 或者14次
            pics = re.findall('\d{13,14}', str(script_info))
            for j, pic in enumerate(pics):
                if len(pic) == 13:
                    pics[j] = pic + '0'
            pics = sorted(pics, key=lambda x: int(x))
            chapterpic_hou = re.findall('\|(\d{5})\|', str(script_info))[0]
            chapterpic_qian = re.findall('\|(\d{4})\|', str(script_info))[0]
            for idx, pic in enumerate(pics):
                if pic[-1] == '0':
                    url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic[:-1] + '.jpg'
                else:
                    url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
                pic_name = '%03d.jpg' % (idx + 1)
                pic_save_path = os.path.join(chapter_save_dir, pic_name)
                # 解绝反爬
                with closing(requests.get(url, headers=download_header, stream=True)) as response:
                    chunk_size = 1024
                    content_size = int(response.headers['content-length'])
                    if response.status_code == 200:
                        with open(pic_save_path, "wb") as file:
                            for data in response.iter_content(chunk_size=chunk_size):
                                file.write(data)
                    else:
                        print('链接异常')
            time.sleep(10)
