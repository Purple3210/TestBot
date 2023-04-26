import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ext.pages import Paginator, Page


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def page(self, ctx):
        pages = [
            Page(embeds=[discord.Embed(title="Du", color=discord.Color.yellow())]),
            Page(embeds=[discord.Embed(title="stinkst", color=discord.Color.yellow())])
        ]
        paginator = Paginator(pages=pages)

        await paginator.respond(ctx.interaction)


def setup(bot):
    bot.add_cog(Warn(bot))