import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class Soup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["define.urban", 'urban', 'search.urban', 'uban.dictionary'])
    async def define_urban(self, ctx, *, query):
        url = f"https://www.urbandictionary.com/define.php?term={query}"
        
        result=requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        try:
            article = doc.find('div', class_="meaning").text
            await ctx.send(f"{ctx.author.mention}, The definition of {query} on the urban dictionary is:\n{article}")
        except:
            await ctx.send(f"{ctx.author.mention}:\n We could not find \"{query}\" on the urban dictionary!")



def setup(client):
    client.add_cog(Soup(client))
