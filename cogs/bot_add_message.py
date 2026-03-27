from ctypes import pythonapi
import re
import discord
from discord.ext import commands

class BotAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = discord.Embed(
            description=(
                "### Thank you for inviting me!\n\n"
                "I'm **Haiku Bot**. I detect Haikus — and sometimes, successfully!\n\n"
                "**I will now be listening to all messages for Haikus.** If you don't want that, use `/haiku detection disable` or simply remove me from your server.\n\n"
                "-# I'm open-source! If you want to host me on your own computer, check out the GitHub repository by [clicking here]()."
            ),
            color=discord.Color(0x944ae8)
        )

        embed.set_author(
            name="Haiku Bot — by Dopamine Studios",
            icon_url=self.bot.user.display_avatar.url
        )
        embed.set_footer(text="A Dopamine Studios product.")

        target_channel = None
        keywords = ["general", "chat", "lounge", "gc"]
        nono = ["admin"]
        for channel in guild.text_channels:
            if any(word in channel.name.lower() for word in keywords):
                if not any(word in channel.name.lower() for word in nono):
                    if channel.permissions_for(guild.me).send_messages:
                        target_channel = channel
                        break

        if not target_channel:
            if guild.system_channel and guild.system_channel.permissions_for(guild.me).send_messages:
                target_channel = guild.system_channel

        if not target_channel:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    target_channel = channel
                    break

        if target_channel:
            await target_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(BotAdd(bot))