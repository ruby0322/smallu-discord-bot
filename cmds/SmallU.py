from funcs.others import report
from core.classes import CogExtension
from funcs.apis import getServerSpeed
import discord
from discord.ext import commands
from core.classes import CogExtension
from consts import cle
from consts import be

class SmallU(CogExtension):
            
    @commands.command()
    async def repo(self, ctx):
        await ctx.send(embed=report())

    @commands.command()
    async def cmdl(self, ctx):
        await ctx.send(embed=cle)
    
    @commands.command()
    async def bult(self, ctx):
        await ctx.send(embed=be)
    
    @commands.command()
    async def spdtst(self, ctx):
        await ctx.send(embed=getServerSpeed())


def setup(bot):
    bot.add_cog(SmallU(bot))
            