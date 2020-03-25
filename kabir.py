import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType

client = Bot(description="Akhil is best", command_prefix="d!", pm_help = True)
client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(type=1,name='PUBG'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name="Clash Of Clans"))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='Harry potter',type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=' QUIPP '))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name=f'Friends'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name=f'Its Spider'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name='with TRIVIA NIGHT'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='bada pachtaoge',type=2))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='HAVE A NICE DAY',type=3))
        await asyncio.sleep(5)


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('AKHIL')
    print('Created by AKHIL')
    client.loop.create_task(status_task())



client.run("NTY2NDg0MjgzNDM5NzEwMjIx.XnCe8w.sE1BqOMCQGXZh6pXk8kXF-9ZXhI", bot=False)
