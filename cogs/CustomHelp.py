import discord
from discord.ext import commands

import asyncio
import datetime


class CustomHelp(commands.Cog, name='Help'):

    """짱구 BOT 도움말 명령어"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['도움말'])
    async def help(self, ctx, *cog):
        """짱구 봇의 모든 명령어를 확인 할 수 있습니다"""

        bot_prefix = '?'

        if not cog:

            em = discord.Embed(description='짱구 BOT 도움말', colour=discord.Colour.blue())

            cogs_desc = ''
            for x in self.bot.cogs:
                cogs_desc += ('**{}** - {}'.format(x, self.bot.cogs[x].__doc__)+'\n')
            em.add_field(name='명령어 목록', value=cogs_desc[0:len(cogs_desc)-1], inline=False)
            await ctx.message.add_reaction(emoji='✉')
            await ctx.send(embed=em)
        else:
            if len(cog)>1:
                found = False
                for x in self.bot.cogs:
                    print(x)
                    for y in cog:
                        print('     '+y)
                        if x == y:
                            print('         '+y)
                            scog_info = ''
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    scog_info += f'**{c.name}** - {c.help}\n'
                            try:
                                em.add_field(name=f'{y} 명령어 목록', value=scog_info)
                            except:
                                em = discord.Embed(colour=discord.Colour.blue())
                                em.add_field(name=f'{y} 명령어 목록', value=scog_info)
                            found = True
                            break
                if not found:
                    em = discord.Embed(colour=discord.Colour.blue())
                    for x in self.bot.cogs:
                        for c in self.bot.get_cog(x).get_commands():
                            for i in cog:
                                if c.name == i:
                                    em.add_field(name=f'{c.name} - {c.help}', value=f'사용방법 :\n{bot_prefix}{c.qualified_name} {c.signature}')
                                    found = True
                    if not found:
                        em = discord.Embed(title='Error!', description=f'`{cog[0]}` 해당 Cog 혹은 명령어를 찾을 수 없습니다\n 확인 후 재사용 부탁드립니다.', colour=discord.Colour.blue())
                else:
                    await ctx.message.add_reaction(emoji='✉')
            else:
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            em = discord.Embed(colour=discord.Colour.blue())
                            scog_info = ''
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    scog_info += f'**{c.name}** - {c.help}\n'
                            em.add_field(name=f'{y} 명령어 목록', value=scog_info)
                            found = True
                            break
                if not found:
                    for x in self.bot.cogs:
                        for c in self.bot.get_cog(x).get_commands():
                            if c.name == cog[0]:
                                em = discord.Embed(colour=discord.Colour.blue())
                                em.add_field(name=f'{c.name} - {c.help}', value=f'사용방법 :\n{bot_prefix}{c.qualified_name} {c.signature}')
                                found = True
                    if not found:
                        em = discord.Embed(title='Error!', description=f'`{cog[0]}` 해당 Cog 혹은 명령어를 찾을 수 없습니다\n 확인 후 재사용 부탁드립니다.', colour=discord.Colour.blue())
                else:
                    await ctx.message.add_reaction(emoji='✉')
            await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(CustomHelp(bot))
