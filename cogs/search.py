import discord
import asyncio
from discord.ext import commands
import urllib
import requests
from bs4 import BeautifulSoup
import json
import re
import random

class Search(commands.Cog, name="Search"):
    """검색 기능"""
    def __init__(self,bot):
        self.client = bot

    delList =  list()
    is_wordend = False
    wordDict = dict()
    alreadySet =  set()
    onewords = set()
    lastWord=''
    firstLetter=''
    nextWords=''
    firstTurn = False
    round = 0
    score = 0

    @commands.command(aliases=['이미지검색'], help='네이버에서 이미지를 검색해드려요!')   #네이버에서 이미지 검색
    async def searchimg(self,ctx,*, img):
        try:
            num=int(img[-1])
            img=img[:-1]
        except:
            num =0
        finally:
            url= 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='+img
            print(url)
            params = {'query' : '파이썬'}
            header_info={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
            response = requests.get(url, headers=header_info, params=params)
            images = BeautifulSoup(response.content, 'html.parser')
            images = images.find_all('img', class_='_img')
            data_images=[]
            for link in images:
                data_images.append(link.get('data-source'))
            embed= discord.Embed(name=img, color=discord.Color(0x72e3ef))
            embed.set_image(url=data_images[num])
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Search(bot))
