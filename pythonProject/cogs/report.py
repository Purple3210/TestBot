import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option


class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Reporte einen User!")
    async def report(self, ctx,
                     user: Option(discord.Member, "Gib einen User an"),
                     text: Option(str, "Gebe an gegen welche Regel der User verstoßen hat.")
                     ):
        if user is None:
            user = await ctx.respond("Du musst einen User angeben.", ephemeral=True)
            return
        if text is None:
            text = await ctx.respond("Du musst einen Text angeben.", ephemeral=True)
            return
        embed = discord.Embed(
            title=f"Report von {ctx.author}",
            description=f"""Der User {ctx.author.mention} hat den User {user.mention} reportet:
                            [{ctx.author.mention}]: {text}
"""
        )
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        channel = await self.bot.fetch_channel(1033103895368577105)
        await channel.send(embed=embed, view=Controlview(self.user))
        await ctx.respond(f'{ctx.author.mention} dein Report wurde erfolgreich gesendet.', ephemeral=True)


def setup(bot):
    bot.add_cog(report(bot))


class Controlview(discord.ui.View):
    def __init__(self, user):
        self.user = user
        super().__init__(timeout=None)

    @discord.ui.button(label="Claim", style=discord.ButtonStyle.blurple)
    async def button_callback(self, button, interaction):
        embed2 = discord.Embed(
            title=f"Hallo,",
            description="Bitte begebe dich umgehend in den **Support**!"
        )
        embed2.set_thumbnail()
        await interaction.user.send(embed=embed2)
