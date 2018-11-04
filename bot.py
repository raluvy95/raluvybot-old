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
 print("Discord.py API version:", discord.__version__)

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
@commands.cooldown(1, 5, commands.BucketType.user)
async def hug(ctx, member: discord.Member=None):
    a = (random.choice(['https://media.giphy.com/media/xUPGchPtx9E4Ijht9S/giphy.gif', 'http://i.imgur.com/VIwkYxz.gif', 'https://vignette.wikia.nocookie.net/steven-universe/images/1/1b/Group_Hug.gif/revision/latest/scale-to-width-down/320?cb=20160515215411', 'http://orig03.deviantart.net/648e/f/2013/071/2/3/hug_by_shiro_nee-d5xtm62.gif', 'https://vignette.wikia.nocookie.net/degrassi/images/f/f1/Asuna_hugs_Kirito.gif', 'https://thumbs.gfycat.com/AlienatedUnawareArcherfish-size_restricted.gif', 'https://media.giphy.com/media/kvKFM3UWg2P04/giphy.gif', 'https://66.media.tumblr.com/5dfb67d0a674fe5f81950478f5b2d4ed/tumblr_ofd4e2h8O81ub9qlao1_500.gif', 'https://i.imgur.com/r9aU2xv.gif', 'https://media.giphy.com/media/14aBJO7py75MD6/giphy.gif', 'https://66.media.tumblr.com/19e9210e27061fd20b58078cad8c9552/tumblr_nj5nw0LHbw1r7eta3o1_500.gif', 'https://media.giphy.com/media/3oz8xU3bnghA8WzEGI/giphy.gif', 'https://vignette.wikia.nocookie.net/degrassi/images/2/29/Beckdam_hug.gif/revision/latest?cb=20130825231225', 'https://media.giphy.com/media/143v0Z4767T15e/giphy.gif', 'https://i.imgur.com/nrdYNtL.gif', 'https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif', 'https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif']))
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"Hugs {member.name}!", color=0xe67e22)
      em.set_image(url=a)
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kiss(ctx, member: discord.Member=None):
    a = (random.choice(['https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865', 'https://i0.wp.com/loveisaname.com/wp-content/uploads/2016/09/3.gif', 'https://vignette.wikia.nocookie.net/highschooldxd/images/7/79/Ise_%26_Asia_second_kiss.gif/revision/latest?cb=20180514130852', 'https://data.whicdn.com/images/144335846/original.gif', 'https://media.giphy.com/media/Gj8bn4pgTocog/giphy.gif', 'https://media.giphy.com/media/KH1CTZtw1iP3W/giphy.gif', 'https://media.giphy.com/media/ONq87vZz4626k/giphy.gif', 'https://lifeo.ru/wp-content/uploads/gif-anime-kisses-13.gif', 'http://37.media.tumblr.com/42f96e0adb59440843c94e45650afd19/tumblr_n5mbsq844s1tzpao0o1_500.gif', 'https://media.giphy.com/media/ll5leTSPh4ocE/giphy.gif', 'http://www.lovethisgif.com/uploaded_images/41239-Anime-Cheek-Kiss-Gif-Karen-Kissing-Shino-lewd-.gif', 'https://i.pinimg.com/originals/33/55/7f/33557fcbfbf21b4dd20b34babb5db7b5.gif', 'https://i.imgur.com/NkfsJV7.gif']))
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"Awwww!", color=0xe67e22)
      em.set_image(url=a)
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def poke(ctx, member: discord.Member=None):
    a = (random.choice(['https://media1.tenor.com/images/76e377271bf00ba61d954b2752713596/tenor.gif?itemid=5075308', 'https://i.gifer.com/bun.gif', 'https://orig00.deviantart.net/1a00/f/2012/007/3/e/minako_poke_by_endless_summer181-d4llj28.gif', 'https://media1.tenor.com/images/48086974f33a3e0114b2e0387f812ae4/tenor.gif?itemid=12360399', 'https://media.giphy.com/media/WvVzZ9mCyMjsc/giphy.gif', 'https://66.media.tumblr.com/913f6c8b397a28cce5d739d9e5440f13/tumblr_on0ks5LR3P1ridyfoo1_500.gif', 'https://media1.tenor.com/images/fd46d903c4a20a7e82519a78f15b2750/tenor.gif?itemid=8562185', 'https://media1.tenor.com/images/ab936c887562756472f83850426bf6ef/tenor.gif?itemid=11956062', 'https://i.gifer.com/S00v.gif']))
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"Poke! :3", color=0xe67e22)
      em.set_image(url=a)
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def pat(ctx, member: discord.Member=None):
    a = (random.choice(['https://media1.tenor.com/images/68d981347bf6ee8c7d6b78f8a7fe3ccb/tenor.gif?itemid=5155410', 'https://media1.tenor.com/images/fb3e0b0f18188450bfded4a585de2b90/tenor.gif?itemid=8208759', 'https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif', 'https://media1.tenor.com/images/1e92c03121c0bd6688d17eef8d275ea7/tenor.gif?itemid=9920853', 'https://thumbs.gfycat.com/AgileHeavyGecko-max-1mb.gif', 'https://i.imgur.com/2lacG7l.gif', 'https://img.fireden.net/a/image/1503/79/1503792695094.gif', 'https://thumbs.gfycat.com/MassiveNeglectedAustraliankestrel-small.gif', 'https://pa1.narvii.com/6215/ed0176937f5de9412f3408cdfd4c6d88b1ec0df1_hq.gif', 'https://i.pinimg.com/originals/2e/62/cd/2e62cd7491be4ec9f0ec210d648b80fd.gif']))
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"Pats {member.name}! :3", color=0xe67e22)
      em.set_image(url=a)
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def slap(ctx, member: discord.Member=None):
    a = (random.choice(['https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif', 'https://media1.tenor.com/images/85722c3e51d390e11a0493696f32fb69/tenor.gif?itemid=5463215', 'https://media1.tenor.com/images/85722c3e51d390e11a0493696f32fb69/tenor.gif?itemid=5463215', 'https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943', 'https://i.gifer.com/2Vj5.gif', 'https://i.imgur.com/Agwwaj6.gif', 'https://gifimage.net/wp-content/uploads/2017/07/anime-slap-gif-14.gif']))
    if member is None:
      return await ctx.send("**Tag a user to run this command.**")
    if member is not None:
      em = discord.Embed(title=f"* Slaps {member.name} *", color=0xe67e22)
      em.set_image(url=a)
      em.timestamp = datetime.datetime.utcnow()
      return await ctx.send(embed=em)

