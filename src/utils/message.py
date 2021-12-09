import discord


async def send_pong(channel: discord.TextChannel):
    await channel.send("pong")
