'''
Created on Oct 24, 2018

@author: Aaron
'''

# Work with Python 3.6
import random
import asyncio
from discord import Game
from discord.ext.commands import Bot
from random import randrange

BOT_PREFIX = ("?", "!")
TOKEN = "NTA0ODE5MjY5MTg4NTgzNDU0.DrOlCQ.k_vjqD87-KJqVT919GgymQ7dINQ"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))
    
@client.command(name='ff',
                description="Answers a yes/no question with a fifty-fifty.",
                brief="Answers from the beyond.",
                aliases=[],
                pass_context=True)
async def ff(context):
    number = randrange(0, 2)
    if number == 1:
        await client.say("*Chick* *Chick* no! " + context.message.author.mention)
    else:
        await client.say("*CHICK* Yes! " + context.message.author.mention)

@client.command()
async def smitedan():
    for x in range(25):
        await client.say("@251489634628927489" + " ZAP!!!")
    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)