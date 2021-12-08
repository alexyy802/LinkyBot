import discord
from discord.ext import commands
from pymongo import MongoClient
import math

bot = commands.Bot(command_prefix="l!")
cluster = MongoClient("MONGO DB CLIENT")
db = cluster["linkydb"]["links"]

@bot.event
async def on_ready():
    print('Linky Is Ready!')

@bot.command()
async def add(ctx,link=None):
    if link == None:
        await ctx.message.add_reaction("🚫")
        return
    else:
        await ctx.send('Link added!')
        addlink = {"id":ctx.author.id, "link":link}
        db.insert_one(addlink)

@bot.command()
async def links(ctx):
    alldata = db.find({})
    for link in alldata:
        links = link["link"]
    e = discord.Embed(title="List of all links",description="desc")
    await ctx.send(embed=e)

@bot.command()
async def test(ctx):
    alldata = db.find({})
    for link in alldata:
        links = link["link"]
    pages = {}
    numOfPages = math.ceil(len(links) / 10)
    j = 0
    for i in range(numOfPages):
        pages[f"page{i}"] = discord.Embed(title=f"Page {i+1}")
        displayUsers = ""
        while j < 10 + i * 10:
            try:
                displayUsers += links[j] + "\n"
            except:
                break
            j += 1
        pages[f"page{i}"].add_field(name="Links:", value=displayUsers)
        await ctx.send(embed=pages[f"page{i}"])


bot.run("UR BOT TOKEN")
