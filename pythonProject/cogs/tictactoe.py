import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import option


class Tictactoe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def start_tictactoe(self, ctx):
        embed = discord.Embed(
            title=f"TicTacToe von {ctx.author}",
            description=f"""
            |---|---|---|
            |---|---|---|
            |---|---|---|
"""
        )
        await ctx.respond(embed=embed, view=selectview)


def setup(bot):
    bot.add_cog(Tictactoe(bot))


class selectview(discord.ui.View):
    @discord.ui.button(label=".", style=discord.ButtonStyle.primary, emoji="<:oben_links:1039609734195576844>")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("")

