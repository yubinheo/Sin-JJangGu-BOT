import discord
from discord.ext import commands
import os
import asyncio
import datetime


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
        await asyncio.sleep(10)

        
@bot.event
async def on_member_join(member):

    guild = member.guild
    channel = discord.utils.get(member.guild.text_channels, id = '703107735100850277')

    join = discord.Embed(description = f'{member}님, {guild}에 입장하셨습니다.', colour = discord.Colour.green())
    join.set_thumbnail(url = member.avatar_url)
    join.set_author(name = member.name, icon_url = member.avatar_url)
    join.set_footer(text = member.guild, icon_url = member.guild.icon_url)
    join.timestamp = datetime.datetime.utcnow()

    await channel.send(embed = join)

    role = discord.utils.get(member.guild.roles, id=int("696510124113526814"))
    await member.add_roles(role)

@bot.event
async def on_member_remove(member):

    guild = member.guild
    channel = discord.utils.get(member.guild.text_channels, id = '703107735100850277')

    remove = discord.Embed(description = f'{member}님, {guild}에서 퇴장하셨습니다.', colour = discord.Colour.red())
    remove.set_thumbnail(url = member.avatar_url)
    remove.set_author(name = member.name, icon_url = member.avatar_url)
    remove.set_footer(text = member.guild, icon_url = member.guild.icon_url)
    remove.timestamp = datetime.datetime.utcnow()

    await channel.send(embed = remove)        
        

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
