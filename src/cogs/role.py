from logging import getLogger
from discord.ext import commands
from src.utils import message

log = getLogger(__name__)


class MyCog(commands.Cog):
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await message.send_pong(ctx.channel)
