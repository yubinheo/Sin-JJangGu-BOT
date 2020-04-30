import discord
from discord.ext import commands
import datetime

class Basics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print('General.py')

    @commands.command(aliases = ['명령어'])
    async def command(self, ctx):
        await ctx.send ('짱구 BOT 명령어는 링크를 통해 확인 할 수 있습니다. https://discord.gg/8CKtcQC')

    @commands.command(aliases = ['초대'])
    async def invite(self, ctx):
        invite = discord.Embed(title = f'{self.bot.user.name}을 초대하고 싶은가요?', colour = discord.Colour.blue())
        invite.timestamp = datetime.datetime.utcnow()
        invite.add_field(name = '관리자 역할로 초대하기', value = '[Text link](https://discordapp.com/api/oauth2/authorize?client_id=696508188584968272&permissions=8&scope=bot)', inline = False)
        invite.add_field(name = '추천 역할로 초대하기', value = '[Text link](https://discordapp.com/oauth2/authorize?client_id=696508188584968272&permissions=1103588416&scope=bot)', inline = False)

        await ctx.send(embed = invite)
       
    @commands.command(aliases = ['문의'])
    async def question(self, ctx):
        embed = discord.Embed(title = f'{self.bot.user.name} 공식 디스코드', url = 'https://discord.gg/dn9MbUp',description ='여기로 가면 문의를 할 수 있습니다!', colour = discord.Colour.blue())
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Basics(bot))
