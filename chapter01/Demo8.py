import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    search_keyword = '越狱第一季'
    search_url = 'http://www.jisudhw.com/index.php'
    serach_params = {
    'm': 'vod-search'
    }
    serach_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'Referer': 'http://www.jisudhw.com/',
        'Origin': 'http://www.jisudhw.com',
        'Host': 'www.jisudhw.com'
    }
    serach_datas = {
        'wd': search_keyword,
        'submit': 'search'
    }
    r = requests.post(url=search_url, params=serach_params, headers=serach_headers, data=serach_datas)
    r.encoding = 'utf-8'
    server = 'http://www.jisudhw.com'
    search_html = BeautifulSoup(r.text, 'lxml')
    search_spans = search_html.find_all('span', class_='xing_vb4')
    for span in search_spans:
        url = server + span.a.get('href')
        name = span.a.string
        print(name)
        print(url)

    detail_url = 'http://www.jisudhw.com/?m=vod-detail-id-15409.html'
    r = requests.get(url=detail_url)
    r.encoding = 'utf-8'
    detail_bf = BeautifulSoup(r.text, 'lxml')
    num = 1
    serach_res = {}
    for each_url in detail_bf.find_all('input'):
        if 'm3u8' in each_url.get('value'):
            url = each_url.get('value')
            if url not in serach_res.keys():
                serach_res[url] = num
            print('第%03d集:' % num)
            print(url)
            num += 1
