from core.classes import CogExtension, checkUser
from funcs.scrapping import scrapeImage
from funcs.apis import getBs
import discord
from discord.ext import commands
from core.classes import CogExtension
from core.classes import users

class Fun(CogExtension):
            
    @commands.command()
    async def pic(self, ctx, search_term):
        pic = scrapeImage(search_term)
        await ctx.send(pic)
        
    @commands.command()
    async def bs(self, ctx, topic):
        await ctx.send(getBs(topic))

    @commands.command()
    async def say(self, ctx, msg):
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(msg)
        
    @commands.command()
    async def enterPushGame(self, ctx):
        checkUser(ctx.message.author.id)
        for user in users:
            if user.id == ctx.message.author.id:
                user.state = 'pushGame'
                break
        await ctx.send('PushGame Started!')

        


def setup(bot):
    bot.add_cog(Fun(bot))
            