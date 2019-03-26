
import discord
# Don't need to import discord.game, included in Discord
from tokens import WA_TOKEN, DISC_TOKEN
import wolframalpha

WA_client = wolframalpha.Client(WA_TOKEN)
TOKEN = DISC_TOKEN

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} \n'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!cmere'):
        msg = 'OMW Homie!'
        await client.send_message(message.channel, msg)
        await client.join_voice_channel(message.author.voice.voice_channel)
    if message.content.startswith('!heel'):
        # disconnect from voice client
        # work in progress
        pass
    if message.content.startswith('!play'):
        # disc needs a file to read for audio from bot
        # write audio stream to file or read direct from sound device
        # I really don't know
        pass
    if message.content.startswith('!math'):
        # wolfram aplha API functionality
        msg = "."
        res = WA_client.query(message.content[5:])
        print ('query:' , message.content[5:])
        try:
            pods = [pod for pod in res.pods]
            subs = [sub.text for sub in pods]
            msg = "\n".join(subs[:2])
        except:
            msg = "Not a valid query"

        await client.send_message(message.channel, msg)

    if message.content.startswith('!rekt'):
        msg =  '{0.author} got rekt'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
