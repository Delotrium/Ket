import discord
from discord.ext import commands

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pm"])
    async def dm(self, ctx, member : discord.Member, *, message):
        await member.send(message + f"\n ``From {ctx.author}``")
        Author = ctx.author
        await Author.send("\""+ message + f"\" was sent to {member}!")



    @commands.command(aliases=['joinvc', 'vc'])
    async def invitevc(self, ctx, member : discord.Member, *, topic):
        inv = await ctx.author.voice.channel.create_invite()
        await member.send(f"``{ctx.author}`` ***has asked you to join the voice chat!***\n Invite: {inv}\nMessage from ``{ctx.author}`` is:\n*``{topic}``*")
        Author = ctx.author
        await Author.send(f"Invite was sent to {member}!")

def setup(client):
    client.add_cog(Tools(client))
