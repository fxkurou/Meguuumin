# cogs/greetings.py
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def say_hello(self, ctx):
        """Responds with a greeting."""
        await ctx.send(f"Hello, {ctx.author.name}!")

    @commands.command(name="goodbye")
    async def say_goodbye(self, ctx):
        """Sends a farewell message."""
        await ctx.send("Goodbye! Have a great day!")

async def setup(bot):
    await bot.add_cog(Greetings(bot))
