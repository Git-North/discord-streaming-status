import discord
from discord.ext import commands

token = "TOKEN_HERE"

bot = commands.Bot(command_prefix = "123456789")

print('type the the thing you are gonna stream here')
status = input(' > ')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/n__rth'
    )
    print('Streaming: ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)    
