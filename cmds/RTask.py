import discord
from discord.ext import commands
from core.classes import CogExtension
import asyncio
from consts import task_channel_id

class RTask(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Task Cog Loaded')
        self.tasking = False
        self.interval = 5
        
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(task_channel_id)
            while not self.bot.is_closed():
                if self.tasking:
                    await self.channel.send('Tasking')
                    print('iterated')
                await asyncio.sleep(self.interval)
                
        self.bg_task = self.bot.loop.create_task(interval())
        
    @commands.command()
    async def rtask_ch(self, ctx, ch):
        try:
            ch = int(ch)
            self.channel = self.bot.get_channel(ch)
            await ctx.send(f'Task target-channel has been set to {self.channel.mention}.')
        except:
            await ctx.send('Input must be an interger number.')
        
    @commands.command()
    async def toggle_rtask(self, ctx):
        self.tasking = not self.tasking
        await ctx.send(f"Task toggled, currently {str(self.tasking)}.")
        
    @commands.command()
    async def rtask_intv(self, ctx, new_interval):
        try:
            self.interval = float(new_interval)
            await ctx.send(f"Interval set, currently {self.interval}.")
        except:
            await ctx.send(f"Input must be a number.")
            
                        
def setup(bot):
    bot.add_cog(RTask(bot))