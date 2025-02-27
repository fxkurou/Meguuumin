import os

from discord.ext import commands
from data.get_summoner import get_summoner
from dotenv import load_dotenv

load_dotenv()

class Summoner(commands.Cog):
    def __init__(self, bot):
        RIOT_API_KEY = os.getenv("RIOT_API_KEY")
        self.riot_api_key = RIOT_API_KEY
        self.bot = bot

    @commands.command(name="summoner")
    async def summoner(self, ctx, region, summoner_name):
        """Get summoner information from the Riot Games API."""
        res = get_summoner(region, summoner_name, self.riot_api_key)
        await ctx.send(f"{res}")

async def setup(bot):
    await bot.add_cog(Summoner(bot))