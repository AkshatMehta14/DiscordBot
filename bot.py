import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is Ready')

client.run('ODY4ODc0ODgzODc3MTgzNTA5.YP2Ayw.NRmrr4JtsApI0UxoIbWiS6NfC08')
