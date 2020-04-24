import discord
import asyncio
import datetime
import platform
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print('Test.py')

    @commands.command()
    async def test(self, ctx):

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__

        info = discord.Embed(title = f'{bot.user.display_name} 정보',colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
        info.set_thumbnail(url = bot.user.avatar_url)
        info.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

        info.add_field(name = '코딩 언어', value = 'Python', inline = True)
        info.add_field(name = 'Python Version', value = pythonVersion)
        info.add_field(name = 'Discord.py Version', value = dpyVersion)

        await ctx.send(embed = info)


def setup(bot):
    bot.add_cog(Test(bot))
