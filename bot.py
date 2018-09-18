import discord
import random
import datetime
import traceback
import aiohttp
import asyncio
import async_timeout
from random import randint
from discord.ext import commands
import logging
import os

bot = commands.Bot(command_prefix=',')
logging.basicConfig(level='INFO')
bot.remove_command('help')
bot.load_extension("cogs.admin")
bot.load_extension("cogs.api")
    
@bot.event
async def on_ready():
 print('Logged in as')
 print(bot.user.name)
 print(bot.user.id)

@bot.listen()
async def on_message(message):
    if message.content.lower() == '<@!489061565430235136>' and message.author != bot.user:
        await message.channel.send('**My prefix is `,` | Use `,help` for show commands.**')
    else:
        await bot.process_command(message)

@bot.listen()
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Type ,h or ,help | BETA"))

@bot.command()
async def invite(ctx):
    await ctx.send("""**You can add me here ->** http://bit.ly/InviteRaluvyBot""")

@bot.command()
async def servers(ctx):
    await ctx.send(f'{len(bot.guilds)} Servers!\n```py\n"' + '"\n"'.join(g.name for g in bot.guilds)+ '"```')

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command(aliases=['emoji_info'])
async def emojiinfo(ctx, emoji: discord.Emoji):
    await ctx.send(f'`Name:` {emoji.name}\n`ID:` {emoji.id}\n`Preview:` {emoji} (`{emoji}`)\n`URL:` {emoji.url}')

@bot.command(aliases=['google'])
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

@bot.command()
async def space(ctx, *, message=None):
    if message is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Hey, please use `,space [message]`!**')
    await ctx.send(' '.join(message))

@bot.command()
async def clap(ctx, *, message=None):
    if message is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Hey, please use `,clap [message]`!**')
    await ctx.send(':clap:'.join(message))

@bot.command()
async def respect(ctx):
    em = discord.Embed(title="", description="", color=discord.Colour.blue())
    em.set_author(name="")
    em.add_field(name=f"{ctx.author.name}", value='Press :regional_indicator_f: to pay respect', inline=True)
    msg = await ctx.send(embed=em)
    await msg.add_reaction('\N{regional indicator symbol letter f}')


@bot.command()
async def choose(ctx, option1, option2):
    a = [option1, option2]
    if option1 == option2:
        return await ctx.send("<:RaluvyError:489805076118896690> | **I can't choose the same things ;-;**") 
    await ctx.send(f':thinking: | {ctx.author.mention}, i choose **' + random.choice(a) + '** !')

@bot.command(aliases=['h'])
async def help(ctx):
    embed = discord.Embed(title="HELP", description="List commands", color=0xe67e22)
    embed.add_field(name="<a:ablobdancewhite:464794007755685898> Fun", value="`choose`  `emoji`  `everyone`  `respect`  `dog`  `doge`  `cat`  `kill`", inline=False)
    embed.add_field(name=":ok: Text", value="`lenny`  `hug`  `shrug`  `blobdance`  `kiss`  `rage`  `unflip`  `tableflip`  `love`  `momsay`  `jesussay`  `clap`  `say`  `space`  `here`  `owo`  `wumpus`  `parrot`", inline=False)
    embed.add_field(name=":hammer:  Moderation", value="`kick`  `ban` `softban` `purge`  `role`", inline=False)
    embed.add_field(name=":information_source: Info", value="`emoji_info`  `serverinfo`  `userinfo`  `stats`", inline=False)
    embed.add_field(name=":pushpin: Utility", value="`ping`  `servers`  `avatar`  `search`  `invite`", inline=False)
    embed.add_field(name=":thinking: More questions?", value="Type `support` for join our server!", inline=False)
    embed.set_footer(text='Use , before using commands')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    

@bot.command()
async def emoji(ctx):
    await ctx.send(random.choice(bot.emojis))

@bot.command()
async def ping(ctx):
    t = await ctx.send(':ping_pong: | Pong!, Calculating...')
    await asyncio.sleep(1)
    await t.edit(content=f':ping_pong: | **Pong!** `{ctx.bot.latency * 1000:,.0f}MS`')