@bot.command()
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
    await ctx.send(f'```{a}           {a}    {a} {a}\n  {a}       {a}      {a}    {a}\n    {a}   {a}        {a}     {a}\n        {a}            {a}     {a}\n    {a}   {a}        {a}     {a}\n  {a}       {a}      {a}    {a}\n{a}           {a}    {a} {a}```')



@bot.command()
async def servers(ctx):
    await ctx.message.delete()
    await ctx.send(f'{len(bot.guilds)} Servers!\n```py\n"' + '"\n"'.join(g.name for g in bot.guilds)+ '"```', delete_after=5)

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

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def doge(ctx, *message):
    i = ('http://dogr.io/' + '/'.join(message) + '/.png?split=false')
    em = discord.Embed(title="Wow, much doge, such amazing!", color=0xe67e22)
    em.set_image(url=i)
    em.timestamp = datetime.datetime.utcnow()
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
async def shrug(ctx):
    await ctx.send("¯\_(ツ)_/¯")


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
    role2 = discord.utils.get(ctx.guild.roles, id=505303297935015936)
    user = ctx.message.author
    await user.remove_roles(role, role2)
  if ctx.author.guild.id != 464783042310045707:
        return

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def here(ctx):
    await ctx.send("""<:here4:487208268964560896><:here3:487208303584346112><:here2:487208337176526858><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384><:here1:487208364972048384>""")


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
async def kill(ctx, member: discord.Member=None):
    if member is None:
        await ctx.send(':gun: | **You died! Tag a user to kill him/her!**')
    if member is ctx.me:
        return await ctx.send('nope.')
    if member is ctx.author:
        return await ctx.send(':gun: | **You died! Tag a user to kill him/her!**')
    if member is not None:
        await ctx.send(random.choice([f':gun: | **{ctx.author.mention} wanted to kill {member.mention} just as he stumbled and struck his head with a stone**', f':gun: | **{member.mention} died from a murderer**', f':gun: | **{member.mention} gave too much rage to Clash Royale until he fainted and died**', f':gun: | **{member.mention} was pushed by {ctx.author.mention} from the 5th floor and died**', f':gun: **{member.mention}, The pregnancy of the table just fell asleep and caught fire**', f':gun: | **{member.mention} was shot by {ctx.author.mention}**', f':gun: **After a hard attempt to kill him {member.mention} , {ctx.author.mention} was arrested**']))


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
    embed = discord.Embed(title="HELP", description="More questions? Type `support` for join our server!", color=0xe67e22)
    embed.add_field(name="<a:ablobdancewhite:464794007755685898> Fun", value="`8ball`  `xd`  `choose`  `shiba`  `emoji`  `respect`  `dog`  `doge`  `cat`  `kill`", inline=False)
    embed.add_field(name=":ok: Text", value="`lenny`  `shrug`  `blobdance`  `uwu`  `momsay`  `jesussay`  `clap`  `sayd`  `say`  `space`  `here`  `owo`  `wumpus`  `parrot`", inline=False)
    embed.add_field(name=":hammer:  Moderation", value="`kick`  `ban`  `softban`  `purge`  `role`", inline=False)
    embed.add_field(name=":smile:  Action", value="`hug`  `kiss`  `poke`  `pat`  `slap`", inline=False)
    embed.add_field(name=":information_source: Info", value="`emojiinfo`  `serverinfo`  `userinfo`  `stats`", inline=False)
    embed.add_field(name=":pushpin: Utility", value="`ping`  `servers`  `randomnumber`  `flipcoin`  `avatar`  `search`  `invite`", inline=False)
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
