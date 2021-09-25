import discord
from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', '8b'])
    async def eightball(self, ctx, *, question):
        answers = ['It is certain',
                   'It is decidedly so', 
                   'Without a doubt', 
                   'Yes – definitely', 
                   'You may rely on it', 
                   'As I see it, yes', 
                   'Most likely', 
                   'Outlook good', 
                   'Yes Signs point to yes', 
                   'Reply hazy', 
                   'try again', 
                   'Ask again later', 
                   'Better not tell you now', 
                   'Cannot predict now', 
                   'Concentrate and ask again', 
                   'Dont count on it', 
                   'My reply is no', 
                   'My sources say no', 
                   'Outlook not so good', 
                   'Very doubtful']
        await ctx.send(f"{ctx.author.mention} asked: {question}\n My reply is: {answers[random.randint(1, len(answers)-1)]}")



def setup(client):
    client.add_cog(Fun(client))
