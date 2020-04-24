import discord, asyncio, datetime
from discord.ext import commands

class CustomHelp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print('CustomHelp.py')

    @commands.command(aliases = ['도움말'])
    async def HELP(self, ctx):


        help = discord.Embed(description = f'접두사 {prefix}', colour = 0X2A2A4C)
        help.set_author(name = f'{bot.user.name} 명령어 목록', icon_url = bot.user.avatar_url)

        help.add_field(name = ':notebook_with_decorative_cover: 기본 명령어', value = '> `도움말`, `명령어`, `문의`',inline = False)
        help.add_field(name = ':notebook_with_decorative_cover: 정보 명령어', value = '> `핑`, `봇정보`, `유저정보`, `서버정보`',inline = False)
        help.add_field(name = ':notebook_with_decorative_cover: 크롤링 명령어')

        await ctx.send(embed = help)

        page1 = discord.Embed(title = f':notebook_with_decorative_cover: {bot.user.display_name} 일반 도움말', description = f'Prefix (접두사) : {prefix}', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
        page1.set_footer(text = f'{ctx.author.display_name} • Page 1 / 4', icon_url = ctx.author.avatar_url)
        page1.set_thumbnail(url = bot.user.avatar_url)

        page1.add_field(name = f'{prefix} 도움말', value = '도움말을 표시해줍니다.', inline = False)
        page1.add_field(name = f'{prefix} 초대', value = '짱구 봇의 초대링크를 줍니다.', inline = False)
        page1.add_field(name = f'{prefix} 문의', value = '짱구 봇 문의 사이트 초대링크를 보냅니다.', inline = False)

        page2 = discord.Embed(title = f':notebook_with_decorative_cover: {bot.user.display_name} 정보 도움말', colour = discord.Colour.dark_blue(), timestamp = ctx.message.created_at)
        page2.set_footer(text = f'{ctx.author.display_name} • Page 2 / 4', icon_url = ctx.author.avatar_url)
        page2.set_thumbnail(url = bot.user.avatar_url)

        page2.add_field(name = f'{prefix} 핑', value = '짱구 봇의 최근 통신 상태(ms) 확인', inline = False)
        page2.add_field(name = f'{prefix} 봇정보', value = f'짱구 봇의 정보를 보여줍니다.', inline = False)
        page2.add_field(name = f'{prefix} 유저정보', value = '@멘션 한사람의 디스코드 정보를 확인 할 수 있습니다.', inline = False)
        page2.add_field(name = f'{prefix} 서버정보', value = '명령어를 사용한 서버의 정보를 확인 할 수 있습니다.', inline = False)
        page2.add_field(name = f'{prefix} 체널정보', value = '명령어를 사용한 해당 채널의 정보를 확인 할 수 있습니다.', inline = False)
        page2.add_field(name = f'{prefix} 생일', value = '@멘션 한 사람의 디스코드 계정 생성일을 확인 할 수 있습니다.', inline = False)
        page2.add_field(name = f'{prefix} 서버생일', value = '명령어를 사용한 서버의 생성일을 확인 할 수 있습니다.', inline = False)

        page3 = discord.Embed(title = f':notebook_with_decorative_cover: {bot.user.display_name} 코로나 도움말', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
        page3.set_footer(text = f'{ctx.author.display_name} • Page 3 / 4' , icon_url = ctx.author.avatar_url)
        page3.set_thumbnail(url = bot.user.avatar_url)

        page3.add_field(name = '추가중',value= '조금만 기달려주세요.')

        page4 = discord.Embed(title = f':notebook_with_decorative_cover: {bot.user.display_name} 도움말', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
        page4.set_footer(text = f'{ctx.author.display_name} • Page 4 / 4' , icon_url = ctx.author.avatar_url)
        page4.set_thumbnail(url = bot.user.avatar_url)

        page4.add_field(name = '추가중',value= '조금만 기달려주세요.')

        pages = [page1, page2, page3, page4]

        message = await ctx.send(embed = page1)
        await ctx.message.delete()

        await message.add_reaction('\u23ee')
        await message.add_reaction('\u25c0')
        await message.add_reaction('\u274e')
        await message.add_reaction('\u25b6')
        await message.add_reaction('\u23ed')

        i = 0
        emoji = ''

        while True:
                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout=30.0)

                    if user == ctx.author:
                            emoji = str(reaction.emoji)

                            if emoji == '\u23ee':
                                i = 0
                                await message.edit(embed=pages[i])
                            elif emoji == '\u25c0':
                                if i > 0:
                                    i -= 1
                                    await message.edit(embed=pages[i])

                            elif emoji == '\u25b6':
                                if i < 3:
                                    i += 1
                                    await message.edit(embed=pages[i])

                            elif emoji == '\u23ed':
                                i = 3
                                await message.edit(embed=pages[i])

                            elif emoji == '\u274e':

                                await message.delete()

                    if bot.user != user:
                        await message.remove_reaction(reaction, user)

                except asyncio.TimeoutError:
                    break

        await message.clear_reactions()

def setup(bot):
    bot.add_cog(CustomHelp(bot))
