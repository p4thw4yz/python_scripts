# Python Discord BOT
# author - n3wdr
# Simple python discord bot to get anyone started with creating there own custom
# discord bot, this can also be used to intergrate other features and programs into you discord server.

import discord

DISCORD_TOKEN = "DISCORD_TOKEN_FROM_DEVELOPER_PORTAL"

#--------------------------------FUNCTIONS---------------------------------#
def getQuote():
    quote = 'Trying to think of some good ones!'
    return quote

def getHelp():
    return 'Commands: #help, #quote'
#--------------------------------------------------------------------------#


#-----------------------------------MAIN-----------------------------------#
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    messageContent = message.content
    print(messageContent)
    response = ''

    if message.author == client.user:
        return
    if ('#help') in messageContent: 
        response = getHelp()
    elif ('#quote') in messageContent: 
        response = getQuote()   
    elif ('hi') in messageContent.lower() or ('hello') in messageContent.lower() or ('hey') in messageContent.lower():
        response = ('Hello World!')

    await message.channel.send(response)

client.run(DISCORD_TOKEN)
