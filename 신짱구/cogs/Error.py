import discord
from discord.ext import commands

class Error(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #EVENT
    @commands.Cog.listener()
    async def on_ready(self):
        print('Error.py')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title = '명령어 오류', colour = discord.Colour.red(), timestamp = ctx.message.created_at)
            embed.set_footer(text = ctx.author)
            embed.add_field(name= f'{error}', value = '명령어가 올바르지 않습니다. 확인 후 재사용 부탁드립니다.')
            await ctx.send(embed = embed)

        elif isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(title = '명령어 오류', colour = discord.Colour.red(), timestamp = ctx.message.created_at)
            embed.set_footer(text = ctx.author)
            embed.add_field(name= f'{error}', value = '정보가 누락 되었습니다. 확인 후 재사용 부탁드립니다.')
            await ctx.send(embed = embed)

        elif isinstance(error, commands.TooManyArguments):

            embed = discord.Embed(title = '명령어 오류', colour = discord.Colour.red(), timestamp = ctx.message.created_at)
            embed.set_footer(text = ctx.author)
            embed.add_field(name= f'{error}', value = '정보가 너무 많습니다. 확인 후 재사용 부탁드립니다.')
            await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Error(bot))
