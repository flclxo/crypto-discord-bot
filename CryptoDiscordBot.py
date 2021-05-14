import requests
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import discord
import time
import random
import urllib.request
from requests.sessions import Session
import json


client = commands.Bot(command_prefix='!')



@client.event
async def on_ready():
    print('Bot is online')


@client.command()
async def anime(wafi):
    #!anime to use 
    anime = requests.get("https://animechan.vercel.app/api/random")

 
    recall1 = anime.json()['anime']
    recall2 = anime.json()['character']
    recall3 = anime.json()['quote']
    

    await wafi.send("Anime Show :  " + recall1 + " | " + " Character: " + recall2 + " | " + " Quote:  " + recall3)

@client.command()
async def image(wafi):
    #!image to use
    image = requests.get("https://api.waifu.pics/sfw/waifu")

 
    recall1 = image.json()['url']
    

    await wafi.send("Image: " + recall1)

@client.command()
async def sadimage(wafi):
    #!sadimage to use
    sad = requests.get("https://api.waifu.pics/sfw/happy")

 
    recall1 = sad.json()['url']
    

    await wafi.send("Image: " + recall1)

@client.command()
async def btc(wafi):
    #!btc to use
    data = urllib.request.urlopen("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&order=id_dsc&per_page=1&page=1&sparkline=false").read()

 
    btc = json.loads(data)
    output_dict = btc
    recall1 = str((output_dict[0]['name']))
    recall2 = str((output_dict[0]['current_price']))
    recall3 = str((output_dict[0]['low_24h']))
    recall4 = str((output_dict[0]['ath']))

    embed = discord.Embed(title="Cyrpto Bot", description="", color=0xff951c)
    
    embed.set_footer(text="Bot made by @flclxo (m4tro)")
    embed.set_thumbnail(url="https://marxistdegeneracy.files.wordpress.com/2018/04/anime-bitcoin.jpg")
    await wafi.channel.send(embed=embed)
    

    await wafi.send("Token: " + recall1+ " | "+ " Current Price: " + recall2 + " | " + "24 Hour Low: " + recall3 + " | " + "ATH: " + recall4)

@client.command()
async def doge(wafi):
    #!doge to use
    data = urllib.request.urlopen("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=dogecoin&order=id_dsc&per_page=1&page=1&sparkline=false").read()

 
    doge = json.loads(data)
    output_dict = doge
    recall1 = str((output_dict[0]['name']))
    recall2 = str((output_dict[0]['current_price']))
    recall3 = str((output_dict[0]['low_24h']))
    recall4 = str((output_dict[0]['ath']))

    embed = discord.Embed(title="Cyrpto Bot", description="", color=0xe7f03e)
    
    embed.set_footer(text="Bot made by @flclxo (m4tro)")
    embed.set_thumbnail(url="http://40.media.tumblr.com/e2ab4591b6e47a3b9bcf195f997326bc/tumblr_no642wHmZG1qa26muo1_500.png")
    await wafi.channel.send(embed=embed)
    

    await wafi.send("Token: " + recall1+ " | "+ " Current Price: " + recall2 + " | " + "24 Hour Low: " + recall3 + " | " + "ATH: " + recall4)


@client.command()
async def eth(wafi):
    #!eth to use
    data = urllib.request.urlopen("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=id_dsc&per_page=1&page=1&sparkline=false").read()
    eth = json.loads(data)
    output_dict = eth
    recall1 = str((output_dict[0]['name']))
    recall2 = str((output_dict[0]['current_price']))
    recall3 = str((output_dict[0]['low_24h']))
    recall4 = str((output_dict[0]['ath']))
    
    embed = discord.Embed(title="Crypto Bot", description="", color=0x0044ff)
    
    embed.set_footer(text="Bot made by @flclxo (m4tro)")
    embed.set_thumbnail(url="https://wallpapercave.com/wp/wp6004749.jpg")
    await wafi.channel.send(embed=embed)

    

    await wafi.send("Token: " + recall1+ " | "+ " Current Price: " + recall2 + " | " + "24 Hour Low: " + recall3 + " | " + "ATH: " + recall4)

client.run('TOKEN HERE')
    
    
