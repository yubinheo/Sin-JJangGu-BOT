import discord
import requests
from urllib.request import urlopen, Request
import urllib
import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
from discord.ext import commands
import json
import pandas as pd
import geocoder
import re
import time

class COVID19(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('COVID19.py')

    @commands.command(aliases = ['코로나K'])
    async def COVID19_KOREA(self, ctx):
        url = "http://ncov.mohw.go.kr/"
        req = urllib.request.urlopen(url)
        res = req.read()
        soup = BeautifulSoup(res,'html.parser')

        # 확진환자, 완치자, 치료중, 사망자, 지역별 확진현황 크롤링
        keywords = soup.find_all('span',class_='num')
        keywords = [each_line.get_text().strip() for each_line in keywords[:25]]

        embed = discord.Embed(title = '짜증나는 코로나 바이러스 정보야! 질병관리본부 제공해줬어!', colour = discord.Colour.red())
        embed.set_image(url="http://ncov.mohw.go.kr/front_new/modules/img_view.jsp?img_loc=/upload/mwEditor/202002/1582701121732_20200226161201.jpg")
        embed.add_field(name = '확진환자 수', value = keywords[0],inline = True)
        embed.add_field(name = '왼치자(격리해제) 수', value = keywords[1],inline = True)
        embed.add_field(name = '치료중(격리중) 수', value = keywords[2],inline = True)
        embed.add_field(name = '사망자 수', value = keywords[3],inline = True)

        embed.add_field(name = '서울', value = keywords[7],inline = True)
        embed.add_field(name = '부산', value = keywords[8],inline = True)
        embed.add_field(name = '대구', value = keywords[9],inline = True)
        embed.add_field(name = '인천', value = keywords[10],inline = True)
        embed.add_field(name = '광주', value = keywords[11],inline = True)
        embed.add_field(name = '대전', value = keywords[12],inline = True)
        embed.add_field(name = '울산', value = keywords[13],inline = True)
        embed.add_field(name = '세종', value = keywords[14],inline = True)
        embed.add_field(name = '경기', value = keywords[15],inline = True)
        embed.add_field(name = '강원', value = keywords[16],inline = True)
        embed.add_field(name = '충북', value = keywords[17],inline = True)
        embed.add_field(name = '충남', value = keywords[18],inline = True)
        embed.add_field(name = '전북', value = keywords[19],inline = True)
        embed.add_field(name = '전남', value = keywords[20],inline = True)
        embed.add_field(name = '경북', value = keywords[21],inline = True)
        embed.add_field(name = '경남', value = keywords[22],inline = True)
        embed.add_field(name = '제주', value = keywords[23],inline = True)
        embed.add_field(name = '검역 (해외 입국자 현황)', value = keywords[24],inline = False)
        embed.add_field(name = '코로나19 국민 행동요령', value = 'https://www.youtube.com/watch?v=ZFUnG41xJOY&feature=youtu.be',inline = False)
        await ctx.send(embed = embed)

    @commands.command(aliases = ['코로나E'])
    async def COVID19_Earth(self, ctx):
        url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun="
        req = urllib.request.urlopen(url)
        res = req.read()
        soup = BeautifulSoup(res,'html.parser')

        # 국가명 크롤링
        keywords = soup.find_all('td', class_='w_bold')
        keywords = [each_line.get_text().strip() for each_line in keywords[:80]]

        # 확진자, 사망자 크롤링
        keywords2 = soup.find_all('td', class_='')
        keywords2 = [each_line.get_text().strip() for each_line in keywords2[:80]]


        embed = discord.Embed(
            title = '지구촌 코로나19 현황이야! 질병관리본부가 제공해줬어!',
            colour = discord.Colour.red()
        )
        for i in range(0, len(keywords)):
            embed.add_field(name = " ".join(keywords[i].split()), value = " ".join(keywords2[i].split()), inline = False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(COVID19(bot))
