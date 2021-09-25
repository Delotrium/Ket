import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=true)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit=amount+1)


    @command.command(aliases=['purge.all', 'clear.all'])
    @commands.has_permissions(manage_messages=true)
    async def clearall(self, ctx):
        await ctx.channel.purge()

def setup(client):
    client.add_cog(Moderation(client))
