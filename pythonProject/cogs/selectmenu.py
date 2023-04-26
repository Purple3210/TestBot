import discord
from discord.ext import commands
from discord.commands import slash_command

class Dropdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @slash_command()
        async def select1(self, ctx):
            await ctx.respond("Wähle Sprache.", view=Tutview)

def setup(bot):
    bot.add_cog(Dropdown(bot))


class Tutview(discord.ui.View):
    options = [
        discord.SelectOption(label="Python", description="Python Beschreibung"),
        discord.SelectOption(label="Javascript", description="JS")
    ]
    @discord.ui.select(
        min_values=1,
        max_values=2,
        placeholder="Triff eine Auswahl",
        options=options
    )
    async def select_callback(self, select, interaction):
        s = ""
        for auswahl in select.values:
            s += f"- {auswahl}\n"

        await interaction.response.send_message(f"Du hast folgendes ausgewählt:\n{s}")