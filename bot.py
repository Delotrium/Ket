import discord
from discord.ext import commands

client = commands.Bot(command_prefix= ">")

@client.event 
async def on_ready():
    print("The Playground Discord Bot is online!")

client.run("ODEyODI2NjMyMTU4NTc2NjQw.YDGZyg.QjX-VfCMVFWAJXPWyabgU-_rMSw")