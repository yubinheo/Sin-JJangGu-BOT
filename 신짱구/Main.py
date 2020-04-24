import discord
import asyncio
import os
import json
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot


prefix = '짱구야 '
bot = commands.Bot(command_prefix=prefix)

bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'{bot.user.name}#{bot.user.discriminator} 으로 로그인 중... / 봇 고유 ID : {bot.user.id}')
    user = len(bot.users)
    server = len(bot.guilds)
    messages = [f'{server}개 {user} 유저와', '짱구와 떡잎마을 방범대', f'{prefix} 도움말 확인중']
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[0], type=discord.ActivityType.playing))
        messages.append(messages.pop(0))
        await asyncio.sleep(7)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[ :-3 ]}')


access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
