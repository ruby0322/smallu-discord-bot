from re import L
import requests
import random
from bs4 import BeautifulSoup
from discord import Embed
import validators

class Unsplash:
    def __init__(self,search_term,per_page=20,quality="regular"):
        self.search_term = search_term
        self.per_page = per_page
        self.page = 0
        self.quality = quality
        self.headers = {
            "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":	"gzip, deflate, br",
            "Accept-Language":	"en-US,en;q=0.5",
            "Host":	"unsplash.com",
            "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
        }

    def set_url(self):
        return f"https://unsplash.com/napi/search/photos?query={self.search_term}&xp=&per_page={self.per_page}&page={self.page}"

    def make_request(self):
        url = self.set_url()
        return requests.request("GET",url,headers=self.headers)

    def get_data(self):
        self.data = self.make_request().json()

    def Scrapper(self,pages):
        result_urls = []
        for page in range(pages+1):
            try:
                self.make_request()
                self.get_data()
                for item in self.data['results']:
                    url = item['urls'][self.quality]
                    result_urls.append(url)
                    # self.data['results'].remove(url)
            except:
                pass
            self.page += 1
        
        return result_urls


def scrapeImage(search_term):
    scrapper = Unsplash(search_term=search_term)
    results = scrapper.Scrapper(3)
    return random.choice(results)


def scrapeCovid():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    res = requests.get('https://covid-19.chinatimes.com/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E,%E5%8F%B0%E7%81%A3', headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    main = soup.find('div', class_='row covid19')
    cases = main.find_all('span', class_='number-high-light') 
    date_div = main.find('div', class_='col-lg-12 title')
    date = date_div.find('h6').text
    total_cases = cases[0].text
    new_cases = cases[1].text
    total_deaths = cases[2].text
    new_deaths = cases[3].text
    cities = soup.find_all('span', class_='city')
    new_local_cases = soup.find_all('div', class_='badge badge-light')
    local = []
    for index in range(len(cities)):
        struct = []
        struct.append(cities[index].text)
        struct.append(new_local_cases[index].text)
        local.append(struct)
    
    embed=Embed(title='```台灣疫情即時資訊```', url='https://covid-19.chinatimes.com/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E,%E5%8F%B0%E7%81%A3', description='```資料來源: 衛福部疾管署```')
    embed.set_thumbnail(url='https://i.imgur.com/EhrBz3t.jpg')
    embed.add_field(name='**[累計數據]**', value=date, inline=False)
    embed.add_field(name='```確診人數```', value=f'*{total_cases}*', inline=True)
    embed.add_field(name='```死亡人數```', value=f'*{total_deaths}*', inline=True)
    embed.add_field(name='**[今日數據]**', value=date, inline=False)
    embed.add_field(name='```確診人數```', value=f'*{new_cases}*', inline=True)
    embed.add_field(name='```死亡人數```', value=f'*{new_deaths}*', inline=True)
    
    embed.add_field(name='**[本土案例]**', value='分布如下:', inline=False)
    local_count = 0
    for region in local:
        if int(region[1][1:]) > 0:
            embed.add_field(name=f'```{region[0]}```', value=f'*{region[1]}*', inline=True)
            local_count += int(region[1][1:])
    
    embed.add_field(name='```總計```', value=f'*{str(local_count)}*', inline=True)
    
    return embed    


def randomWiki():
    url = "https://zh.wikipedia.org/wiki/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    rq = requests.get(url, headers=headers)
    soup = BeautifulSoup(rq.text, 'lxml')
    header = soup.find('div', id='content')
    body = soup.find('div', id='bodyContent')

    title = header.find('h1', id='firstHeading').text
    content = body.find(
        'div', class_='mw-parser-output').find('p').text.replace(' ', '')
    link = 'https://zh.wikipedia.org/wiki/' + title

    return '```ini\n本次主題: ' + title + '\n```\n```apache\n' + content + '詳細內容:```\n' + link


def googleThis(search_term, hl):
    url = "https://www.google.com/search"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    params = {
        "q": search_term,
        "hl": hl,
        "ie": "UTF-8"
    }
    rq = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(rq.text, 'lxml')
    soup = soup.find('div', id='search')

    
    embed=Embed(title='```\n[' + search_term + '的搜尋結果]\n```', description='資料來源: Google')
    embed.set_thumbnail(url='https://i.imgur.com/DolWAqJ.png')
    
    results = soup.find_all('div', class_='g')
    for result in results:
        try:
            embed.add_field(name=((result.find('h3', 'LC20lb DKV0Md').text) if len(result.find('h3', 'LC20lb DKV0Md').text) <= 256 else (
                        result.find('h3', 'LC20lb DKV0Md').text[:253] + '...')) if len(result.find('h3', 'LC20lb DKV0Md').text) > 0 else '無標題', value=((result.find('div', 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc').text) if len(result.find('div', 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc').text) <= 1024 else (
                        result.find('div', 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc').text[:1021] + '...')) if len(result.find('div', 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc').text) > 0 else ('無敘述'), inline=False)
            link = result.find('a')['href']
            if validators.url(link):
                embed.add_field(name='```造訪網站```', value=link, inline=False)
            else:
                embed.add_field(name='無法造訪', value='讀取失敗', inline=False)
        except:
            continue
        
    return embed


def scrapeNews():
    
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    url = 'https://udn.com/news/breaknews/1'
    res = requests.get(url, headers)
    soup = BeautifulSoup(res.text, 'lxml')
    content = soup.find('div', class_='context-box__content story-list__holder story-list__holder--full')
    first_news = content.find('div', class_='story-list__news')
    return first_news