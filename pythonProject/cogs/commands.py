import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def give_role(self,
                        member: Option(discord.Member),
                        role: Option(discord.Role)
                        ):
        member.add_roles(role)


def setup(bot):
    bot.add_cog(Commands(bot))