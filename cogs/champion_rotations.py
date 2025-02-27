import os
from discord.ext import commands
from dotenv import load_dotenv
from data.get_champion_rotations import get_champion_rotations, get_champion_data, get_champion_name

load_dotenv()

class ChampionRotations(commands.Cog):
    def __init__(self, bot):
        API_KEY = os.getenv("DEVELOPMENT_API_KEY")

        self.riot_api_key = API_KEY
        self.bot = bot

    @commands.command(name="champion_rotations")
    async def champion_rotations(self, ctx, region: str):
        """Get the current champion rotations from the Riot Games API."""
        rotations = get_champion_rotations(region=region, api_key=self.riot_api_key)
        champion_data = get_champion_data()
        rotation_ids = rotations["freeChampionIds"]
        free_champions = [get_champion_name(champion_id, champion_data) for champion_id in rotation_ids]
        await ctx.send(f"Free champions: {', '.join(free_champions)}")

async def setup(bot):
    await bot.add_cog(ChampionRotations(bot))