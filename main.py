import os
import discord, json
import time
import requests 
from datetime import datetime
from discord.ext import commands

prefix = '$'

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

os.system('title Auto Bumperis $start by Robke96#9780')

@bot.event
async def on_ready():
    print(f'Pasirink savo kanalą ir parašyk komandą: {prefix}start')

@bot.command()
async def start(ctx):
    await ctx.message.delete()
    while True:
        print('Naudojama komandą !d bump | Laikas:', current_time)
        await ctx.send('!d bump')
        time.sleep(7200)


bot.run(token, bot=False)
