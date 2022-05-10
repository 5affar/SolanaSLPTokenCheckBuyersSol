from asyncio.windows_events import NULL
from gettext import NullTranslations
from time import sleep
import webbrowser
import discord
import tokenscraper
import threading
import requests
import json

content = ""

TOKEN = 'Add bot token here'

address = []
solana = []


client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    
    callandrequest = user_message.split(" ")

    print(f'{username}: {user_message} ({channel})')
    print(callandrequest[0])

    if message.author == client.user:
        return

    #!tokeninfo listner

    if callandrequest[0].lower() == '!tokeninfo':

        await message.channel.send(f'{message.author.mention} Tracking token: {callandrequest[1]}')
        
        while True:

          sleep(3)

          if callandrequest[0].lower() == '!end':

            break
            

          else:
            address,solana = tokenscraper.Scraper(callandrequest[1])
            
            for i in range(len(address)):

              await message.channel.send(f'**{address[i-1]}** - {solana[i-1]} SOL')

        return





client.run(TOKEN)

