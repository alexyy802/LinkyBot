# Linky - nextcord
# loading
print('\nLoading...')
import nextcord
import asyncio
import os
import random
import getpass
import socket
import datetime
import pytz
import json
import environ
import pymongo
environ.token()
never_gonna_give_you_up = os.getenv('TOKEN')
environ.connectDB()
conDB = os.getenv('connectDB')
u = getpass.getuser()
H = socket.gethostname()
userHost = u + '@' + H
client = nextcord.Client(intents=nextcord.Intents.all())
# connecting to db
print('Connecting to DB...')
cluster = MongoClient(conDB)
db = cluster["linkydb"]
print('Connected!\n')

# on ready
@client.event
async def on_ready():
    p = os.getenv('prefix')
    if p == None: os.environ['prefix'] = 'l!'
    p = os.getenv('prefix')
    print(f'Connected to Discord!')
    print(f'Logged in as {str(client.user)}!')
    print(f'Running on {userHost}!')
    print('')
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'{p}help'), status=nextcord.Status.online)

# on_message
@client.event
async def on_message(message):
    # to prevent lag:
    # Section a) checks if message starts with bot prefix or message is equal to bot ping
    p = os.getenv('prefix')
    p = p.lower()
    cum = client.user.mention
    cum2 = cum.replace('<@', '<@!')
    if msg.startswith(p) or msg == cum or msg == cum2: pass
    else: return
    # Section b) checks if message is from DMs
    if message.guild == None:
       await reply('**{no} You cannot use this command in DMs!**')
       return
    
    # shortcuts
    msg = message.content
    sendmsg = message.channel.send
    author = message.author
    mention = message.author.mention
    reply = message.reply
    typing = message.channel.trigger_typing
    delete = message.delete
    wait = asyncio.sleep
    lowmsg = msg.lower()
    edit = message.edit
    react = message.add_reaction
    prefix = p
    yes = '<a:Animated_Checkmark:901803000861966346>'
    no = '<a:no:901803557014077480>'
    
    # colours
    c = nextcord.Colour
    blue = c.blue()
    blurple = c.blurple()
    brand_green = c.brand_green()
    brand_red = c.brand_red()
    dark_blue = c.dark_blue()
    dark_gold = c.dark_gold()
    dark_gray = c.dark_gray()
    dark_green = c.dark_green()
    dark_grey = c.dark_grey()
    dark_magenta = c.dark_magenta()
    dark_orange = c.dark_orange()
    dark_purple = c.dark_purple()
    dark_red = c.dark_red()
    dark_teal = c.dark_teal()
    dark_theme = c.dark_theme()
    darker_gray = c.darker_gray()
    darker_grey = c.darker_grey()
    default = c.default()
    fuchsia = c.fuchsia()
    gold = c.gold()
    green = c.green()
    greyple = c.greyple()
    light_gray = c.light_gray()
    light_grey = c.light_grey()
    lighter_gray = c.lighter_gray()
    lighter_grey = c.lighter_grey()
    magenta = c.magenta()
    red = c.red()
    teal = c.teal()
    yellow = c.yellow()
    
    
    ####################
    # start of functions define #
    
    # ping to member id
    def ping_replace(mem):
        if '<' in mem and '@' in mem and '>' in mem:
            mem = mem.replace('<', '')
            mem = mem.replace('@', '')
            mem = mem.replace('>', '')
            if '!' in mem: mem = mem.replace('!', '')
        return int(mem)
    
    # remove prefix
    def remprefix(msg):
        p = os.getenv('prefix')
        lowp = p.lower()
        if msg.startswith(p):
            msg = msg.split(p, 1)
            msg = msg.lstrip()
        elif msg.startswith(lowp):
            msg = msg.split(lowp, 1)
            msg = msg.lstrip()
        return msg
    
    # end of functions define #
    ###################
     
    # emoji servers
    emojiServers = [901800331204259870]
    if message.guild.id in emojiServers:
        is_emojiServer = True
        msg = remprefix(msg)
        elif msg == 'emojis':
            await reply('**List of emojis:**')
            for emoji in message.guild.emojis:
                await sendmsg(f'{emoji} - {emoji.id}')
                await sendmsg(f'\{emoji}')
                await sendmsg('`-------`')
     
    # if author is bot itself
    if author == client.user: return
    
    # if lowmessage starts with lowprefix
    lowprefix = prefix.lower()
    if lowmsg.startswith(lowprefix):
        # removing prefix from msg
        msg = remprefix(msg)
        
        # ''
        if msg == '':
            cServ = await client.fetch_guild(919110751103361084)
            sqd = await cServ.fetch_member(477683725673693184)
            alexy = await cServ.fetch_member(697323031919591454)
            await reply(f'''Hey! I am **Linky Bot**. Created by {sqd} and {alexy}.
My prefix is **`{p}`**.
Coded in `Python` using the `nextcord` library.
(short introduction of the bot here)
**Join the community server here: https://discord.gg/E4CDUJBUm5**''')
        
        ############
        # COMMANDS #
        ############
        
        #############################
        ### type commands below this line ###
        
        # command name
        elif msg == 'command name':
            await reply('Hmm')
        
        ### type commands above this line ###
        #############################
        else:
            if is_emojiServer and msg == 'emojis': return
            else: await reply(f'**Command `{p}{msg}` not found!**')
    
    if msg == cum or msg == cum2:
        cServ = await client.fetch_guild(919110751103361084)
        sqd = await cServ.fetch_member(477683725673693184)
        alexy = await cServ.fetch_member(697323031919591454)
        await reply(f'''Hey! I am **Linky Bot**. Created by {sqd} and {alexy}.
My prefix is **`{p}`**.
Coded in `Python` using the `nextcord` library.
(short introduction of the bot here)
**Join the community server here: https://discord.gg/E4CDUJBUm5**''')
    
    # update status lol
    guilds = len(client.guilds)
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'{guilds} servers! | {p}help'), status=nextcord.Status.online)

# logging into Linky
print('Logging into Linky...\n\n')
client.run(never_gonna_give_you_up)