import discord
import requests
from urllib.request import urlopen, Request
import urllib
import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
from discord.ext import commands
import json


class Mask(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mask.py')

    @commands.command(aliases=['마스크'])
    async def Mask(self, ctx, *, mask: str):
        maskurl = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'
        region = mask[:52]
        print(region)
        params = {
            'address': str(region)
        }
        res = requests.get(maskurl, params=params)
        json = res.json()
        m = 10000

        stores = json['stores']
        count = json['count']

        data = {
            "addr": [],
            "created_at": [],
            "name": [],
            "store_type": [],
            "remain_stat": [],
        }

        '''
        few: 조금(2개 ~ 29개)
        some: 약간(30 ~ 99개)
        plenty: 많은(100개 이상)
        empty : 매진
        '''
        try:
            embed = discord.Embed(
                title='마스크 정보!',
                colour=discord.Colour.red()
            )

            for store in stores:
                addr = store['addr']
                created_at = store['created_at']
                name = store['name']
                store_type = store['type']
                remain_stat = store.get('remain_stat', '')
                data['addr'].append(addr)
                data['created_at'].append(created_at)
                data['name'].append(name)
                data['store_type'].append(store_type)
                data['remain_stat'].append(remain_stat)
                #print('addr: %s, created_at: %s, name: %s, store_type: %s, remain_stat: %s'%(addr, created_at, name, store_type, remain_stat))
                if str(remain_stat) == "few":
                    embed.add_field(
                        name=name + " ([수량] 2 ~ 29개)", value=addr, inline=False)
                elif str(remain_stat) == "some":
                    embed.add_field(
                        name=name + " ([수량] 30 ~ 99개)", value=addr, inline=False)
                elif str(remain_stat) == "plenty":
                    embed.add_field(
                        name=name + " ([수량] 100개 이상)", value=addr, inline=False)
                elif str(remain_stat) == "empty":
                    embed.add_field(name=name + " (매진됨)",
                                    value=addr, inline=False)

            await ctx.send(embed=embed)

        except:

            embed = discord.Embed(
                title='🔥 Error! 🔥',
                colour=discord.Colour.red()
            )
            embed.add_field(
                name="Error Contents", value="판매처 수집에 오류가 생겼습니다. 상세 주소까지 입력 해 주세요.", inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Mask(bot))
