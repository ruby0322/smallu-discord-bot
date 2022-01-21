from funcs.scrapping import scrapeNews
import discord
from discord.ext import commands
import datetime
from core.classes import CogExtension
from discord import Embed
import asyncio
from consts import news_channel_id


def Scrapper(self):
    recent_news = scrapeNews()
    link = 'https://udn.com' + recent_news.find('h2').find('a')['href']
    thumbnail = 'https://udn.com' + recent_news.find('a')['href']
    description = recent_news.find('p').find('a').text
    title = recent_news.find('a').text
    datePublished = recent_news.find('time').text
    views = recent_news.find('span').text
    
    if self.prev_news_link == link:
        return None
    self.prev_news_link = link
    
    embed=discord.Embed(title=title, url=link, description=description)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name="觀看次數", value=views, inline=True)
    embed.set_footer(text=datePublished)
                
    embed = Embed()
    
    
    return embed


class News(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Task Cog Loaded')
        self.tasking = True
        self.prev_news_link = None
        
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(news_channel_id)
            while not self.bot.is_closed():
                if self.tasking:
                    print('Tasking News')
                    recent_news = scrapeNews()
                    link = 'https://udn.com' + recent_news.find('h2').find('a')['href']
                    thumbnail = recent_news.find('img')['data-src']
                    description = recent_news.find('p').find('a').text
                    title = recent_news.find('h2').text
                    datePublished = recent_news.find('time').text
                    views = recent_news.find('span').text
                    
                    
                    embed=Embed(title=title, url=link, description=description)
                    embed.set_thumbnail(url=thumbnail)
                    embed.add_field(name="觀看次數", value=views, inline=True)
                    embed.set_footer(text=datePublished)
                                
                    if self.prev_news_link != link:
                        try:
                            await self.channel.send(embed=embed)
                            print('Gotit')
                            self.prev_news_link = link
                        except:
                            print('Exception caught')
                            self.prev_news_link = link                    
                await asyncio.sleep(5)
                
        self.bg_task = self.bot.loop.create_task(interval())
        
        
    

    
        
    @commands.command()
    async def news_ch(self, ctx, ch):
        try:
            ch = int(ch)
            self.channel = self.bot.get_channel(ch)
            await ctx.send(f'Task target-channel has been set to {self.channel.mention}.')
        except:
            await ctx.send('Input must be an interger number.')
        
    @commands.command()
    async def toggle_news(self, ctx):
        self.tasking = not self.tasking
        await ctx.send(f"Task toggled, currently {str(self.tasking)}.")
        
            
                        
def setup(bot):
    bot.add_cog(News(bot))