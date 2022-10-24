import random
from discord.ext import commands
from discord.commands import slash_command

class ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def witz(self, ctx):
        witze = ["Witz1", "Witz2", "Witz3", "Witz4", "Witz5"]
        witz = random.choice(witze)
        channel = await self.bot.fetch_channel(1033830468723949678)
        await channel.send(witz)
        await ctx.respond("Hier ist dein Witz", ephemeral=True)


def setup(bot):
    bot.add_cog(ticket(bot))