import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option


class tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Neues Ticket System")
    async def new_ticketsystem(self, ctx,
                               title: Option(str, "Titel"),
                               desc: Option(str, "Beschreibung"),
                               channel: Option(discord.TextChannel, "Channel"),
                               category: Option(discord.CategoryChannel, "Kategorie"),
                               ):
        if title is None:
            title = await ctx.respond("Du musst eine Überschrift angeben.", ephemeral=True)
            return
        if desc is None:
            desc = await ctx.respond("Du musst einen Text angeben.", ephemeral=True)
        if channel is None:
            channel = await ctx.respond("Gib bitte die Channel ID an.", ephemeral=True)
            return
        embed = discord.Embed(
            title=f"{title}",
            description=f"{desc}"
        )
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        channel = await self.bot.fetch_channel(channel)
        await channel.send(embed=embed)
        await ctx.respond(f'{ctx.author.mention} dein Ticket System wurde erfolgreich gesendet.', ephemeral=True)


def setup(bot):
    bot.add_cog(tickets(bot))


class Openview(discord.ui.View):
    def __init__(self, user):
        self.user = user
        super().__init__(timeout=None)

    @discord.ui.Button(label="Claim", style=discord.ButtonStyle.blurple, custom_id="claim")
    async def button_callback(self, button, interaction):
        category = self.client.get_channel()
        await self.interaction.guild.create_text_channel(f"{}")
        await interaction.message_send("User wurde verständigt", ephemeral=True)