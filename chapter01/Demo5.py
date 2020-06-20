import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.dmzj.com/view/yaoshenji/41917.html'
r = requests.get(url=url)
html = BeautifulSoup(r.text, 'lxml')
script_info = html.script
pics = re.findall('\d{13,14}', str(script_info))
chapterpic_hou = re.findall('\|(\d{5})\|', str(script_info))[0]
chapterpic_qian = re.findall('\|(\d{4})\|', str(script_info))[0]
for pic in pics:
    url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
    print(url)
