import discord
import random
import datetime
import traceback
import aiohttp
import asyncio
from discord import opus
import async_timeout
from random import randint
from discord.ext import commands
from discord.utils import find
from asyncio import sleep
import logging
import time
import os
import json

start_time = time.time()
with open("data/config.json", "r") as f:
    kek = json.load(f)
    
bot = commands.Bot(command_prefix=kek['prefix'])
logging.basicConfig(level='INFO')
bot.remove_command('help')
bot.load_extension("cogs.admin")
bot.load_extension("cogs.api")
bot.load_extension("cogs.mineswepper")
    
@bot.event
async def on_guild_join(guild):
    print (f"+1 {guild.name}| ID {guild.id}")
    em = discord.Embed(title=f"+1 server (Total: {len(bot.guilds)})", color=0xe67e22)
    em.add_field(name="Name Server", value=guild.name, inline=True)
    em.add_field(name="ID", value=guild.id, inline=True)
    em.add_field(name="Owner Server", value=guild.owner, inline=True)
    em.add_field(name="Members", value=guild.member_count, inline=True)
    em.add_field(name="New members on the bot", value=len(bot.users), inline=True)
    em.set_thumbnail(url=guild.icon_url)
    em.timestamp = datetime.datetime.utcnow()
    await bot.get_guild(489498283194974210).get_channel(520218875493744660).send(embed=em)
    
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('**Thanks for added me! <a:ablobdancewhite:464794007755685898>\nMy prefix is `,` Use `,help` for list commands!\nSo if you found a bug/glitch command(s) or have a question about this bot, use `,support` for join our support server! Enjoy!** :hugging:')
   

@bot.event
async def on_guild_remove(guild):
    print (f"-1 {guild.name}| ID {guild.id}")
    em = discord.Embed(title=f"-1 server (Total: {len(bot.guilds)})", color=0xe67e22)
    em.add_field(name="Name Server", value=guild.name, inline=True)
    em.add_field(name="ID", value=guild.id, inline=True)
    em.add_field(name="Owner Server", value=guild.owner, inline=True)
    em.add_field(name="Members", value=guild.member_count, inline=True)
    em.add_field(name="New members on the bot", value=len(bot.users), inline=True)
    em.set_thumbnail(url=guild.icon_url)
    em.timestamp = datetime.datetime.utcnow()
    await bot.get_guild(489498283194974210).get_channel(520218875493744660).send(embed=em)
    
@bot.listen()
async def on_member_remove(member):
    if member.guild.id == 464783042310045707:
        em = discord.Embed(color=discord.Colour.red())
        em.add_field(name='Goodbye!', value=f"<a:Leave:503203313076928518> {member.mention}", inline=False)
        em.add_field(name='Info', value='Ne-a parasit... Speram sa revii, esti mereu bine venit :sob:', inline=False)
        em.set_thumbnail(url=member.avatar_url)
        await bot.get_guild(464783042310045707).get_channel(464783042310045709).send(embed=em)
    if member.guild.id != 464783042310045707:
        return

@bot.listen()
async def on_member_join(member):
    if member.guild.id == 464783042310045707:        
        em = discord.Embed(color=discord.Colour.green())
        em.add_field(name='Welcome', value=f"<a:Join:503203359097094154> {member.mention}", inline=False)
        em.add_field(name='Info', value='Nu uita sa citesti <#464789280368230400> inainte de a scrii pe chat!\n**Nu poti sa scrii aici? Intra pe <#532601194670063619> si apasa pe reactia.**', inline=False)
        em.set_thumbnail(url=member.avatar_url)
        await bot.get_channel(464783042310045709).send(embed=em)
    if member.guild.id != 464783042310045707:
        return

@bot.event
async def on_ready():
 print('Logged in as')
 print(bot.user.name)
 print(bot.user.id)
 print("Discord.py API version:", discord.__version__)

