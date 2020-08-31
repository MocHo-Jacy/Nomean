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
    soup = BeautifulSoup(demo, 'html.parser')
    l = soup('ol', attrs={'class': 'grid_view'})
    for i in l[0]('li'):
        try:
            numo = i('em', attrs={'class': ''})[0]
            title = i('span', attrs={'class': 'title'})[0]
            urls = i('a', attrs={'class', ''})[0]['href']
            print('{0:<5}\t{1:{3}<30}\t{2:<}'.format(numo.string, title.string, urls, chr(12288)))
        except:
            print('')

def main():
    nums = 0
    for i in range(10):
        nums = i*25
        new_url = 'https://movie.douban.com/top250?start=' + str(nums) + '&filter='
        demo = getHTML(new_url)
        sortHTML(demo)

main()
