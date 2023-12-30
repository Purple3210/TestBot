from discord.ext import commands
from discord.commands import slash_command


class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def nick(self, ctx):
        await ctx.respond("NickyNick17")


def setup(bot):
    bot.add_cog(Cooldown(bot))