@bot.listen()
async def on_command_error(ctx, error):
    print(f'\'{ctx.author}\' used command \'{ctx.command}\' on \'{ctx.guild.name} and got this error: \n{error}')
    em = discord.Embed(title=f"Error!", color=discord.Color.red())
    em.add_field(name="Command name", value=ctx.command, inline=False)
    em.add_field(name="User", value=ctx.author, inline=True)
    em.add_field(name="User ID", value=ctx.author.id, inline=True)
    em.add_field(name="Channel name", value=ctx.channel.name, inline=True)
    em.add_field(name="Channel ID", value=ctx.channel.id, inline=True)
    em.add_field(name="Server name", value=ctx.guild.name, inline=True)
    em.add_field(name="Server ID", value=ctx.guild.id, inline=True)
    em.add_field(name="Error:", value=error, inline=False)
    em.timestamp = datetime.datetime.utcnow()
    await bot.get_guild(489498283194974210).get_channel(530107395247177740).send(embed=em)
    if isinstance(error, commands.CommandOnCooldown):
        return await ctx.send(f':no_entry:  | This command is on cooldown... **[{int(error.retry_after)} seconds]**', delete_after=5)
    if isinstance(error, commands.NotOwner):
        return await ctx.send('<:RaluvyWarning:489805114224410625> | **You do not own this bot!**')
    if isinstance(error, commands.BadArgument):
        return await ctx.send(f'<:RaluvyError:489805076118896690> | **{error}**')
    if isinstance(error, commands.MissingPermissions):
        return await ctx.send('<:RaluvyForbidden:489805084650110976> | **You are missing permission to execute this command!**')
    if isinstance(error, commands.BotMissingPermissions):
        return await ctx.send('<:RaluvyForbidden:489805084650110976> | **I am missing permission to perform this command!**')


@bot.listen()
async def on_message(message):
    if message.content.lower() == '<@489061565430235136>' and message.author != bot.user:
        await message.channel.send('**My prefix is `,` | Use `,help` for show commands.**')
    else:
        await bot.process_command(message)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def invite(ctx):
    await ctx.send("""**You can add me here ->** http://bit.ly/InviteRaluvyBot""")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def vote(ctx):
    await ctx.send("**Vote me for more commands ->** https://discordbots.org/bot/489061565430235136/vote")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def hug(ctx, member: discord.Member=None):
    with open("data/hug.json", "r") as f:
        res = json.load(f)
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"Hugs {member.name}!", color=0xe67e22)
      em.set_image(url=(random.choice(res['hug'])))
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kiss(ctx, member: discord.Member=None):
    with open("data/kiss.json", "r") as f:
        res = json.load(f)
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"Awwww!", color=0xe67e22)
      em.set_image(url=(random.choice(res['kiss'])))
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def poke(ctx, member: discord.Member=None):
    with open("data/poke.json", "r") as f:
        res = json.load(f)
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"Poke! :3", color=0xe67e22)
      em.set_image(url=(random.choice(res['poke'])))
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def pat(ctx, member: discord.Member=None):
    with open("data/pat.json", "r") as f:
        res = json.load(f)
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"Pats {member.name}! :3", color=0xe67e22)
      em.set_image(url=(random.choice(res['pat'])))
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def slap(ctx, member: discord.Member=None):
    with open("data/slap.json", "r") as f:
        res = json.load(f)
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"* Slaps {member.name} *", color=0xe67e22)
      em.set_image(url=(random.choice(res['slap'])))
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)
    
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def lick(ctx, member: discord.Member=None):
    with open("data/lick.json", "r") as f:
        res = json.load(f)
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"* Licks {member.name} *", color=0xe67e22)
      em.set_image(url=(random.choice(res['lick'])))
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)
    
@bot.command(aliases=['flipcoins'])
async def flipcoin(ctx):
    a = (ctx.author.mention)
    msg = await ctx.send('Flipping...')
    await asyncio.sleep(1.5)
    await msg.edit(content=random.choice([f"{a}, **Heads!**", f"{a}, **Tails!**"]))


@bot.group()
@commands.cooldown(1, 5, commands.BucketType.user)
async def lenny(ctx):
    if ctx.invoked_subcommand is None:
        return await ctx.send('( ͡° ͜ʖ ͡°)')

@lenny.command()
async def help(ctx):
    await ctx.send('```Help lenny\n\nOriginal - ( ͡° ͜ʖ ͡°)\nHug - (つ ͡° ͜ʖ ͡°)つ\nAttack - (∩ ͡ ° ʖ ͡ °) ⊃-(===>\nFliptable - ( ͡° ͜ʖ ͡°) ╯︵ ┻─┻\nGlasses - ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ\nLove - ( ͡♥ 3 ͡♥)```')

