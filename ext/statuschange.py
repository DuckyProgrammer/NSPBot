import discord
from discord import Streaming, Embed
from discord.ext.commands import errors
from discord.utils import get
from discord.ext import commands
intents = discord.Intents(messages=True, guilds=True, members=True)
client = discord.Client(intents=intents)
class StreamEvent(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.description = "Stream Broadcast"
        self.db = False

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if before.id != 961366939584851978:
            return
        if after.guild.id == 1069570510612082749:
            if before.activity == after.activity:
                return
            channel = discord.utils.get(after.guild.channels, name="stream-broadcasts")
            role_id = 1113214179860561971
            role = discord.utils.get(after.guild.roles, id=role_id)
            if isinstance(after.activity, Streaming):
                #await after.add_roles(role)
                stream_url = after.activity.url
                stream_url_split = stream_url.split(".")
                streaming_service = stream_url_split[1]
                streaming_service = streaming_service.capitalize()
                await channel.send(f"||<@&{role_id}>||\n\nAHOY THERE!!\n\n{stream_url}")
            else:
                return


    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if ctx.author.bot:
            return
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, 'original', error)
        if isinstance(error, errors.CommandNotFound):
            return
        elif isinstance(error, errors.NotOwner):
            tempMessage = await ctx.reply("Permission denied. This is an Owner command, and you are not the owner of this bot.")
            await ctx.message.delete()
            return await tempMessage.delete(delay=5)
        elif isinstance(error, discord.errors.Forbidden):
            return
        elif isinstance(error, errors.CheckFailure):
            tempMessage = await ctx.reply(f"Permission denied. You do not have the appropriate permissions to run this command.")
            await ctx.message.delete()
            return await tempMessage.delete(delay=5)

async def setup(bot: commands.Bot):
    await bot.add_cog(StreamEvent(bot))
