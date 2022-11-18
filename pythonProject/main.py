import os

import discord
from discord.commands import Option
from dotenv import load_dotenv
import config

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


status = discord.Status.online
activity = discord.Activity(type=discord.ActivityType.playing, name="Python")

client = discord.Bot(intents=intents, debug_guilds=None, status=status, activity=activity)


@client.event
async def on_ready():
    print("------------")
    print(f"{client.user} ist online!")
    print("Pycord Version: "+discord.__version__)
    print("------------")
    print(f"{filename} " + config.load_message)


@client.slash_command(description="Lass den Bot eine Nachricht senden")
async def say(
        ctx,
        text: Option(str, "Der Text, den du senden möchtest"),
        channel: Option(discord.TextChannel, "Der Channel, in den du die Nachricht senden möchtest")
):
    await channel.send(text)
    await ctx.respond("Nachricht gesendet", ephemeral=True)


@client.slash_command(description="Stalke einen User :P", name="userinfo")
async def info(
        ctx,
        user: Option(discord.Member, "Gib einen User an", default=None)
):
    if user is None:
        user = ctx.author

    embed = discord.Embed(
        title=f"Hier siehst du alle Infos über {user.name}",
        description=f"Hier siehst du alle Infos über {user.mention}",
        color=discord.Color.blue()
    )

    time = discord.utils.format_dt(user.created_at, "R")

    embed.add_field(name="Account erstellt", value=time, inline=False)
    embed.add_field(name="ID", value=user.id)

    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text="Bot erstellt von @maddib | Purple#3265")

    await ctx.respond(embed=embed)


@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Willkommen",
        description=f"Hallo {member.mention}",
        color=discord.Color.green()
    )

    channel = await client.fetch_channel(1033102371657617420)
    await channel.send(embed=embed)

if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")

    load_dotenv()
    client.run(os.getenv("TOKEN"))
