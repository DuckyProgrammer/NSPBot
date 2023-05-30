import discord
from discord.ext import commands
from discord.utils import get
from discord import app_commands, Embed
from typing import Union
from .util import *

class Roles(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.value = None
    @discord.ui.button(label="Stream Notifications Role", style=discord.ButtonStyle.blurple, custom_id='persistent_view:stream')
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.button):
        user = interaction.user
        roles = user.roles
        hasRole = False
        for role in roles:
            if role.name == "Stream Notification":
                hasRole = True
        if hasRole == True:
            await user.remove_roles(discord.utils.get(interaction.guild.roles, name="Stream Notification"))
            embed = Embed(title = f"Roles Changed", description= f"```You have been removed from the Stream Notification role.```", color = discord.Color.from_rgb(243, 170, 5))
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await user.add_roles(discord.utils.get(interaction.guild.roles, name="Stream Notification"))
            embed = Embed(title = f"Roles Changed", description= f"```You have received the Stream Notification role.```", color = discord.Color.from_rgb(243, 170, 5))
            await interaction.response.send_message(embed=embed, ephemeral=True)
class ButtonRoles(commands.Cog):

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.description = "Stream Notification System"

        self.db = False

    @app_commands.describe(user="Send the button roles embed.")
    @commands.hybrid_command(name="buttonrolesembed", description="Send the button roles embed.")
    @Util.is_mod_check()
    async def _ticketembed(self, ctx: commands.Context, *, discorduser: discord.User = None):
        view = Roles(ctx)
        roleEmbed = discord.Embed(title=f"Stream Notifications", description=f"```Use the button below to add/remove your stream notification role.```", color=0x21cccf)
        await ctx.send(embed=roleEmbed, view=view)
        return await ctx.message.delete()
        #return

async def setup(bot: commands.Bot):
    await bot.add_cog(ButtonRoles(bot))