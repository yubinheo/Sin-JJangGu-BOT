import discord
from discord.ext import commands

import asyncio
import datetime
import platform


class Info(commands.Cog, name='정보 Cog'):

    """짱구 봇을 이용해 다양한 정보를 얻어보세요"""

    def __init__(self, bot):
        self.bot = bot
        self.prefix = '짱구야 '


    @commands.command(aliases=['핑'])
    async def Ping(self, ctx):

        em = discord.Embed(colour = discord.Colour.blue())
        em.timestamp = datetime.datetime.utcnow()
        em.set_footer(text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')

        em.add_field(name=':ping_pong: **Pong**!', value=f'__**{round(self.bot.latency * 1000)}ms!**__')

        await ctx.send(embed=em)

    @commands.command(aliases = ['봇정보'])
    async def info_bot(self, ctx):

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        user = len(self.bot.users)
        server = len(self.bot.guilds)

        em = discord.Embed(colour=discord.Colour.blue())
        em.timestamp = datetime.datetime.utcnow()
        em.set_author(name=f'{self.bot.user.name} - 정보', icon_url=self.bot.user.avatar_url)
        em.set_footer(text=f'요청자 - {ctx.author.name}', icon_url=ctx.author.avatar_url)
        em.set_thumbnail(url=self.bot.user.avatar_url)

        em.add_field(name = '접두사(Prefix) :', value = f'`{self.prefix}`', inline = False)
        em.add_field(name = '이름 :', value = f'**{self.bot.user.name}#{self.bot.user.discriminator}\n({self.bot.user.id})**', inline = False)
        em.add_field(name = '<:Python:698093562985840710> 코딩 언어 :',value = '**Python**', inline = False)
        em.add_field(name = '<:Python:698093562985840710> 파이썬 버전 :',value = f'**{pythonVersion}**', inline = False)
        em.add_field(name = '<:discord_py:698416902199836683> 디스코드.py 버전 :',value = f'**{dpyVersion}**', inline = False)
        em.add_field(name = '<:bot_tag:698093696582680586> BOT 서버 및 사용자 :', value = f'**{server}개의 서버와 {user}명이 이용 중.**' , inline = False)
        em.add_field(name = ':birthday: BOT 생성일', value = self.bot.user.created_at.strftime("**%Y년 %m월 %d일**".encode("unicode-escape").decode()).encode().decode("unicode-escape"), inline = False)
        await ctx.send(embed=em)

    @commands.command(aliases = ['유저정보'])
    async def info_user(self, ctx, member : discord.Member = None):

        member = ctx.author if not member else member
        roles = [role for role in member.roles][1:]

        statuses = {'online': '<:online:698093763343548458> 온라인',
        'idle': '<:idle:698093784357142559> 자리비움',
        'dnd': '<:dnd:698093800106623097> 다른 용무 중',
        'offline': '<:offline:698093811364003860> 오프라인'}

        status = statuses[f'{member.status}']

        em = discord.Embed(colour = member.colour)
        em.timestamp = datetime.datetime.utcnow()
        em.set_author(name = f'{member} - 정보', icon_url = member.avatar_url)
        em.set_footer(text = f'요청자 - {ctx.author}', icon_url = ctx.author.avatar_url)

        em.add_field(name = '닉네임 :', value = f'**{member.name}#{member.discriminator}\n({member.id})**', inline = False)
        em.add_field(name = '상태 :', value = str(status), inline = False)
        em.add_field(name = ':birthday: 계정 생성일 :', value = member.created_at.strftime("%Y년 %m월 %d일".encode("unicode-escape").decode()).encode().decode("unicode-escape"), inline = False)
        em.add_field(name = ':inbox_tray: 서버 입장일 :', value = member.joined_at.strftime("%Y년 %m월 %d일".encode("unicode-escape").decode()).encode().decode("unicode-escape"), inline = False)
        em.add_field(name = '역할 :', value = " | ".join([role.mention for role in roles]), inline = False)
        em.add_field(name = '봇 :', value = ('맞습니다' if member.bot else '아닙니다'), inline = False)
        await ctx.send(embed = em)

    @commands.command(aliases = ['서버정보'])
    async def info_server(self, ctx):

        guild = ctx.message.guild

        countrys = {"brazil": ":flag_br: 브라질",
                    "europe": ":flag_eu: 유럽",
                    "hongkong": "flag_hk 홍콩",
                    "india": ":flag_in: 인도",
                    "japan": "flag_jp 일본",
                    "russia": "flag_ru 러시아",
                    "singapore": ":flag_sg: 싱가포르",
                    "southafrica": ":flag_za: 남아메리카",
                    "south-korea": ":flag_kr: 대한민국",
                    "sydeny": ":flag_au: 호주",
                    "us-central": ":flag_us: 미국 중부",
                    "us-east": ":flag_us: 미국 동부",
                    "us-south": ":flag_us: 미국 남부",
                    "us-west": ":flag_us: 미국 서부"
                    }

        region = countrys[f'{guild.region}']

        em = discord.Embed(colour = discord.Colour.blue())
        em.timestamp = datetime.datetime.utcnow()
        em.set_author(name = f"{guild} - 서버 정보 ", icon_url = guild.icon_url)
        em.set_footer(text = f'요청자 - {ctx.author}', icon_url = ctx.author.avatar_url)

        em.add_field(name='서버 주인 :', value=f'**{ctx.guild.owner.display_name}#{ctx.guild.owner.discriminator}\n({ctx.guild.owner.id})**', inline=False)
        em.add_field(name='서버 이름 / 고유 ID :', value=f'**{ctx.guild.name}\n{ctx.guild.id}**', inline=False)
        em.add_field(name='서버 지역 :', value=str(region), inline=False)
        em.add_field(name='서버 생성일 :', value=ctx.guild.created_at.strftime("**%Y년 %m월 %d일**".encode("unicode-escape").decode()).encode().decode("unicode-escape"), inline=False)
        em.add_field(name='서버 채널 수 :', value=f'**카테고리 : {len(guild.categories)}개 | 채팅 : {len(guild.text_channels)}개 | 음성 : {len(guild.voice_channels)}개**', inline=False)
        em.add_field(name='서버 인원 수 :',value=f'**총 인원 : {guild.member_count}명 | 회원 : {len([Member for Member in guild.members if not Member.bot])}명 | 봇 : {len([Member for Member in guild.members if Member.bot])}명**', inline=False)
        em.add_field(name='서버 커스텀 이모지 수:',value = f'{len(guild.emojis)}개 / {guild.emoji_limit}개',inline = False)
        
        await ctx.send(embed = em)
        
    @commands.command(aliases=['서버목록'])
    async def serverlist(self, ctx):
        em = discord.Embed(title=f'{self.bot.user.name} 서버 목록')
        for g in self.bot.guilds:
            em.add_field(name=g.name, value=f'{len(g.members)}명', inline=False)

        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Info(bot))
