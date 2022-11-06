import discord
from discord.ext import commands
from discord.commands import slash_command


class Menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def menu1(self, ctx):
        embed = discord.Embed(
            title="Menu",
            description="You can choose between 2 Levels!",
            color=discord.Color.light_gray()
        )
        embed.set_footer(text="Game created by Purple")
        await ctx.respond(embed=embed, view=TutorialView())


class TutorialView(discord.ui.View):
    @discord.ui.button(label="Mission 1", style=discord.ButtonStyle.blurple)
    async def button_callback(self, button, interaction):
        embed1 = discord.Embed(
            title="Der Anfang.",
            description="You are stranded with your team"
        )
        await interaction.response.send_message(embed=embed1)


def setup(bot):
    bot.add_cog(Menu(bot))
