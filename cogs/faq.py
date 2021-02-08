import discord
from discord.ext import commands
import json

class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def faq(self, ctx, index=None):
        with open("assets/faq.json", "r", encoding="utf-8") as f:
            faqs = json.load(f)
        if not index:
            msg = "Here is the list of items. Use `a!faq [number]` to get more help.\n"
            for index, entry in enumerate(faqs):
                msg += f"""**{entry["name"]}** - `{index + 1}`\n"""
            await ctx.send(msg)
        else:
            try:
                entry = faqs[int(index) - 1]
                await ctx.send(f"""__**{entry["name"]}**__\n{entry["value"]}""")
            except IndexError:
                await ctx.send(f"The number you gave is out of range! Please give a number between `1` and `{len(faqs)}`!")

def setup(bot):
    bot.add_cog(FAQ(bot))