from funcs.push_game import PushGame
import discord
from discord.ext import commands

class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
class User:
    def __init__(self, id) -> None:
        self.id = id
        self.state = 'chat'
        self.pushGame = PushGame()

users = []
        
def checkUser(user_id):
    exists = False
    for user in users:
        if user.id == user_id:
            exists = True
            break
    if not exists:
        users.append(User(user_id))
        
        
def getUser(user_id):
    for user in users:
        if user.id == user_id:
            return user