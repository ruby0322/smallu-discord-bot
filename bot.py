import os
from discord.ext import commands
from consts import *


#################################################################

bot = commands.Bot(command_prefix=command_prefix)

####################### Commands #########################

for f in os.listdir('./cmds'):
    if f.endswith('.py'):
        bot.load_extension(f'cmds.{f[:-3]}')
            
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} loaded.')
    
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} unloaded.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} reloaded.')

############################################################

# if __name__ == '__main__':
bot.run(TOKEN)

