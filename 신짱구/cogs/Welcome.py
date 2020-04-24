import discord
import asyncio
import datetime
from discord.ext import commands

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print('Welcome.py')

    @commands.Cog.listener()
    async def on_member_join(self, member):

        guild = member.guild
        channel = discord.utils.get(member.guild.text_channels, id = '695588050536759326')

        join = discord.Embed(description = f'{member}님, {guild}에 입장하셨습니다.', colour = discord.Colour.green())
        join.set_thumbnail(url = member.avatar_url)
        join.set_author(name = member.name, icon_url = member.avatar_url)
        join.set_footer(text = member.guild, icon_url = member.guild.icon_url)
        join.timestamp = datetime.datetime.utcnow()

        await channel.send(embed = join)

        role = discord.utils.get(member.guild.roles, id=int("696510124113526814"))
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        guild = member.guild
        channel = discord.utils.get(member.guild.text_channels, id = '695588050536759326')

        remove = discord.Embed(description = f'{member}님, {guild}에서 퇴장하셨습니다.', colour = discord.Colour.red())
        remove.set_thumbnail(url = member.avatar_url)
        remove.set_author(name = member.name, icon_url = member.avatar_url)
        remove.set_footer(text = member.guild, icon_url = member.guild.icon_url)
        remove.timestamp = datetime.datetime.utcnow()

        await channel.send(embed = remove)

def setup(bot):
    bot.add_cog(Welcome(bot))
