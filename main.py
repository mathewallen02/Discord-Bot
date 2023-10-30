import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


#declares what the bot is allowed to do
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


#confirms that bot is online
@client.event
async def on_ready():
    print('Bot Online')

#message handler
@client.event
async def on_message(message: str):
    #returns if message is posted by the bot itself
    if message.author == client.user:
        return  

    #prints message to console
    print(message.content)

    #prints repsonse
    response = 'hi'
    await message.channel.send(response)


load_dotenv()

client.run(os.getenv("TOKEN"))
