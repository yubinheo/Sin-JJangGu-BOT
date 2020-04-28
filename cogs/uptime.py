import discord
from discord.ext import commands

import datetime
import time

start_time = time.time()

class Uptime(commands.Cog):

def __init__(self, bot):
	self.bot = bot

    @commands.command()
	async def uptime(self, ctx):
		curr_time = time.time()
		diff = int(round(curr_time - start_time))
		text = str(datetime.timedelta(seconds=diff))
		embed = discord.Embed(color=discord.Color.dark_blue())
		embed.add_field(name="Im Uptime Since :-", value=text)
		try:
			await ctx.send(embed=embed)
		except discord.HTTPException:
			await ctx.send("Uptime is " + text)

def setup(bot):
	bot.add_cog(Uptime(bot))
