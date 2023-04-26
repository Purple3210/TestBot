import discord
from discord.ext import commands
from discord.commands import slash_command

class Chatgpt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Chatgpt(bot))