@lenny.command()
async def original(ctx):
    await ctx.send('( ͡° ͜ʖ ͡°)')

@lenny.command()
async def hug(ctx):
    await ctx.send('(つ ͡° ͜ʖ ͡°)つ')

@lenny.command()
async def fliptable(ctx):
    await ctx.send('( ͡° ͜ʖ ͡°) ╯︵ ┻─┻')

@lenny.command()
async def attack(ctx):
    await ctx.send('(∩ ͡ ° ʖ ͡ °) ⊃-(===>')

@lenny.command()
async def glasses(ctx):
    await ctx.send('ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ')

@lenny.command()
async def love(ctx):
    await ctx.send('( ͡♥ 3 ͡♥)')

@bot.command()
async def xd(ctx, message=None):
    if message is None:
        return await ctx.send("Please put a message...")
    a=message
    await ctx.send(f'```{a}           {a}    {a} {a}\n  {a}       {a}      {a}    {a}\n    {a}   {a}        {a}     {a}\n       {a}            {a}     {a}\n    {a}   {a}        {a}     {a}\n  {a}       {a}      {a}    {a}\n{a}           {a}    {a} {a}```')

@bot.command()
async def logo(ctx, *, text):
    if len(text)>18:
         return await ctx.send("**Your text is too long!** Try again.")
    a = random.choice(['scoobydoo','cnn', 'starWars', 'yahoo', '43things', 'batman', 'SpiderMan', 'harrypotter', 'army', 'blazed', '101puppies'])
    em = discord.Embed(colour=discord.Colour.blue(), title='Your custom logo:')
    brand = text.replace(" ","%20")
    em.set_image(url=f'http://createfunnylogo.com/logo/{a}/{brand}.jpg')
    await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command(aliases=['howgay'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def gay(ctx, member: discord.Member=None):
     a = random.randint(0, 101)
     if member is None:
            member = (ctx.author)
     embed = discord.Embed(color=0xe67e22)
     embed.add_field(name=f"Is {member.name} gay?", value=f"**{a}%** gay! :gay_pride_flag:", inline=False)
     await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def sayd(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)


@bot.command(aliases=['emoji_info', 'emoji info'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def emojiinfo(ctx, emoji: discord.Emoji):
    await ctx.send(f'`Name:` {emoji.name}\n`ID:` {emoji.id}\n`Preview:` {emoji} (`{emoji}`)\n`URL:` {emoji.url}\n`Created at:` {emoji.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")}')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def doge(ctx, *message):
    if message is None:
            return await ctx.send("**Please put a message to run this command!**")
    if message is not None:
            i = ('http://dogr.io/' + '/'.join(message) + '/.png?split=false')
            em = discord.Embed(title="Wow, much doge, such amazing!", color=0xe67e22)
            em.set_image(url=i)
            em.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=em)

@bot.command(aliases=['cursed-images', 'cursedimage', 'cursedimages', 'cursed-image'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def cursed(ctx):
     with open("data/cursed.json", "r") as f:
        res = json.load(f)
        gay = random.choice(res['image'])
     embed = discord.Embed(title="Random Cursed Images", color=discord.Color.green())
     embed.set_image(url=gay)
     embed.timestamp = datetime.datetime.utcnow()
     await ctx.send(embed=embed)
                   
@bot.command(aliases=['mc', 'minecraft'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def achievement(ctx, *message):
    if message is None:
            return await ctx.send("**Please put a message to run this command!**")
    if message is not None:
            i = ('https://www.minecraftskinstealer.com/achievement/a.php?i=1&h=Achievement+get%21&t=' + '+'.join(message))
            em = discord.Embed(title="", color=0xe67e22)
            em.set_image(url=i)
            await ctx.send(embed=em)


@bot.command(aliases=['google'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def search(ctx, *, query):
    search = query
    URL = 'https://www.google.com/search?q='
    words = search.split(" ")
    num = 0
    for w in words:
        if num is 0:
            URL = URL + w
            num = 1
        else:
            URL = URL + "+"+ w
    await ctx.send(URL)


@bot.command(aliases= ["number"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def randomnumber(ctx, *, digits:int=1):
    number = ""
    for i in range(digits):
        number += str(random.randint(0, 100))
    await ctx.send(f":1234: | **Your random number is `{number}`!**")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def space(ctx, *, message=None):
    if message is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Hey, please use `,space [message]`!**')
    await ctx.send(' '.join(message))

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def clap(ctx, *, message=None):
    if message is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Hey, please use `,clap [message]`!**')
    await ctx.send(':clap:'.join(message))

@bot.command(aliases=['roll', 'rolls', 'dic'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def dice(ctx):
    a = (random.choice(['1', '2', '3', '4', '5', '6']))
    await ctx.send(f":game_die: | **I rolled a `{a}`!**")          
                   
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def parrot(ctx, *, message=None):
    if message is None:
        return await ctx.send('<a:parrot:491311653884002304>')
    await ctx.send('<a:parrot:491311653884002304>'.join(message))

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def owo(ctx, *, message=None):
    if message is None:
        return await ctx.send("**OwO! What's this?**")
    await ctx.send(f"""**OwO! {message}**""")
                           
@bot.command(aliases=['slot'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def slots(ctx):
       t = await ctx.send('Spinning...')
       await asyncio.sleep(1)
       a = (random.choice(['------------------\n:soccer: : :tangerine: : :chocolate_bar:\n:potato: : :chocolate_bar: : :watermelon:<\n:tangerine: : :soccer: : :seven:\n------------------\n\n**You Lose! :(**', '------------------\n:soccer: : :tangerine: : :seven:\n:chocolate_bar: : :chocolate_bar: : :chocolate_bar:<\n:soccer: : :watermelon: : :seven:\n------------------\n\n**You Win! :D**', '------------------\n:chocolate_bar: : :soccer: : :potato:\n:seven: : :seven: : :seven:<\n:soccer: : :chocolate_bar: : :watermelon:\n------------------\n\n**You Win! :D**', '------------------\n:chocolate_bar: : :potato: : :soccer:\n:potato: : :tangerine: : :seven:<\n:soccer: : :chocolate_bar: : :tangerine:\n------------------\n\n**You Lose! :(**'])) 
       await t.edit(content=a)
    

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def wumpus(ctx, *, message=None):
    if message is None:
        return await ctx.send('<a:aWumpus:479223216796336148>')
    await ctx.send('<a:aWumpus:479223216796336148>'.join(message))

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def blobdance(ctx, *, message=None):
    if message is None:
        return await ctx.send('<a:blobdance:535801229050118164>')
    await ctx.send('<a:blobdance:535801229050118164>'.join(message))

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def respect(ctx):
    em = discord.Embed(title="", description="", color=discord.Colour.blue())
    em.set_author(name="")
    em.add_field(name=f"{ctx.author.name}", value='Press :regional_indicator_f: to pay respect', inline=True)
    msg = await ctx.send(embed=em)
    await msg.add_reaction('\N{regional indicator symbol letter f}')


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def choose(ctx, option1, option2):
    a = [option1, option2]
    if option1 == option2:
        return await ctx.send("<:RaluvyError:489805076118896690> | **I can't choose the same things ;-;**") 
    await ctx.send(f':thinking: | {ctx.author.mention}, i choose **' + random.choice(a) + '** !')

    

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def emoji(ctx):
    await ctx.send(random.choice(bot.emojis))
                   
@bot.command(aliases=['emojiavatar', 'iconemoji', 'avataremoji'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def emojiicon(ctx, emoji: discord.Emoji):
    em = discord.Embed(color=discord.Colour.orange())
    em.set_image(url = f"{emoji.url}")
    await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    t = await ctx.send(':ping_pong: | Pong!, Calculating...')
    await asyncio.sleep(1)
    await t.edit(content=f':ping_pong: | **Pong!** `{ctx.bot.latency * 1000:,.0f}MS`')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def shrug(ctx):
    await ctx.send("¯\_(ツ)_/¯")


@bot.command(name='8ball')
@commands.cooldown(1, 5, commands.BucketType.user)
async def lball(ctx, question = None):
        if question is None:
                return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please put a question!**')
        if question is not None:
                await ctx.send(random.choice(['● It is certain.', '● It is decidedly so.', '● Without a doubt.', '● Yes - definitely.', '● You may rely on it', '● As I see it, yes.', '● Most likely.', '● Outlook good.', '● Yes.', '● Signs point to yes.', '● Reply hazy, try again', '● Ask again later.', '● Better not tell you now.', '● Cannot predict now.', '● Concentrate and ask again.', '● Don`t count on it.', '● My reply is no.', '● My sources say no', '● Outlook not so good.', '● Very doubtful.' ]))
                

@bot.command(aliases=['jesus'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def jesussay(ctx, *, message=None):
    if message is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please put the message what jesus says.**')
    embed=discord.Embed(color=0xd2cd68)
    embed.set_thumbnail(url="https://i.kym-cdn.com/entries/icons/facebook/000/009/556/jesus-bleu-mauve.jpg")
    embed.add_field(name="Jesus says", value=message, inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@bot.command(aliases= ["sinfo", "server info", "server_info"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def serverinfo(ctx):
    c = 0
    a = 0
    g = 0
    online = 0
    idle = 0
    dnd = 0
    n = ctx.guild.member_count
    for i in ctx.guild.members:
     if i.bot is True:
      c+=1
    for i in ctx.guild.members:
     if i.bot is False:
      a+=1
    for i in ctx.guild.members:
      if i.status.name == 'online':
          online += 1
      if i.status.name == 'idle':
          idle += 1
      if i.status.name == 'dnd':
          dnd += 1
      g = online + idle + dnd
    em = discord.Embed(color=discord.Colour.orange())
    em.add_field(name='Name', value=f'{ctx.author.guild.name}', inline=True)
    em.add_field(name='Owner', value=f'{ctx.author.guild.owner.mention} [{ctx.author.guild.owner.id}]', inline=True)
    em.add_field(name='Icon', value='Type `,servericon`', inline=True)
    em.add_field(name='Verification level', value=ctx.guild.verification_level, inline=True)
    em.add_field(name='Roles', value=f'{len(ctx.guild.roles)} `,sroles`', inline=True)
    em.add_field(name='Text Channels', value=f'{len(ctx.guild.channels)}', inline=True)
    em.add_field(name='Voice', value=f'{len(ctx.guild.voice_channels)}', inline=True)
    em.add_field(name='Members', value=f'{n}', inline=True)
    em.add_field(name='Bots', value=f'{c}', inline=True)
    em.add_field(name='People', value=f'{a}', inline=True)
    em.add_field(name='Online', value=f'{g}', inline=True)
    em.add_field(name='Created at', value=ctx.guild.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=True)
    em.add_field(name='Region', value=ctx.guild.region, inline=True)
    em.set_thumbnail(url=ctx.guild.icon_url)
    em.set_footer(text=f'ID: {ctx.guild.id}')
    em.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=em)


@bot.command(aliases =['sicon'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def servericon(ctx):
    em = discord.Embed(title="", color=discord.Colour.blue())
    em.set_author(name=f"{ctx.guild.name}'s icon")
    em.set_image(url=ctx.guild.icon_url)
    em.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=em)

@bot.command(aliases=['sroles'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def serverroles(ctx):
    try:
         em = discord.Embed(color=discord.Colour.blue())
         em.add_field(name=f'Server Roles [{len(ctx.guild.roles)}]', value=', '.join(g.name for g in ctx.guild.roles))
         await ctx.send(embed=em)
    except discord.HTTPException as owo:
         await ctx.send("**This server has too many roles!** Sorry! :(")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kill(ctx, member: discord.Member=None):
    if member is None:
        await ctx.send(':gun: | **You died! Tag a user to kill him/her!**')
    if member is ctx.me:
        return await ctx.send('nope.')
    if member is ctx.author:
        return await ctx.send(':gun: | **You died! Tag a user to kill him/her!**')
    if member is not None:
        await ctx.send(random.choice([f':gun: | **{ctx.author.mention} wanted to kill {member.mention} just as he stumbled and struck his head with a stone**', f':gun: | **{member.mention} died from a murderer**', f':gun: | **{member.mention} gave too much rage to Clash Royale until he fainted and died**', f':gun: | **{member.mention} was pushed by {ctx.author.mention} from the 5th floor and died**', f':gun: **{member.mention}, The pregnancy of the table just fell asleep and caught fire**', f':gun: | **{member.mention} was shot by {ctx.author.mention}**', f':gun: **After a hard attempt to kill him {member.mention} , {ctx.author.mention} was arrested**']))

@bot.command(aliases=['about', 'info', 'botinfo'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def stats(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
                   
    embed = discord.Embed(title="Stats Bot", color=0xe67e22)
    embed.add_field(name="<:RaluvyUsers:489805123191701504> Total Users", value=len(bot.users), inline=True)
    embed.add_field(name="<:RaluvyServers:489805145757188097> Total Servers", value=len(bot.guilds), inline=True)
    embed.add_field(name=":crown: Owner Bot", value=f"<@390540063609454593>", inline=True)
    embed.add_field(name="Uptime", value=text, inline=True)
    embed.add_field(name="Commands", value=len(ctx.bot.commands), inline=True)
    embed.add_field(name='Created at', value=ctx.me.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
    embed.add_field(name="Library", value="<:RaluvyPython:489805100420694016> discord.py", inline=True)
    embed.add_field(name="Discord.py API Version", value=discord.__version__, inline=True)
    embed.set_thumbnail(url=ctx.me.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Thank you for using Raluvy <3')
        
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    await ctx.send(text)

@bot.command(aliases=['role-info'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def roleinfo(ctx, role: discord.Role=None):
     if role is None:
          return await ctx.send(f"**Ops... Try again with role mention or role name!**")
     if role.mentionable is True:
          mention = "Yes"
     else:
          mention = "No"
     if role.hoist is True:
          hoist = "Yes"
     else:
          hoist = "No"
     embed = discord.Embed(title=role.name, color=role.color)
     embed.add_field(name="Created at", value=role.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=True)
     embed.add_field(name="Mentionable", value=mention, inline=True)
     embed.add_field(name="ID", value=role.id, inline=True)
     embed.add_field(name="Color", value=role.color, inline=True)
     embed.add_field(name="Members in this role", value=len(role.members), inline=True)
     embed.add_field(name="Displayed separately", value=hoist)
     await ctx.send(embed=embed)



@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, message=None):
        try:
             if member is None:
                  return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,kick <member>`!**")
             else:
                  if member is ctx.author:
                       return await ctx.send("<:RaluvyError:489805076118896690> | **I can't kick you! ;-;**")
                  if member.guild_permissions.administrator is True:
                       return await ctx.send("<:RaluvyError:489805076118896690> | **I don't kick because that user is a Administrator permission**")
                  if message is None:
                       await member.kick(reason=f"Requested by {ctx.author}")
                  else:
                       try:
                          await member.kick(reason=f"{message} | {ctx.author}")
                       except:
                          await member.kick(reason=f"Requested by {ctx.author}")
        except discord.Forbidden as owo:
             return await ctx.send(f"Ops... I can't kick because\n`{owo}`")

@bot.command()
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member = None, *, message=None):
        try:
             if member is None:
                  return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,softban <member>`!**")
             else:
                  if member is ctx.author:
                       return await ctx.send("<:RaluvyError:489805076118896690> | **I can't softban you! ;-;**")
                  if member.guild_permissions.administrator is True:
                       return await ctx.send("<:RaluvyError:489805076118896690> | **I don't softban because that user is a Administrator permission**")
                  if message is None:
                       await member.ban(reason=f"Requested by {ctx.author}")
                       await member.unban()
                  else:
                       try:
                          await member.ban(reason=f"{message} | {ctx.author}")
                          await member.unban()
                       except:
                          await member.ban(reason=f"Requested by {ctx.author}")
                          await member.unban()
        except discord.Forbidden as owo:
             return await ctx.send(f"Ops... I can't kick because\n`{owo}`")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, message=None):
        try:
             if member is None:
                  return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,ban <member>`!**")
             else:
                  if member is ctx.author:
                       return await ctx.send("<:RaluvyError:489805076118896690> | **I can't ban you! ;-;**")
                  if member.guild_permissions.administrator is True:
                       return await ctx.send("<:RaluvyError:489805076118896690> | **I don't ban because that user is a Administrator permission**")
                  if message is None:
                       await member.ban(reason=f"Requested by {ctx.author}")
                  else:
                       try:
                          await member.ban(reason=f"{message} | {ctx.author}")
                       except:
                          await member.ban(reason=f"Requested by {ctx.author}")
        except discord.Forbidden as owo:
             return await ctx.send(f"Ops... I can't kick because\n`{owo}`")                   
                   
@bot.command(aliases=['nickname'])
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member=None, *, uwu):
     try:
          if uwu == "remove":
              await member.edit(nick=member.name)
              return await ctx.message.add_reaction('\U00002705')
          if member is not None and uwu is not None:
              await member.edit(nick=f'{uwu}')
              return await ctx.send("Done! :white_check_mark: ")
          if member is not None and uwu is None:
              return await ctx.send(":x: Please use `,nick <mention> <new nick> [remove]`")
          if member is None and uwu is None:
              return await ctx.send(":x: Please use `,nick <mention> <new nick> [remove]`")
     except discord.Forbidden as owo:
          return await ctx.send(f"**Ops... I can't change because:**\n`{owo}`")
        
        
@bot.group(aliases=['rank'])
@commands.has_permissions(manage_roles=True)
async def role(ctx):
    if ctx.invoked_subcommand is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please, use** `,role [add/remove] [role] [membru]`')

@role.command()
@commands.has_permissions(manage_roles=True)
async def add(ctx, role: discord.Role, member: discord.Member):
    await member.add_roles(role)
    await ctx.send(f'<:RaluvySucces:489805130963615754> | **I added the rank `{role}` to `{member}`!**')
    
@role.command()
@commands.has_permissions(manage_roles=True)
async def remove(ctx, role: discord.Role, member: discord.Member):
    await member.remove_roles(role)
    await ctx.send(f'<:RaluvySucces:489805130963615754> | **I removed the rank `{role}` to `{member}`!**')

@bot.command(aliases=['prune'])
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, number: int):
    if number>200:
        return await ctx.send("<:RaluvyError:489805076118896690> **Too many numbers! Try again!**")
    await ctx.message.delete()
    await ctx.channel.purge(limit=number)
        
        

        
    
        
@bot.command(aliases=['av'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def avatar(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    em = discord.Embed(description=f'{member.mention}\'s [avatar]({member.avatar_url})', color=discord.Colour.blurple())
    em.set_image(url=member.avatar_url)
    await ctx.send(embed=em)
        
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def membercount(ctx):
    c = 0
    a = 0
    online = 0
    idle = 0
    dnd = 0
    offline = 0
    tonline = 0
    tidle = 0
    tdnd = 0
    toffline = 0
    n = ctx.guild.member_count
    for i in ctx.guild.members:
     if i.bot is True:
      c+=1
    for i in ctx.guild.members:
     if i.bot is False:
      a+=1
    for i in ctx.guild.members:
      if i.status.name == 'online':
          online += 1
      if i.status.name == 'idle':
          idle += 1
      if i.status.name == 'dnd':
          dnd += 1
      if i.status.name == 'offline':
          offline += 1
    for i in ctx.guild.members:
     if i.bot is False:
      if i.status.name == 'online':
          tonline += 1
      if i.status.name == 'idle':
          tidle += 1
      if i.status.name == 'dnd':
          tdnd += 1
      if i.status.name == 'offline':
          toffline += 1
      g = online + idle + dnd
      tg = tonline + tidle + tdnd
    ts = f"{tg}\n<:online:536240817602560010> Online - **{tonline}**\n<:dnd:536240817531125760> DND - **{tdnd}**\n<:idle:536240817522868224> Idle - **{tidle}**\n<:offline:536240817552228385> Offline - **{toffline}**"
    s = f"{g}\n<:online:536240817602560010> Online - **{online}**\n<:dnd:536240817531125760> DND - **{dnd}**\n<:idle:536240817522868224> Idle - **{idle}**\n<:offline:536240817552228385> Offline - **{offline}**"
    em = discord.Embed(color=discord.Colour.orange())
    em.add_field(name='Members', value=f'{n}', inline=True)
    em.add_field(name='Bots', value=f'{c}', inline=True)
    em.add_field(name='People', value=f'{a}', inline=True)
    em.add_field(name='Members Online', value=f'{s}', inline=True)
    em.add_field(name='People Online', value=f'{ts}', inline=True)
    em.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=em)

        
@bot.command(aliases= ["whois", "uinfo", "playerinfo", "user-info"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def userinfo(ctx, member: discord.Member=None):
    if member is None:
            member = (ctx.author)
    if member.bot is True:
          a = "Yes, he's a bot! :robot:"
    if member.bot is False:
          a = "No, he's not a bot! :grinning:"
    if member.status.name == 'online':
          b = "<:online:536240817602560010> Online"
    if member.status.name == 'idle':
          b = "<:idle:536240817522868224> Idle"
    if member.status.name == 'dnd':
          b = "<:dnd:536240817531125760> DND"
    if member.status.name == 'offline':
          b = "<:offline:536240817552228385> Offline"
    if member.activity is None:
          c = 'This user is not playing yet'
    if member.activity is not None:
          c = ctx.author.activity.name
    embed = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
    embed.set_author(name="Who is?")
    embed.add_field(name="Name", value=member.name)
    embed.add_field(name="Is this a bot?", value=a)
    embed.add_field(name="Status", value=b)
    embed.add_field(name="Playing", value=c)
    embed.add_field(name="Tag", value=member.discriminator)
    embed.add_field(name="Top Role", value=member.top_role)
    embed.add_field(name="Nick", value=member.nick)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
    embed.add_field(name="Created at", value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
    embed.add_field(name="Roles", value=', '.join(g.name for g in member.roles))
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'ID: {member.id}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)


        
@bot.command(hidden=True, aliases=['set_playing', 'set playing'])
async def setplaying(ctx, *, message = None):
    if message is None:
        return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please put message what's playing bot...**")
    await bot.change_presence(activity=discord.Game(name=f"{message} || ,help"))
    await ctx.send("<:RaluvySucces:489805130963615754>", delete_after=2)                   
                   
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def support(ctx):
    em = discord.Embed(title="", description="", color=discord.Colour.green())
    em.add_field(name='Join our support server!', value='[here]( https://discord.gg/bazhjYQ )')
    await ctx.send(embed=em)

@bot.command(aliases=['h'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    await ctx.message.add_reaction("\N{WHITE HEAVY CHECK MARK}")
    embed = discord.Embed(title=f"All commands (Total: {len(ctx.bot.commands)})", description="Visit our [website]( http://raluvybot.coolpage.biz/ ) for more information about the commands!\nMore question? Join [Support Server!]( https://discordapp.com/invite/bazhjYQ )", color=0xe67e22)
    embed.add_field(name="<a:ablobdancewhite:464794007755685898> Fun", value="`8ball`  `gay`  `dice`  `slots`  `xd`  `choose`  `dogfact`   `mineswepper`  `catfact`  `emoji`  `respect`  `kill`", inline=False)
    embed.add_field(name=":ok: Text", value="`lenny`  `shrug`  `blobdance`  `jesussay`  `clap`  `sayd`  `say`  `space`  `owo`  `wumpus`  `parrot`", inline=False)
    embed.add_field(name=":hammer:  Moderation", value="`kick`  `ban`  `nickname`  `softban`  `purge`  `role`", inline=False)
    embed.add_field(name=":mountain_snow:  Images", value="`lick`  `slap`  `pat`  `shiba`  `cat`  `dog`  `hug`  `cursed`  `pika`  `achievement`  `meme`  `kiss`  `doge`  `logo`", inline=False)
    embed.add_field(name=":information_source: Info", value="`emojiinfo`  `roleinfo`  `membercount`  `serverinfo`  `pokemon`  `userinfo`  `stats`", inline=False)
    embed.add_field(name=":pushpin: Utility", value="`ping`  `uptime`  `vote`  `randomnumber`  `flipcoin`  `avatar`  `support`  `emojiavatar`  `search`  `invite`", inline=False)
    embed.set_footer(text='Use , before using commands')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.author.send(embed=embed)

async def presence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        a = 0
        for i in bot.guilds:
            for u in i.members:
                if u.bot == False:
                    a = a + 1

        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="i like cookies || ,help"))
        await sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=",invite || ,help"))
        await sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="Noice || ,help"))
        await sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.users)} users || ,help"))
        await sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers || ,help"))
        await sleep(30)
        

bot.loop.create_task(presence())
bot.run(os.getenv("TOKEN"))
