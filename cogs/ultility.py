# cogs/utility.py
from discord.ext import commands
import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="time")
    async def get_time(self, ctx):
        """Displays the current server time."""
        now = datetime.datetime.now()
        await ctx.send(f"The current time is {now.strftime('%Y-%m-%d %H:%M:%S')}")

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Checks the bot's latency."""
        latency = round(self.bot.latency * 1000)  # Convert to ms
        await ctx.send(f"Pong! Latency: {latency}ms")

async def setup(bot):
    await bot.add_cog(Utility(bot))
