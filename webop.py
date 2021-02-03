import requests
from bs4 import BeautifulSoup
import re

def doc_noi_dung(url):
    raw_page = requests.get(url)
    content = BeautifulSoup(raw_page.text, 'html.parser')
    return content


def lay_cac_duong_link(content, url):
    atag = content('a', attrs={'href': True})
    result = []
    for i in atag:
        lk = i['href']
        mau = f'^{url}[^?#]*$'
        mau2 = '^/[^?#]*$'
        if re.match(mau, lk):
            result.append(lk)
        else:
            if re.match(mau2, lk):
                link = f'{url}{lk}'
                result.append(link)
    return result


def countlink(cache, url, count):
    history = cache
    while (len(cache) > 0) and (len(history) < count):
        url_tim_duoc = lay_cac_duong_link(cache.pop(), url)
        cache = cache | (url_tim_duoc - history)
        history = history | url_tim_duoc
    return history


def main():
    links = doc_noi_dung('http://vnexpress.vn')
    url_tim_duoc = lay_cac_duong_link(links, 'http://vnexpress.vn')
    history = countlink(url_tim_duoc, 'http://vnexpress.vn', 1000)
    for i in history:
        print(i)


if __name__ == '__main__':
    main()