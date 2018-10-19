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
from asyncio import sleep
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
async def on_command_error(ctx, error):
    print(f'\'{ctx.author}\' used command \'{ctx.command}\' and got this error: \n-{error}')
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

@bot.listen()
async def on_message(message):
    if message.content.lower() == '<@390540063609454593>' and message.author != bot.user:
        await message.channel.send("**Raluvy is away**, Please... don't ping me. ;w;")
    else:
        await bot.process_command(message)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def invite(ctx):
    await ctx.send("""**You can add me here ->** http://bit.ly/InviteRaluvyBot""")

@bot.command()
async def servers(ctx):
    await ctx.send(f'{len(bot.guilds)} Servers!\n```py\n"' + '"\n"'.join(g.name for g in bot.guilds)+ '"```')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def sayd(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)


@bot.command(aliases=['emoji_info', 'emoji info'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def emojiinfo(ctx, emoji: discord.Emoji):
    await ctx.send(f'`Name:` {emoji.name}\n`ID:` {emoji.id}\n`Preview:` {emoji} (`{emoji}`)\n`URL:` {emoji.url}\n`Created at:` {emoji.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")}')


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

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def love(ctx):
    await ctx.send("(˵ ͡~ ͜ʖ ͡°˵)ﾉ⌒♡*:･。.")

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
	
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def uwu(ctx, *, message=None):
    if message is None:
        return await ctx.send("<a:aUWU:478879639586996224>")
    await ctx.send(f"""<a:aUWU:478879639586996224> | **{message}**""")

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
        return await ctx.send('<a:ablobyay:464794064579985409>')
    await ctx.send('<a:ablobyay:464794064579985409>'.join(message))

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

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    t = await ctx.send(':ping_pong: | Pong!, Calculating...')
    await asyncio.sleep(1)
    await t.edit(content=f':ping_pong: | **Pong!** `{ctx.bot.latency * 1000:,.0f}MS`')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def lenny(ctx):
    await ctx.send("( ͡° ͜ʖ ͡°)")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def shrug(ctx):
    await ctx.send("¯\_(ツ)_/¯")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def hug(ctx):
    await ctx.send("(つ ͡° ͜ʖ ͡°)つ")

@bot.command(name='8ball')
@commands.cooldown(1, 5, commands.BucketType.user)
async def lball(ctx, question = None):
	if question is None:
		return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please put a question!**')
	if question is not None:
		await ctx.send(random.choice(['● It is certain.', '● It is decidedly so.', '● Without a doubt.', '● Yes - definitely.', '● You may rely on it', '● As I see it, yes.', '● Most likely.', '● Outlook good.', '● Yes.', '● Signs point to yes.', '● Reply hazy, try again', '● Ask again later.', '● Better not tell you now.', '● Cannot predict now.', '● Concentrate and ask again.', '● Don`t count on it.', '● My reply is no.', '● My sources say no', '● Outlook not so good.', '● Very doubtful.' ]))
		
@bot.command()
async def kys(ctx):
    await ctx.send("Nu te sinucide :)")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kiss(ctx):
    await ctx.send("( ˶˘ ³˘(˵ ͡° ͜ʖ ͡°˵)♡")

@bot.command(aliases=['mom'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def momsay(ctx, *, message=None):
    if message is None:
        return await ctx.send('<:RaluvyQuestion:489805105764499467> | **Please put the message what mom says.**')
    await ctx.send(f'Mom: **{message}**     Me: **no.**')

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

@bot.command()
async def verify(ctx):
  if ctx.author.guild.id == 464783042310045707:
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, id=464786254790393866)
    user = ctx.message.author
    await user.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, id=498186204353921035)
    user = ctx.message.author
    await user.remove_roles(role)
  if ctx.author.guild.id != 464783042310045707:
        return

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def here(ctx):
    await ctx.send("""<:here4:487208268964560896><:here3:487208303584346112><:here2:487208337176526858><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384>""")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def rage(ctx):
    await ctx.send("ヽ( ಠ益ಠ )ﾉ")

@bot.command(aliases= ["sinfo", "server info", "server_info"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def serverinfo(ctx):
    c = 0
    a = 0
    n = ctx.guild.member_count
    for i in ctx.guild.members:
     if i.bot is True:
      c+=1
    for i in ctx.guild.members:
     if i.bot is False:
      a+=1
    em = discord.Embed(color=discord.Colour.orange())
    em.add_field(name=':pencil2: Name', value=f'{ctx.author.guild.name}', inline=True)
    em.add_field(name=':crown: Owner', value=f'{ctx.author.guild.owner.mention} [{ctx.author.guild.owner.id}]', inline=True)
    em.add_field(name=':mountain_snow: Icon', value='Type `,servericon`', inline=True)
    em.add_field(name=':beginner: Roles', value=f'{len(ctx.guild.roles)} `,sroles`', inline=True)
    em.add_field(name=':busts_in_silhouette: Members', value=f'{n}', inline=True)
    em.add_field(name=':robot: Bots', value=f'{c}', inline=True)
    em.add_field(name=':bust_in_silhouette: People', value=f'{a}', inline=True)
    em.add_field(name=':clock1: Created at', value=ctx.guild.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=True)
    em.add_field(name=':globe_with_meridians: Region', value=ctx.guild.region, inline=True)
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
    em = discord.Embed(color=discord.Colour.blue())
    em.add_field(name=f'Server Roles [{len(ctx.guild.roles)}]', value=', '.join(g.name for g in ctx.guild.roles))
    await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def tableflip(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻")


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
        await ctx.send(random.choice([f':gun: | **{ctx.author.mention} wanted to kill {member.mention} just as he stumbled and struck his head with a stone**', f':gun: | **{member.mention} gave too much rage to Clash Royale until he fainted and died**', f':gun: | **{member.mention} was pushed by {ctx.author.mention} from the 5th floor and died**', f':gun: **{member.mention}, The pregnancy of the table just fell asleep and caught fire**', f':gun: | **{member.mention} was shot by {ctx.author.mention}**', f':gun: **After a hard attempt to kill him {member.mention} , {ctx.author.mention} was arrested**']))

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def unflip(ctx):
    await ctx.send("┬─┬ ノ( ゜-゜ノ)")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def cplm(ctx):
    await ctx.send("<:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372><:BlobCPLM:465441659140964372>")

@bot.command(aliases=['about', 'info', 'botinfo'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def stats(ctx):
    embed = discord.Embed(title="Stats Bot", color=0xe67e22)
    embed.add_field(name="<:RaluvyUsers:489805123191701504> | Total Users", value=len(bot.users), inline=True)
    embed.add_field(name="<:RaluvyServers:489805145757188097> | Total Servers", value=len(bot.guilds), inline=True)
    embed.add_field(name=":crown: | Owner Bot", value=f'<@390540063609454593>', inline=True)
    embed.add_field(name=':clock1: | Created at', value=ctx.me.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
    embed.add_field(name="Library", value="<:RaluvyPython:489805100420694016> Python 3.6.6 (discord.py)", inline=True)
    embed.set_thumbnail(url=ctx.me.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Thank you for using Raluvy <3')
	
    await ctx.send(embed=embed)



# Moderation #

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, message=None):
        if member is ctx.author:
             return await ctx.send("<:RaluvyError:489805076118896690> | **I can't kick you! ;-;**")
        if member is ctx.message.guild.owner:
             await ctx.send("<:RaluvyError:489805076118896690> | **I can't kick to Owner!**")
        if member is ctx.me:
             await ctx.send("<:RaluvyError:489805076118896690> | **I can't kick myself ;-;**")
        if member is None:
             await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,kick <member>`!**")
        if member is not None and message is None:
             await member.kick(reason=f'Requested by {ctx.author}')
             await ctx.send(f'<:RaluvySucces:489805130963615754> | **{member} was kicked!**')
        if member is not None and message is not None:
             await member.kick(reason=f'{message}  by {ctx.author}')
             await ctx.send(f'<:RaluvySucces:489805130963615754> | **{member} was kicked!**')

@bot.command()
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member = None, *, message = None):
         if member is ctx.author:
             return await ctx.send("<:RaluvyError:489805076118896690> | **I can't softban you! ;-;**")
         if member is ctx.message.guild.owner:
             await ctx.send("<:RaluvyError:489805076118896690> | **I can't softban to Owner!**")
         if member is ctx.me:
             await ctx.send("<:RaluvyError:489805076118896690> | **I can't softban myself ;-;**")
         if member is None:
             await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,softban <member>`!**")
         if member is not None and message is None:
             await member.ban(reason=f'Requested by {ctx.author}')
             await member.unban()
             await ctx.send(f'<:RaluvySucces:489805130963615754> | **{member} was kicked (softban)!**')
         if member is not None and message is not None:
             await member.ban(reason=f'{message}  by {ctx.author}')
             await member.unban()
             await ctx.send(f'<:RaluvySucces:489805130963615754> | **{member} was kicked (softban)!**')


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, message=None):
         if member is ctx.author:
             return await ctx.send("<:RaluvyError:489805076118896690> | **I can't ban you! ;-;**")
         if member is ctx.message.guild.owner:
             await ctx.send("<:RaluvyError:489805076118896690> | **I can't ban to Owner!**")
         if member is ctx.me:
             await ctx.send("<:RaluvyError:489805076118896690> | **I can't ban myself ;-;**")
         if member is None:
             await ctx.send("<:RaluvyQuestion:489805105764499467> | **Please use `,ban <member>`!**")
         if member is not None and message is None:
             await member.ban(reason=f'Requested by {ctx.author}')
             await ctx.send(f'<:RaluvySucces:489805130963615754> | **{member} was banned!**')
         if member is not None and message is not None:
             await member.ban(reason=f'{message}  by {ctx.author}')
             await ctx.send(f'<:RaluvySucces:489805130963615754> | **{member} was banned!**')
	
	
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
    await ctx.message.delete()
    await ctx.message.channel.purge(limit=number)
    await ctx.send(f'<:RaluvySucces:489805130963615754> | **{int(number)} message deleted**', delete_after=5)
	
	
	

	
# Utility #	
	
@bot.command(aliases=['av'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def avatar(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    em = discord.Embed(description=f'{member.mention}\'s [avatar]({member.avatar_url})', color=discord.Colour.blurple())
    em.set_image(url=member.avatar_url)
    await ctx.send(embed=em)
	
	
@bot.command(aliases= ["whois", "uinfo", "playerinfo", "user info"])
async def userinfo(ctx, member: discord.Member=None):
    if member is None:
	    member = (ctx.author)
    embed = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
    embed.set_author(name="Who is?")
    embed.add_field(name=":bust_in_silhouette: Name", value=member.name)
    embed.add_field(name="Is this a bot?", value=member.bot)
    embed.add_field(name=":atm: Tag", value=member.discriminator)
    embed.add_field(name=":eject: Top Role", value=member.top_role)
    embed.add_field(name=":pencil2: Nick", value=member.nick)
    embed.add_field(name=":inbox_tray: Joined", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
    embed.add_field(name=":clock1: Created at", value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
    embed.add_field(name=":beginner:  Roles", value=', '.join(g.name for g in member.roles))
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'ID: {member.id}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)




# More #
	
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
    embed = discord.Embed(title="HELP", description="List commands", color=0xe67e22)
    embed.add_field(name="<a:ablobdancewhite:464794007755685898> Fun", value="`8ball`  `choose`  `emoji`  `respect`  `dog`  `doge`  `cat`  `kill`", inline=False)
    embed.add_field(name=":ok: Text", value="`lenny`  `hug`  `shrug`  `blobdance`  `uwu`  `kiss`  `rage`  `unflip`  `tableflip`  `love`  `momsay`  `jesussay`  `clap`  `sayd`  `say`  `space`  `here`  `owo`  `wumpus`  `parrot`", inline=False)
    embed.add_field(name=":hammer:  Moderation", value="`kick`  `ban`  `softban`  `purge`  `role`", inline=False)
    embed.add_field(name=":information_source: Info", value="`emojiinfo`  `serverinfo`  `userinfo`  `stats`", inline=False)
    embed.add_field(name=":pushpin: Utility", value="`ping`  `servers`  `randomnumber`  `avatar`  `search`  `invite`", inline=False)
    embed.add_field(name=":thinking: More questions?", value="Type `support` for join our server!", inline=False)
    embed.set_footer(text='Use , before using commands')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

async def presence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        a = 0
        for i in bot.guilds:
            for u in i.members:
                if u.bot == False:
                    a = a + 1

        await bot.change_presence(activity=discord.Game(name="i like cookies || ,help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=",invite || ,help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Game(name="Noice || ,help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.users)} users || ,help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers || ,help"))
        await sleep(30)
	

bot.loop.create_task(presence())
bot.run(os.getenv("TOKEN"))