@bot.command()
async def lenny(ctx):
    await ctx.send("( ͡° ͜ʖ ͡°)")

@bot.command()
async def shrug(ctx):
    await ctx.send("¯\_(ツ)_/¯")

@bot.command()
async def hug(ctx):
    await ctx.send("(つ ͡° ͜ʖ ͡°)つ")

@bot.command()
async def kys(ctx):
    await ctx.send("Nu te sinucide :)")

@bot.command()
async def kiss(ctx):
    await ctx.send("( ˶˘ ³˘(˵ ͡° ͜ʖ ͡°˵)♡")

@bot.command(aliases=['mom'])
async def momsay(ctx, *, message=None):
    if message is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please put the message what mom says.**')
    await ctx.send(f'Mom: **{message}**     Me: **no.**')

@bot.command(aliases=['jesus'])
async def jesussay(ctx, *, message=None):
    if message is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please put the message what jesus says.**')
    await ctx.send(f'Jesus says: **{message}**')


@bot.command()
async def here(ctx):
    await ctx.send("""<:here4:487208268964560896><:here3:487208303584346112><:here2:487208337176526858><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384>""")


@bot.command()
async def rage(ctx):
    await ctx.send("ヽ( ಠ益ಠ )ﾉ")

@bot.event
async def on_command_error(ctx, error):
    if ctx.author.bot is True:
        return
    await ctx.send(f'<:RaluvyError:489805076118896690> | **{error}**')

@bot.command(aliases= ["sinfo"])
async def serverinfo(ctx):
    em = discord.Embed(color=discord.Colour.orange())
    em.add_field(name=':pencil2: | Name', value=f'{ctx.author.guild.name}', inline=True)
    em.add_field(name=':crown: | Owner', value=f'{ctx.author.guild.owner.mention} [{ctx.author.guild.owner.id}]', inline=True)
    em.add_field(name=':mountain_snow: | Icon', value='Type `,servericon` for see this.', inline=True)
    em.add_field(name=':family_mwgb: | Roles', value='Type `,serverroles` for see this.', inline=True)
    em.add_field(name=':busts_in_silhouette: | Members', value=f'{ctx.guild.member_count}', inline=True)
    em.add_field(name=':clock1: | Created at', value=ctx.guild.created_at, inline=True)
    em.set_thumbnail(url=ctx.guild.icon_url)
    em.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=em)

@bot.command(aliases =['sicon'])
async def servericon(ctx):
    em = discord.Embed(title="", color=discord.Colour.blue())
    em.set_author(name=f"{ctx.guild.name}'s icon")
    em.set_image(url=ctx.guild.icon_url)
    em.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=em)

@bot.command(aliases=['sroles'])
async def serverroles(ctx):
    em = discord.Embed(color=discord.Colour.blue())
    em.add_field(name=f'Server Roles [{len(ctx.guild.roles)}]', value=', '.join(g.name for g in ctx.guild.roles))
    await ctx.send(embed=em)

