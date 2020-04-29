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
import datetime

class COVID19(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('COVID19.py')

    @commands.command(aliases = ['코로나현황'])
    async def COVID19_KOREA(self, ctx):
        url = "http://ncov.mohw.go.kr/"
        req = urllib.request.urlopen(url)
        res = req.read()
        soup = BeautifulSoup(res,'html.parser')

        # 확진환자, 완치자, 치료중, 사망자, 지역별 확진현황 크롤링
        keywords = soup.find_all('span',class_='num')
        keywords = [each_line.get_text().strip() for each_line in keywords[:25]]

        em = discord.Embed(title = 'COVID-19 대한민국 현황', colour = discord.Colour.red())
        em.timestamp = datetime.datetime.utcnow()
        em.set_footer(text = '출처 : 질병관리본부', icon_url = 'https://cdn.discordapp.com/attachments/704609288655470593/704610900190953472/6a162e5fe3d0dd61.jpg')
        em.add_field(name = '확진환자 수 :', value = keywords[0],inline = False)
        em.add_field(name = '왼치자(격리해제) 수 :', value = keywords[1],inline = False)
        em.add_field(name = '치료중(격리중) 수 :', value = keywords[2],inline = False)
        em.add_field(name = '사망자 수 :', value = keywords[3],inline = False)
        em.add_field(name = '코로나19', value = '[코로나19 국민 행동요령](https://www.youtube.com/watch?v=ZFUnG41xJOY&feature=youtu.be)', inline = False)

        await ctx.send(embed = em)

    @commands.command(aliases = ['코로나_대도시'])
    async def COVID19_metropolitan_city(self, ctx):
        url = "http://ncov.mohw.go.kr/"
        req = urllib.request.urlopen(url)
        res = req.read()
        soup = BeautifulSoup(res,'html.parser')

        # 확진환자, 완치자, 치료중, 사망자, 지역별 확진현황 크롤링
        keywords = soup.find_all('span',class_='num')
        keywords = [each_line.get_text().strip() for each_line in keywords[:25]]

        embed = discord.Embed(title = 'COVID-19 대도시 지역별 현황', colour = discord.Colour.red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text = '출처 : 질병관리본부', icon_url = 'https://cdn.discordapp.com/attachments/704609288655470593/704610900190953472/6a162e5fe3d0dd61.jpg')

        embed.add_field(name = '광역시 현황', value = f'서울 특별시 : {keywords[7]}명\n부산광역시 : {keywords[8]}명\n대구광역시 : {keywords[9]}명\n인천광역시 : {keywords[10]}명\n광주광역시 : {keywords[11]}명\n대전광역시 : {keywords[12]}명\n울산광역시 : {keywords[13]}명\n세종특별자치시 : {keywords[14]}명', inline = False)
        embed.add_field(name = '도 현황', value = f'경기도 : {keywords[15]}명\n강원도 : {keywords[16]}명\n충청북도 : {keywords[17]}명\n충청남도 : {keywords[17]}명\n전라북도 : {keywords[19]}명\n전라남도 : {keywords[20]}명\n경상북도 : {keywords[21]}명\n경상남도 : {keywords[22]}명\n 제주특별자지도 : {keywords[23]}명', inline = False)
        embed.add_field(name = '코로나19', value = '[코로나19 국민 행동요령](https://www.youtube.com/watch?v=ZFUnG41xJOY&feature=youtu.be)', inline = False)

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


        embed = discord.Embed(title = '지구촌 코로나19 현황이야! 질병관리본부가 제공해줬어!', colour = discord.Colour.red())
        for i in range(0, len(keywords)):
            embed.add_field(name = " ".join(keywords[i].split()), value = " ".join(keywords2[i].split()), inline = False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(COVID19(bot))
