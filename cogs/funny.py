import discord
import asyncio
from discord.ext import commands
import urllib
import requests
from bs4 import BeautifulSoup
import json
import re
import random

class Funny(commands.Cog, name="Funny"):
    """검색 기능"""
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['8ball','마법의 고동'])
    async def _8ball(self, ctx, *, question):

        embed = discord.Embed(title = '마법의 고동', color = discord.Colour.green(), timestamp = ctx.message.created_at)

        embed.set_image(url="https://cdn.discordapp.com/attachments/653867722861445140/659276058507608084/08029efa49dec5e8.jpg")

        embed.set_thumbnail(url=bot.user.avatar_url)
        embed.set_footer(text = f'질문자 : {ctx.author}')

        responses = ['확실합니다.',
                     '100% 장담합니다.',
                     '물론!'
                     '저를 믿으세요, 맞습니다.',
                     '아마도 맞지 않을까요?'
                     '네.',
                     '아니요.',
                     '아닌거같아요',
                     '정확하지 않습니다',
                     '다시 한번 질문해주세요.',]

        embed.add_field(name= "질문: ", value = question, inline=False)

        embed.add_field(name= "답변: ", value = random.choice(responses), inline=False)

        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Funny(bot))
