import discord
from discord.ext import commands

import datetime
import time

start_time = time.time()

class Uptime(commands.Cog):

def __init__(self, bot):
    self.bot = bot

    @commands.command(aliases = ['업타임'])
    async def uptime(self, ctx):
    curr_time = time.time()
	    diff = int(round(curr_time - start_time))
	    text = str(datetime.timedelta(seconds=diff))
	    embed = discord.Embed(color=discord.Color.blue())
	    embed.add_field(name=f"{self.bot.user.name} 온라인 시간 :-", value=text)
	    try:
	        await ctx.send(embed=embed)
	    except discord.HTTPException:
	        await ctx.send(f"{self.bot.user.name} 온라인 시간 " + text)

def setup(bot):
	bot.add_cog(Uptime(bot))
