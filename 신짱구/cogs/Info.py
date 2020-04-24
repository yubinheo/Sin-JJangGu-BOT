import discord
import asyncio
import psutil
import time
from platform import python_version
from datetime import datetime
from discord.ext import commands
import random
import urllib.parse

start_time = time.time()

class Bot_Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process()
        self.prefix = '!?'

    def getUptime(self):
        now = datetime.utcnow()
        delta = now - self.bot.startTime
        hours, rem = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(rem, 60)
        days, hours = divmod(hours, 24)
        if days:
            return f"{days} days, {hours} hr, {minutes} mins, and {seconds} secs"
        else:
            return f"{hours} hr, {minutes} mins, and {seconds} secs"

    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print('Info.py')

    @commands.command(aliases = ['봇정보'])
    async def info_bot(self, ctx):

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        user = len(bot.users)
        server = len(bot.guilds)
        ramUsage = self.process.memory_full_info().uss / 1024**2
        cpuUsage = self.process.cpu_percent() / psutil.cpu_count()

        em = discord.Embed(title = f'{bot.user.name} - 정보', colour = 0XFFE302)
        em.timestamp = datetime.datetime.utcnow()
        em.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
        em.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_thumbnail(url = bot.user.avatar_url)

        process = f"""• Memory Usage: **{ramUsage:.2f}MiB**
    • CPU Usage: **{cpuUsage:.2f}%**
    • Uptime: **{self.getUptime()}**"""

        em.add_field(name = '접두사 :', value = prefix, inline = False)
        em.add_field(name = '이름 :', value = f'{bot.user.name}#{bot.user.discriminator}\n{bot.user.id}', inline = False)
        em.add_field(name = '<:Python:698093562985840710> 파이썬 버전 :', value = pythonVersion, inline = False)
        em.add_field(name = '<:discord_py:698416902199836683> 디스코드.py 버전 :', value = dpyVersion, inline = False)
        em.add_field(name = 'BOT 사용 서버 수 :', value = server, inline = False)
        em.add_field(name = 'BOT 사용 멤버 수 :', value = user, inline = False)
        em.add_field(name = ':birthday: 봇 생성일 :', value = bot.user.created_at.strftime("%Y년 %m월 %d일".encode("unicode-escape").decode()).encode().decode("unicode-escape"),inline = False)
        em.add_field(name="❯❯ Process", value = process, inline = True)
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Bot_Info(bot))
