import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord import Member
from discord import Embed
import time
import subprocess


class Utilities(commands.Cog):
    """
    General Utilities
    """

    @commands.command()
    async def ping(self, ctx: Context):
        """
        Status check
        """
        start_time = time.time()
        message = await ctx.send('pong. `DWSPz latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms`')
        end_time = time.time()
        await message.edit(content='pong. `DWSP latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms` ' +
                                   '`Response time: ' + str(int((end_time - start_time) * 1000)) + 'ms`')

    @commands.command()
    async def source(self, ctx: Context):
        """
        Print a link to the source code
        """
        await ctx.send(content='Created by `Joel Adams`\n'
                               'https://github.com/JoelLucaAdams/ManPageBot')

    @commands.command()
    async def man(self, ctx: Context, message: str):
        """
        Replies with message
        """
        p1 = subprocess.run(['C:\\Users\\joelu\\AppData\\Local\\Microsoft\\WindowsApps\\ubuntu.exe', '-c', 'man', f'{message}'], capture_output=True)
        msg = p1.stdout.decode()[:1980]
        if p1.returncode != 0:
            await ctx.send("`Status: Bad argument input`")
            return
        embed = Embed(title=message, description=msg, color=discord.Colour.blue())
        embed.set_footer(icon_url=ctx.author.avatar_url, text= f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)
