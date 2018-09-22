
import discord
import discord.game
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
    if message.content.startswith('!c\'mere'):
        msg = 'OMW Homie!'
        await client.send_message(message.channel, msg)
        channels_list = [channel for channel in message.server.channels if channel.type is ChannelType.voice]
        for i in channels_list:
            try:
                await client.join_voice_channel(i)
                break
            except:
                pass
    if message.content.startswith('!heel'):
        pass

# i think that was right XD
    if message.content.startswith('!rekt'):
        msg = 'You\'re a fucking loser {0.owner}'.format(message)
        await client.send_message(message.channel, msg)



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
            await ev.bot.change_presence(game=game)
        except Exception as e:
            ev.log.error(f'STATUS ROTATION FAILED: {e}')
        await asyncio.sleep(60)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
