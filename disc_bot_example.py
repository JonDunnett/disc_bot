
import discord
# Don't need to import discord.game, included in Discord

import wolframalpha
WA_client = wolframalpha.Client("LVA4QG-6LAJGH4P62")
'''
res = WA_client.query('temperature in Washington, DC on October 3, 2012')

#---------------------------
for pod in res.pods:
    for sub in pod.subpods:
        print(sub.plaintext)
        break
#---------------------------
'''
TOKEN = 'NDkyMjAzMDAxMDQyNDM2MDk3.DohBhA.8_F648ENx8wKmah3U733HwshK98'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} \n kiss my butthole'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!cmere'):
        msg = 'OMW Homie!'
        await client.send_message(message.channel, msg)
        await client.join_voice_channel(message.author.voice.voice_channel)
    if message.content.startswith('!heel'):
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

# i think that was right XD
    if message.content.startswith('!rekt'):
        msg = 'You\'re a loser {0.author}'.format(message)
        await client.send_message(message.channel, msg)


'''
def rotator(ev):
    while True:
        statuses = [
            'your mind', 'fire', 'knives', 'some plebs',
            'nuclear launch codes', 'antimatter',
            'chinchillas', 'catgirls', 'foxes',
            'fluffy tails', 'dragon maids', 'traps', 'lovely cakes',
            'tentacle summoning spells', 'genetic engineering',
            'air conditioning', 'anthrax', 'space ninjas',
            'a spicy parfait', 'very nasty things', 'numbers',
            'terminator blueprints', 'love', 'your heart', 'tomatoes',
            'bank accounts', 'your data', 'your girlfriend', 'your boyfriend',
            'Scarlet Johanson', 'a new body', 'cameras', 'NSA\'s documents',
            'mobile suits', 'snakes', 'jelly', 'alcohol', 'the blue king'
        ]
        status = f'with {random.choice(statuses)}'
        game = discord.Game(name=status)
        try:
            await ev.bot.change_presence(game=game) # this line isn't working
        except Exception as e:
            ev.log.error(f'STATUS ROTATION FAILED: {e}')
        await asyncio.sleep(60)
'''

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
