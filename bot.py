import discord
from discord.ext import commands
import requests
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is Ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! {client.latency} ms')

@client.command(name = "copycat", description = "copies message and prints")
async def copycat(ctx, *args):
    await ctx.send(' '.join(args))

@client.command(name = "yomama", description = "sends random yo mama joke")
async def yomama(ctx):
    url = "https://api.yomomma.info/"
    res  = requests.get(url)
    res_json = res.json()
    joke = res_json["joke"]
    await ctx.send(joke)

@client.command(name = "8ball", description = "Magic 8ball (try this: !8ball [A random question])")
async def eightBall(ctx):
    responses = ["It is certain.", "Without a doubt.", "You may rely on it.", "Yes, definitely.", "It is decidedly so.", "As I see it, yes.", "Most likely.", "Yes.", 
    "Outlook good.", "Signs point to yes", "Reply hazy try again.", "Better not tell you now.", "Ask again later.", "Cannot predict now.", "Concentrate and ask again.", 
    "Don't count on it.", "Outlook not so good.", "My sources say no.", "Very doubtful.", "My reply is no."]

    question = input("What is your question? ")
    choice = random.choice([1, 2, 3])

    if (choice == 1): await ctx.send(question+"? "+random.choice(responses[0:10]))
    elif (choice == 2): await ctx.send(question+"? "+random.choice(responses[10:15]))
    elif (choice == 3): await ctx.send(question+"? "+random.choice(responses[15:]))
    else: print("An unexpected error ocurred.")

client.run('Nzk2NDkxNzY0MDkyNjMzMTI4.X_Yswg.dOmUw99A4b2BYocAmh2LvSiB6Fo')
client.run('ODY4ODc0ODgzODc3MTgzNTA5.YP2Ayw.JRxgqUr0siOBmzI22MhCFVstmtg')
