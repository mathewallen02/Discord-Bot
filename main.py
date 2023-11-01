import os
import openai
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

openAiKey = os.getenv("OPENAIKEY")

#Defines what the bot is allowed to do
#Gives bot privileged abilites such as reading message content
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#Prints a command to terminal that confirms that bot is online
@client.event
async def on_ready():
    print('Bot Online')

#Function that gets a response from openAI based on a user query 
def generate_response(query):
    openai.api_key = openAiKey
    response = openai.Completion.create(
        model = "gpt-3.5-turbo", 
        prompt = query
    )
    print(response)

    return response.choices[0].text

#Message handler
@client.event
async def on_message(message: str):
    #returns if message is posted by the bot itself
    if message.author == client.user:
        return  

    #prints message to console
    print(message.content)

    #takes user message and gets a response from open ai
    query = message.content
    response = generate_response(query)
    await message.channel.send(response)

#runs bot 
client.run(os.getenv("TOKEN"))
