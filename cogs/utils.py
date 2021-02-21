import discord
from discord.ext import commands

class utils(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("The Playground Discord Bot is online!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined The Playground! ")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left The Playground! ")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test Worked! POGGERS!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"POG! ({(client.latency)*1000}ms)")


    @commands.command(aliases=["purge", "rid"])
    async def clear(self, ctx, amount=5):
        if amount < 1500:
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send("Can only purge 1500 msg at a time!")

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}!")

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}!")

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}!")
                return




def setup(client):
    client.add_cog(utils(client))