@bot.command()
async def tableflip(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻")

@bot.command(aliases=['prune'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, number: int):
    await ctx.message.delete()
    await ctx.message.channel.purge(limit=number)
    await ctx.send(f'<:RaluvySucces:489805130963615754> | **{int(number)} message deleted**', delete_after=5)

@bot.command(aliases=['av'])
async def avatar(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    em = discord.Embed(description=f'{member.mention}\'s [avatar]({member.avatar_url})', color=discord.Colour.blurple())
    em.set_image(url=member.avatar_url)
    await ctx.send(embed=em)

@bot.command()
async def kill(ctx, member: discord.Member=None):
    if member is None:
        await ctx.send(":gun: | **You died, tag a user to kill!**")
    if member is not None:
        await ctx.send(f':gun: | **{member} died**')


@bot.command()
async def unflip(ctx):
    await ctx.send("┬─┬ ノ( ゜-゜ノ)")

@bot.command()
async def cplm(ctx):
    await ctx.send("<:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372>")

@bot.command(aliases=['about'])
async def stats(ctx):
    embed = discord.Embed(title="Stats Bot", color=0xe67e22)
    embed.add_field(name="<:RaluvyUsers:489805123191701504> | Total Users", value=len(bot.users), inline=True)
    embed.add_field(name="<:RaluvyServers:489805145757188097> | Total Servers", value=len(bot.guilds), inline=True)
    embed.add_field(name=":crown: | Owner Bot", value=f'<@390540063609454593>', inline=True)
    embed.add_field(name=':clock1: | Created at', value=ctx.me.created_at)
    embed.add_field(name="Library", value="<:RaluvyPython:489805100420694016> Python 3.6.6 (discord.py)", inline=True)
    embed.set_thumbnail(url=ctx.me.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Thank you for using Raluvy <3')
		
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None):
    if member is None:
       return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Nothing? Tag a user!**")
    await user.kick(reason=f'Requested by {ctx.author}')
    await ctx.send("<:RaluvySucces:489805130963615754> | **{} has been kicked!**".format(member.mention))

@bot.command()
@commands.has_permissions(kick_members=True)
async def softban(ctx, user: discord.Member = None):
    if member is None:
       return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Nothing? Tag a user!**")
    await user.ban(reason=f'Requested by {ctx.author}')
    await user.unban()
    await ctx.send("<:RaluvySucces:489805130963615754> | **{} has been kicked (softban)!**".format(user.mention))

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    if member is None:
       return await ctx.send("<:RaluvyQuestion:489805105764499467> | **Nothing? Tag a user!**")
    await user.ban(reason=f'Requested by {ctx.author}')
    await ctx.send("<:RaluvySucces:489805130963615754> | **{} has been banned!**".format(user.mention))

@bot.command()
async def love(ctx):
    await ctx.send("(˵ ͡~ ͜ʖ ͡°˵)ﾉ⌒♡*:･。.")

@bot.command(aliases= ["whois"])
async def userinfo(ctx, member: discord.Member=None):
    if member is None:
	    member = (ctx.author)
    embed = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
    embed.set_author(name="Who is?")
    embed.add_field(name=":bust_in_silhouette: | Name", value=member.name)
    embed.add_field(name=":id: | ID", value=member.id)
    embed.add_field(name=":robot: | Is this a bot?", value=member.bot)
    embed.add_field(name=":atm: | Tag", value=member.discriminator)
    embed.add_field(name=":eject: | Top Role", value=member.top_role)
    embed.add_field(name=":pencil2: | Nick", value=member.nick)
    embed.add_field(name=":inbox_tray: | Joined", value=member.joined_at)
    embed.add_field(name=":clock1: | Created at", value=member.created_at)
    embed.set_thumbnail(url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    
    await ctx.send(embed=embed)


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

@bot.command()
async def owo(ctx, *, message=None):
    if message is None:
        return await ctx.send("**OwO! What's this?**")
    await ctx.send(f"""**OwO! {message}**""")

@bot.command()
async def wumpus(ctx, *, message=None):
    if message is None:
        return await ctx.send('<a:aWumpus:479223216796336148>')
    await ctx.send('<a:aWumpus:479223216796336148>'.join(message))

@bot.command()
async def blobdance(ctx, *, message=None):
    if message is None:
        return await ctx.send('<a:ablobyay:464794064579985409>')
    await ctx.send('<a:ablobyay:464794064579985409>'.join(message))

@bot.command()
async def parrot(ctx, *, message=None):
    if message is None:
        return await ctx.send('<a:parrot:491311653884002304>')
    await ctx.send('<a:parrot:491311653884002304>'.join(message))

@bot.command()
async def support(ctx):
    em = discord.Embed(title="", description="", color=discord.Colour.green())
    em.add_field(name='Join our support server!', value='[here]( https://discord.gg/bazhjYQ )')
    await ctx.send(embed=em)





bot.run(os.getenv("TOKEN"))
