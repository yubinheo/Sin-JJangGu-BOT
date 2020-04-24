import asyncio
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import r6sapi as api
import requests
import time

auth = api.Auth(token='ZG9feXVuZ0BuYXZlci5jb206a2ltZHkzMDExMDEw')


class rainbowsixsiege(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['레식전적', 'r6'])
    async def r6s(self, ctx, *args):
        start = time.time()
        try:
            name = args[0]
            prof = await getr6stat(name)
            ranks = getrank(name)
            tierimg = gettier(ranks['tier'])
            inform = '{0} levels, {1} hours played.'.format(
                prof['level'], prof['played_time'] // 3600)
            info = discord.Embed(colour=discord.Colour.dark_blue(), description=inform)
            info.set_author(name='{}님의 레인보우 식스 시즈 전적 조회'.format(
                prof['name']), icon_url=prof['icon_url'])
            info.set_thumbnail(url=str(tierimg))
            info.add_field(name='# MMR', value=ranks['mmr'], inline=True)
            info.add_field(name='# Tier', value=ranks['tier'], inline=True)
            info.add_field(name='# Max MMR', value=ranks['maxmmr'], inline=True)
            info.add_field(name='# Max Tier', value=ranks['maxtier'], inline=True)
            info.add_field(name='# kills/deaths', value='{0} kills / {1} deaths \nKD : {2}'.format(
                ranks['Kills'], ranks['Deaths'], ranks['KD']), inline=True)
            info.add_field(name='# wins/losses', value='{0} wins / {1} losses / {3} abandons\nWin% : {2}'.format(
                ranks['wins'], ranks['losses'], ranks['win%'], ranks['abandons']), inline=True)
            info.set_footer(text='{0}, Season : {1} | {2} secs.'.format(
                ranks['region'][1:-1], prof['season'], round(time.time() - start, 2)))
            await ctx.channel.send(embed=info)
        except:
            await ctx.channel.send("해당 플레이어의 전적을 조회할 수 없습니다.")

    @commands.command(aliases=['레식시즌'])
    async def r6season(self, ctx, *args):
        player = await auth.get_player(name=args[0], platform=api.Platforms.UPLAY)
        lastedSeason = 17
        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_author(name='{}님의 레인보우 식스 시즈 시즌 티어'.format(player.name), icon_url=player.icon_url)
        for i in range(1, lastedSeason + 1):
            info = str()
            Asia = await player.load_rank(api.RankedRegions.ASIA, season=i)
            EU = await player.load_rank(api.RankedRegions.EU, season=i)
            NA = await player.load_rank(api.RankedRegions.NA, season=i)
            if Asia.rank != 'Unranked':
                info += "\n{0} (ASIA)".format(Asia.rank)
            if EU.rank != 'Unranked':
                info += "\n{0} (EU)".format(EU.rank)
            if NA.rank != 'Unranked':
                info += "\n{0} (NA)".format(NA.rank)
            if info != '':
                embed.add_field(name='# {} season'.format(i), value=info, inline=True)
        await ctx.channel.send(embed=embed)


async def getr6stat(name):
    player = await auth.get_player(name=name, platform=api.Platforms.UPLAY)
    Rank = await player.load_rank(api.RankedRegions.ASIA, season=-1)
    await player.load_level()
    await player.load_general()
    return {
        'id': player.id, 'name': player.name, 'level': player.level, 'played_time': player.time_played, 'icon_url': player.icon_url, 'xp': player.xp, 'season': Rank.season
    }


def getrank(name):
    url = 'https://r6.tracker.network/profile/pc/' + name
    hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
    req = requests.get(url, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    return {
        'KD': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(1) > div.trn-defstat__value')[0].text, 'Kills': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(3) > div.trn-defstat__value')[0].text, 'Deaths': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(4) > div.trn-defstat__value')[0].text, 'win%': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(5) > div.trn-defstat__value')[0].text, 'wins': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(6) > div.trn-defstat__value')[0].text, 'losses': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(7) > div.trn-defstat__value')[0].text, 'abandons': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(8) > div.trn-defstat__value')[0].text, 'tier': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(9) > div.trn-defstat__value')[0].text, 'maxtier': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(10) > div.trn-defstat__value')[0].text, 'mmr': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__info > div:nth-child(3) > div.r6-season-rank > div > div > span')[0].text, 'maxmmr': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__stats > div > div:nth-child(12) > div.trn-defstat__value')[0].text, 'region': soup.select('#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__info > div.r6-season__region')[0].text
    }


def gettier(tier):
    count = 0
    tier = str(tier)
    if tier != 'DIAMOND':
        tier = tier.split()
        tier = tier[0].lower() + str(len(tier[1]))
        result = 'https://r6s-stats.horyu.me/old/{}.png'.format(tier)
        return result
    else:
        tier = tier.lower()
        result = 'https://r6s-stats.horyu.me/old/{}.png'.format(tier)
        return result


def setup(bot):
    bot.add_cog(rainbowsixsiege(bot))
