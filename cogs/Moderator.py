import discord
from discord.ext import commands


class Moderator(commands.Cog, name='관리자_명령어'):

    """짱구 봇을 이용해 서버를 관리하세요"""

    def __init__(self, bot):
        bot.bot = bot

    @commands.command(aliases=['청소'], help = '불필요한 메세지를 청소 명령어를 통해 삭제하세요.')
    async def clear(self, ctx, *, number: int = None):
        if ctx.message.author.guild_permissions.manage_messages:
            try:
                if number is None:
                    await ctx.send("삭제할 메세지의 개수를 정해주세요!")
                else:
                    deleted = await ctx.message.channel.purge(limit=number)
                    limit = number + 1
                    await ctx.send(f"{ctx.message.author.mention}님의 요청으로 `{len(deleted)}`개의 메세지를 삭제했습니다.")
            except:
                await ctx.send("더 이상 메세지를 삭제 할 수 없습니다.")
        else:
            await ctx.send("관리자가 아닌 경우 명령어를 사용할 수 없습니다.")

    @commands.command(aliases=['킥'], help = '멘션한 멤버를 서버 추방 할 수 있습니다.')
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if user.guild_permissions.manage_messages:
            await ctx.send('해당 이용자는 관리자 이므로 추방 할 수 없습니다.')
        elif ctx.message.author.guild_permissions.kick_members:
            if reason is None:
                await ctx.guild.kick(user=user, reason="None")
                await ctx.send(f'{ctx.author}님이 {user}을 추방했습니다.')
            else:
                await ctx.guild.kick(user=user, reason=reason)
                await ctx.send(f'{ctx.author}님 요청 {user}을 추방했습니다.')
        else:
            await ctx.send('관리자가 아닌 경우 명령어를 사용할 수 없습니다.')

    @commands.command(aliases = ['밴'], help = '해당 맴버를 서버 차단을 할 수 있습니다.')
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if user.guild_permissions.manage_messages:
            await ctx.send("해당 이용자는 관리자 이므로 추방 할 수 없습니다.")
        elif ctx.message.author.guild_permissions.ban_members:
            if reason is None:
                await ctx.guild.ban(user=user, reason="None")
                await ctx.send(f"{user} has been banned.")
            else:
                await ctx.guild.ban(user=user, reason=reason)
                await ctx.send(f"{user} has been banned.")
        else:
            await ctx.send('관리자가 아닌 경우 명령어를 사용할 수 없습니다.')

    @commands.command(aliases = ['언밴'], help = '서버 차단 맴버를 풀어 줄 수 있습니다.')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member.name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @commands.command(aliases = ['뮤트'], help = '서버 이용 제한을 하고 싶으면 이 명령어를 쓰세요.')
    async def mute(self, ctx, member:discord.Member = None):
        role = discord.utils.get(ctx.guild.roles, id = 703835572543946844)
        if not member:
            await ctx.send('해당 멤버를 찾을 수 없습니다.')
            return
        await member.add_roles(role)
        await ctx.send(f'{role} 역할이 추가 되었습니다.')

    @commands.command(aliases = ['언뮤트'], help = '서버 이용 제한 멤버를 풀수 있습니다.')
    async def unmute(self ,ctx, member:discord.Member = None):
        role = discord.utils.get(ctx.guild.roles, id = 703835572543946844)
        if not member:
            await ctx.send('해당 멤버를 찾을 수 없습니다.')
            return
        await member.remove_roles(role)
        await ctx.send(f'{role} 역할이 삭제 되었습니다.')

    @commands.command(aliases = ['밴리스트'], help = '지금까지 밴 된 유저들의 목록입니다!')
    async def show_ban(self, ctx):
        banned_users = await ctx.guild.bans()
        em= discord.Embed(title=f'{ctx.guild.name} 의 밴 목록입니다', colour= discord.Color.red())
        for members in banned_users:
            members = str(members)[9:-1]
            member_list = members.split(' ')
            member_reason = str(member_list[0])[8:-2]
            member_name = str(member_list[3])[6:-1]
            member_discriminator = str(member_list[4])[15:-1]
            print(member_reason)
            if member_reason == 'None':
                member_reason ='없음'
            em.add_field(name = member_name+'#'+member_discriminator,
            value = f'이유 : "{member_reason}"')
        await ctx.send(embed= em)


def setup(bot):
    bot.add_cog(Moderator(bot))
