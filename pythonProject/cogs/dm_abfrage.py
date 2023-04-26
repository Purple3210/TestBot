import discord
from discord.ext import commands
from discord import slash_command

class Dm_abfrage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def info(self, ctx):
        embed = discord.Embed(
            title="Info über den Bot.",
            description="""""",
        )
        ctx.respond(embed=embed)


def setup(bot):
            bot.add_cog(Dm_abfrage(bot))