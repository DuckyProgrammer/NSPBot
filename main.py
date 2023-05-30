import discord
from discord.ext import commands, tasks
import logging
from ext.buttonroles import *

extensions = ["jishaku", "ext.buttonroles", "ext.statuschange"]

LOGGER = logging.getLogger("streaming.core")


intents = discord.Intents.all()
intents.members = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="=", intents=intents, slash_commands=True, message_commands=True, allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents().all()
        super().__init__(command_prefix="=!", intents=intents)
    async def setup_hook(self) -> None:
        self.add_view(Roles(bot))
        for extension in extensions:
            try:
                await bot.load_extension(extension)
                LOGGER.info(f"Loaded extension {extension}")

            except:
                LOGGER.exception(f"Failed loading extension {extension}")
        if jsk := bot.get_command("jsk"):
            jsk.hidden = True
bot = PersistentViewBot()


bot.run("")
