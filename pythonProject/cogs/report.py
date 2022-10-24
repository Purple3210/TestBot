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
                     text: Option(str,"Gebe an gegen welche Regel der User verstoßen hat.")
                     ):
        if user is None:
            user = await ctx.respond("Du musst einen User angeben.", ephemeral=True)
            return
        if text is None:
            text = await ctx.respond("Du musst einen Text angeben.", ephemeral=True)
            return
        channel = await self.bot.fetch_channel(1033103895368577105)
        await channel.send(f'{ctx.author.mention} hat den User {user.mention} gemeldet: {text}')
        await ctx.respond(f'{ctx.author.mention} dein Report wurde erfolgreich gesendet.', ephemeral=True)


def setup(bot):
    bot.add_cog(report(bot))
