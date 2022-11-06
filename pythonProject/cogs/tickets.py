import discord.ui
from discord.commands import slash_command
from discord.ext import commands


class tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def embed(self, ctx):
        modal = testmodal(title="Erzeuge ein Embed")
        await ctx.send_modal(modal)


def setup(bot):
    bot.add_cog(tickets(bot))


class testmodal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Embed",
                placeholdere="Placeholder"
            )
            * args,
            **kwargs
        )
