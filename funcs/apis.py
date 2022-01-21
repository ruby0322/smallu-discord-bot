from datetime import datetime
import discord
from discord.embeds import Embed
import requests
import json
from speedtest import Speedtest
def getBs(topic):

    data = json.dumps({"Topic": topic, "MinLen": 30})

    response = requests.post(
        "https://api.howtobullshit.me/bullshit", data=data).text.replace('&nbsp;', '').replace('<br>', '\n')

    return f'```{response}```'

def getWeatherData(city):
    token = 'CWB-C51B7DEE-3270-4070-BF82-96B301D60283'
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=' + \
        token + '&format=JSON&locationName=' + str(city)
    Data = requests.get(url)
    Data = (json.loads(Data.text)
            )['records']['location'][0]['weatherElement']
    res = [[], [], []]
    for j in range(3):
        for i in Data:
            res[j].append(i['time'][j])
    return res

def getWeatherEmbed(city):
        city = city.replace('台', '臺')
        res = getWeatherData(city)
        embed=discord.Embed(title=f'__**{city}未來36小時天氣預報**__', url='https://www.cwb.gov.tw/V8/C/W/County/index.html', description="```資料來源: 中央氣象局```", timestamp=datetime.utcnow())
        embed.set_thumbnail(url='https://i.imgur.com/Mm8U6i6.jpg')
        
        count = 0
        
        for data in res:
            
            embed.add_field(name='**=========時段=========**', value=f"{res[count][0]['startTime'][5:-3].replace('-', '/').replace(' ', ', ')} ~ {res[count][0]['endTime'][5:-3].replace('-', '/').replace(' ', ', ')}", inline=False)
            embed.add_field(name='```天氣狀況```', value=f"*{data[0]['parameter']['parameterName']}*", inline=True)
            embed.add_field(name='```溫度```', value=f"*{data[2]['parameter']['parameterName']} ~ {data[4]['parameter']['parameterName']} °C*", inline=True)
            embed.add_field(name='```降雨機率```', value=f"*{data[1]['parameter']['parameterName']} %*", inline=True)
            
            count += 1

        embed.set_footer(text='詳細內容請參閱標題連結')
        return embed

def getServerSpeed():
    st = Speedtest()
    download_speed = round(st.download() / (1024 ** 2))
    upload_speed = round(st.upload() / (1024 ** 2))
    embed=Embed(title="```[Heroku伺服器]```", description='```測速結果如下```')
    embed.add_field(name='```下載速度```', value=f'*{download_speed} Mbps*', inline=True)
    embed.add_field(name='```上傳速度```', value=f'*{upload_speed} Mbps*', inline=True)
    
    return embed