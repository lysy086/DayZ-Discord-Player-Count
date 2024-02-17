import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests
import asyncio

async def update_status():
    while True:
        resp = requests.get('https://api.battlemetrics.com/servers/25921946')
        resp_dict = resp.json()
        zmienna = resp_dict["data"]["attributes"]["players"]
        zmienna2 = resp_dict["data"]["attributes"]["maxPlayers"]
        activity = discord.Game(name=f"{zmienna} / {zmienna2}", type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        await asyncio.sleep(5)  # Czekaj 5 sekund przed następnym sprawdzeniem

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

@bot.event
async def on_ready():
    print("Bot is ready!")
    await update_status()
    
bot.run('TOKEN')
