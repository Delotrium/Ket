import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix= ">")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

client.run("ODEyODI2NjMyMTU4NTc2NjQw.YDGZyg.ytgAR9EB8SfnHJlh2xqY-panhSY")