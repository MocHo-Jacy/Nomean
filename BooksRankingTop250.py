from bs4 import BeautifulSoup
import requests


def getHTML(url):
    try:
        r = requests.get(url, headers = {'user-agent': 'Mozilla/5.0'}, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败！')


def sortHTML(demo):
    global num
    soup = BeautifulSoup(demo, 'html.parser')
    l = soup('table', attrs={'width': '100%'})
    for i in l:
        try:
            title0 = i('a')[1]['title']
            title = '《' + title0 + '》'
            author = i('p', attrs={'class': 'pl'})[0]
            urls = i('a')[1]['href']
            if i('span', attrs={'class': 'inq'}) == []:
                quote = ''
            else:
                quote = i('span', attrs={'class': 'inq'})[0].string
            print('Top'+str(num), title, author.string, urls, quote, sep='\n')
            print('\n')
            num += 1
        except:
            print('')


num = 1
nums = 0
for i in range(10):
    nums = i*25
    new_url = 'https://book.douban.com/top250?start=' + str(nums)
    demo = getHTML(new_url)
    sortHTML(demo)
