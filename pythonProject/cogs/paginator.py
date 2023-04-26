import discord
from discord.ext import commands
from discord.commands import slash_command

from discord.ext import pages


class Page(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Page(bot))