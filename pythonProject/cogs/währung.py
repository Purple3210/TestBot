import discord
from discord.ext import commands
from discord.commands import slash_command

import aiosqlite
import random


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.DB = "economy.db"

    @staticmethod
    def get_balance(credits):
        balance = 1
        amount = 100

        while True:
            credits -= amount
            if credits < 0:
                return balance
            balance += 1
            amount += 100

    @commands.Cog.listener()
    async def on_ready(self):
        async with aiosqlite.connect(self.DB) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                msg_count INTEGER DEFAULT 0,
                credits INTEGER DEFAULT 0
                )"""
            )


def setup(bot):
    bot.add_cog(Economy(bot))
