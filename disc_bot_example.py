
import discord

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


# i think that was right XD
    if message.content.startswith('!rekt'):
        msg = 'You\'re a fucking loser {0.owner}'.format(message)
        await client.send_message(message.channel, msg)



async def random_status();
    status = ["Sucking titties","Getting money","Shitting pants"]
    me = discord.utils.find(lambda s: s != None, client.servers).me
    if not me:
        return
    elif not me.game:
        updated_game = discord.game(name = random.choice(status))
    else:
        updated_game = me.game
        updated_game.name = random.choice(status)
    await client.change_presence(game = updated_game)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
