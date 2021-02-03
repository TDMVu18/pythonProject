import os
import requests
import codecs

def thumuc(name):
    os.mkdir(name)
    os.chdir(name)


def taofile(url, i):
    file = codecs.open('file' + str(i) + '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()

def luufile(history, count):
    for (i, url_con) in enumerate(history):
        if i >= count:
            break
        taofie(url_con, i)
        print(f'{i} {url_con}')

def main():
    thumuc('v')
    taofile('https://baomoi.com/', 2)

if __name__ == "__main__":
    main()