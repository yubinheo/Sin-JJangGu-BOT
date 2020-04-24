import discord
from discord.ext import commands
import urllib
import requests
from bs4 import BeautifulSoup
class Imgsearch(commands.Cog):
    def __init__(self,bot):
        self.clinet = bot

    @commands.command(aliases=['이미지검색'])
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
            images = BeautifulSoup(response.content, 'lxml')
            images = images.find_all('img', class_='_img')
            data_images=[]
            for link in images:
                data_images.append(link.get('data-source'))
            embed= discord.Embed(name=img, color=discord.Color(0x72e3ef))
            embed.set_image(url=data_images[num])
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Imgsearch(bot))