import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='ket!')

#Change Status:
@client.command()
async def status(ctx, *, stat):
    whitelist = [433159491404693514, 708113653940879502]
    if ctx.author.id in whitelist:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(stat))
    else:
        await ctx.send(f"Sorry {ctx.author.mention}, but you have contact the owner of the bot (delotrium) to change my status!")



@client.command()
async def load(ctx, extension):
    client.load_extension(f"src.{extension}")

@client.command()
async def   unload(ctx, extension):
    client.unload_extension(f"src.{extension}")

for filename in os.listdir('DiscordBot\src'):
    if filename.endswith('.py'):
        client.load_extension(f"src.{filename[:-3]}")



client.run("")
