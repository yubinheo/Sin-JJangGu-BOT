import discord
from discord.ext import commands


class Error(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.error, 'on_error'):
                return
            else:
                embed = discord.Embed(
                    title=f'{ctx.command} 에서 오류 발생', description=f'{ctx.command.qualified_name}\n{error}', Colour=discord.Colour.red())
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title=f'{ctx.command} 에서 오류 발생',
                                  description=f'{error}', Colour=discord.Colour.red())
            await ctx.send(embed=emded)


def setup(bot):
    bot.add_cog(Error(bot))
