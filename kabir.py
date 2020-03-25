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

client = Bot(description="DarkBot Bot is best", command_prefix="d!", pm_help = True)
client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(type=1,name='HAPPY CITY'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name="With My girl friend"))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with Python coding',type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=' your love and affection'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name=f'ghhh'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name=f'with vgg'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name='with MoonliteツTrivia V2.0'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='bada pachtaoge',type=2))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='HAPPY CITY',type=3))
        await asyncio.sleep(5)


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('AKHIL')
    print('Created by AKHIL')
    client.loop.create_task(status_task())



client.run("Njg2MjE3MzQ4MTQ2NzkwNDQ0.XmT_3A.FSMrUboEuaGm9TFr7925PwGI1ms", bot=False)
