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
        await ctx.send(f"{ctx.author.mention} asked: {question}\n My reply is: {answers[random.randint(0, len(answers)-1)]}")


    @commands.command(aliases=['kill', 'hunt'])
    async def shoot(self, ctx, member : discord.Member):
        replies = [f'Damn nice shot {ctx.author.mention}. You shot {member.mention} right in the head....',
                   f'{ctx.author.mention}, did you know that was a water gun? You just got {member.mention} all wet... and not in a good way ;)',
                   f'Uhhh... well done {ctx.author.mention}. The gun was the wrong way.... You are very lucky {member.mention}',
                   f'{ctx.author.mention}, your gun was taken by {member.mention} after their quick karate skills, better luck next time.',
                   f'OMG {ctx.author.mention} JUST HIT A 360, NO-SCOPE, WALL JUMP, EYES CLOSED, PLAYING WITH FEET, BUNNY HOP, SHOT ON {member.mention}... MLG!!!!!',
                   f'{member.mention} ran away... maybe don\'t be so fat {ctx.author.mention}.',
                   f'{member.mention} pulled out a bigger gun, you better run {ctx.author.mention}.',
                   f'{ctx.author.mention} did you just hug {member.mention}? That\'s abit weird...',
                   f'A police officer was looking at you {ctx.author.mention}... you have to pay {member.mention} money...',
                   f'{ctx.author.mention} chose kick! It was highly effective! {member.mention} is now half HP!']
        await ctx.send(replies[random.randint(0, 9)])

    @commands.command()
    async def chance(self, ctx, *, query):
        await ctx.send(f"{ctx.author.mention}, there is a {random.randint(1, 100)}% chance that {query}!")

def setup(client):
    client.add_cog(Fun(client))
