# main.py
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Import cogs
from cogs.greetings import Greetings
from cogs.ultility import Utility
from cogs.summoner import Summoner
from cogs.champion_rotations import ChampionRotations

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
async def load_cogs():
    await bot.add_cog(Greetings(bot))
    await bot.add_cog(Utility(bot))
    await bot.add_cog(Summoner(bot))
    await bot.add_cog(ChampionRotations(bot))

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    await load_cogs()

# Run the bot
if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")  # Load your bot token from environment variables
    bot.run(TOKEN)


#TODO: Add news functionality to bot