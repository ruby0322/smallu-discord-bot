from funcs.apis import getWeatherEmbed
from funcs.others import calculate
from core.classes import CogExtension
from funcs.scrapping import *
from funcs.others import *
import discord
from discord.ext import commands
from core.classes import CogExtension

class Useful(CogExtension):
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Bot\'s ping: { str(round(self.bot.latency * 1000) } ms')

    @commands.command()
    async def covid(self, ctx):
        await ctx.send(embed=scrapeCovid())
        
    @commands.command()
    async def cal(self, ctx, equation):
        await ctx.send(calculate(equation))

    @commands.command()
    async def search(self, ctx, search_term):
        await ctx.send(embed=googleThis(search_term, 'us'))
        
    @commands.command()
    async def weather(self, ctx, city):
        await ctx.send(embed=getWeatherEmbed(city=city))
        
    

def setup(bot):
    bot.add_cog(Useful(bot))
            