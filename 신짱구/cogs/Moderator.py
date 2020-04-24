import discord
from discord.ext import commands

class Moderator(commands.Cog):

    def __init__(self, bot):
        bot.client = bot

    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderator.py')

    #Command
    @commands.command(aliases = ['청소'])
    async def clear(self, ctx, *, number:int = None):
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

    @commands.command(aliases = ['킥'])
    async def kick(self, ctx, user: discord.Member, *, reason = None):
        if user.guild_permissions.manage_messages:
            await ctx.send('해당 이용자는 관리자 이므로 추방 할 수 없습니다.')
        elif ctx.message.author.guild_permissions.kick_members:
            if reason is None:
                await ctx.guild.kick(user=user, reason = "None")
                await ctx.send(f'{ctx.author}님이 {user}을 추방했습니다.')
            else:
                await ctx.guild.kick(user=user, reason=reason)
                await ctx.send(f'{ctx.author}님 요청 {user}을 추방했습니다.')
        else:
            await ctx.send('관리자가 아닌 경우 명령어를 사용할 수 없습니다.')

    @commands.command()
    async def ban(self, ctx, user:discord.Member, *, reason=None):
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

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member.name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @commands.command()
    async def mute(self, ctx):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name = 'Mute')
        await author.add_roles(role)

    @commands.command()
    async def unmunt(self, ctx):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name='Mute')
        await author.remove_roles(role)

def setup(bot):
    bot.add_cog(Moderator(bot))
