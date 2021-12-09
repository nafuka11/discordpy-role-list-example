from logging import getLogger
from discord.ext import commands
from src.cogs.my_cog import MyCog

log = getLogger(__name__)


class MyBot(commands.Bot):
    async def on_ready(self):
        log.info(f"Ready: {self.user}")
        log.info(f"guilds: {self.guilds}")
        self.add_cog(MyCog())
