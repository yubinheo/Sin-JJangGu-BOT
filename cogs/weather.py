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

class weather(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('weather.py')

    @commands.command(aliases = ['날씨'])
    async def weather(self, ctx, *,mes:str):
        region = mes[:13]
        enregion = parse.quote(region + "+날씨")

        url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enregion
        print(url)

        req = urllib.request.urlopen(url)
        res = req.read()
        soup = BeautifulSoup(res,'html.parser')

        weather_todaytemp = soup.find_all('span', class_='todaytemp')
        weather_todaytemp = [each_line.get_text().strip() for each_line in weather_todaytemp[:20]]

        weather_cast_txt = soup.find_all('p', class_='cast_txt')
        weather_cast_txt = [each_line.get_text().strip() for each_line in weather_cast_txt[:20]]

        weather_region = soup.find_all('span', class_='btn_select')
        weather_region = [each_line.get_text().strip() for each_line in weather_region[:20]]

        try:
            embed = discord.Embed(
                title = '💨 오늘의 날씨 [ ' + region + ' ]',
                colour = discord.Colour.blue()
            )
            embed.add_field(name = "측정 지역(상세)", value = str(weather_region[0]) + "℃", inline = False)
            embed.add_field(name = "오늘 온도 (℃)", value = str(weather_todaytemp[0]) + "℃", inline = False)
            embed.add_field(name = "상세 정보", value = weather_cast_txt[0], inline = False)
            await ctx.send(embed=embed)

        except:

            embed = discord.Embed(
                title = '🔥 Error! 🔥',
                colour = discord.Colour.red()
            )
            embed.add_field(name = "Error Contents", value = "날씨정보 수집에 오류가 생겼습니다.", inline = False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(weather(bot))
