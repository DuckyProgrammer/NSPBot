import discord
from discord.ext import commands
from typing import Union

def mod_check(ctx: Union[commands.Context, discord.Interaction]):
    if ctx.guild is None: return False

    if isinstance(ctx, commands.Context):
        user = ctx.author
    else:
        user = ctx.user

    #if user.id == 232950078514397186: return True - From debugging and creation. Line is disabled.
    if user.id == 961366939584851978: return True

    return False

class Util(commands.Cog):

    def is_mod_check():
        return commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True), commands.check(mod_check))

async def setup(bot: commands.Bot):
    cog = Util(bot)
    await bot.add_cog(cog)