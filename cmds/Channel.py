from core.classes import CogExtension
from funcs.scrapping import *
from funcs.others import *
import discord
from discord.ext import commands
from core.classes import CogExtension

class Channel(CogExtension):
        
    @commands.command()
    async def cls(self, ctx):
        await ctx.channel.purge()
        
    @commands.command()
    async def cl(self, ctx, lim=2):
        await ctx.channel.purge(limit=lim)


def setup(bot):
    bot.add_cog(Channel(bot))
            