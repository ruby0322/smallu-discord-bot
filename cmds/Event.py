from re import I
from typing import get_type_hints
from funcs.apis import *
from funcs.others import *
from funcs.scrapping import *
from core.classes import CogExtension, checkUser, getUser
import discord
from discord.ext import commands
from core.classes import CogExtension
from consts import welcome_channel_id
from consts import leave_channel_id
from consts import cle
from consts import be


def adjustCommand(command):
    if command[0] == ' ':
        return command[1:]
    else:
        return command


class Event(CogExtension):
                
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Online')
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(welcome_channel_id)
        await channel.send(f'{member} joined!')
        
    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = self.bot.get_channel(leave_channel_id)
        await channel.send(f'{member} leaved!')
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        user_id = msg.author.id
        checkUser(user_id)
        content = msg.content
        if getUser(user_id).state == 'chat':
            if content[:2] == '小幽':
                try:
                    command = adjustCommand(content[2:])
                except:
                    await msg.channel.send('小幽在! 怎麼啦?')
                    return 
                if command[:1] == '說':
                    try:
                        await msg.delete()
                    except:
                        pass
                    await msg.channel.send(adjustCommand(command[1:]))
                elif command[:1] == '算':
                    await msg.channel.send(calculate(adjustCommand(command[1:])))
                elif command[:1] == '查':
                    await msg.channel.send(embed=googleThis(adjustCommand(command[1:]), '"zh-TW"'))
                elif command[:2] == '抽圖':
                    await msg.channel.send(scrapeImage(adjustCommand(command[2:])))
                elif command[:2] == '測速':
                    await msg.channel.send(embed=getServerSpeed())
                elif command[:2] == '清除':
                    await msg.channel.purge()
                elif command[:2] == '唬爛':
                    await msg.channel.send(getBs(adjustCommand(command[2:])))
                elif command[:2] == '公告':
                    await msg.channel.send(embed=be)
                elif command[:2] == '疫情':
                    await msg.channel.send(embed=scrapeCovid())
                elif command[:2] == '科普':
                    await msg.channel.send(randomWiki())
                elif command[:2] == '天氣':
                    await msg.channel.send(embed=getWeatherEmbed(adjustCommand(command[2:])))
                elif command[:2] == '回報':
                    await msg.channel.send(embed=report())
                elif command[:3] == '指令集':
                    await msg.channel.send(embed=cle)
                elif command[:3] == '推箱子':
                    getUser(user_id).state = 'pushGame'
                    await msg.channel.send('```歡迎遊玩推箱子```')
                    await msg.channel.send(embed=getUser(user_id).pushGame.Renderer())
        elif getUser(user_id).state == 'pushGame':
            command = content
            if command == '離開':
                getUser(user_id).state = 'chat'
                getUser(user_id).pushGame.level = 1
                getUser(user_id).pushGame.newLevel()
                await msg.channel.send('```感謝遊玩```')
            else:
                if command == 'w' or command == 'W':
                    getUser(user_id).pushGame.update('up')
                elif command == 'a' or command == 'A':
                    getUser(user_id).pushGame.update('left')
                elif command == 's' or command == 'S':
                    getUser(user_id).pushGame.update('down')
                elif command == 'd' or command == 'D':
                    getUser(user_id).pushGame.update('right')

                await msg.channel.send(embed=getUser(user_id).pushGame.Renderer())

            
def setup(bot):
    bot.add_cog(Event(bot))
            