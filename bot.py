import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is Ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the best server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command(name = "ping", description = "sends pong")
async def ping(ctx):
    await ctx.send('Pong!!!')

@client.command(name = "copycat", description = "copies message and prints")
async def copycat(ctx, *args):
    await ctx.send(' '.join(args))

@client.command(name = "yomama", description = "sends random yo mama joke"
async def yomama(ctx):
    url = "https://api.yomomma.info/"
    res  = requests.get(url)
    res_json = res.json()
    joke = res_json["joke"]
    await ctx.send(joke)

client.run('ODY4ODc0ODgzODc3MTgzNTA5.YP2Ayw.JRxgqUr0siOBmzI22MhCFVstmtg')

