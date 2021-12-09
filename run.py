import logging
import os
import sys
from dotenv import load_dotenv
from src.bot import MyBot


def setup_logging():
    logging.getLogger("discord").setLevel(logging.INFO)
    logging.getLogger("discord.http").setLevel(logging.WARNING)

    log = logging.getLogger()
    log.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "[{levelname:<7}] {name} {funcName} | {message}", style="{")
    handler.setFormatter(formatter)
    log.addHandler(handler)


def main():
    setup_logging()
    load_dotenv()
    token = os.environ["DISCORD_BOT_TOKEN"]
    bot = MyBot(command_prefix="??")
    bot.run(token)


if __name__ == "__main__":
    main()
