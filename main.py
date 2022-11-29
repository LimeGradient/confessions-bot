import disnake
import os

from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

bot = commands.Bot(
    command_prefix='!',
    test_guilds=[1044997386314993715]
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

last_author = ""

@bot.slash_command(name="confess",description="Confess to the server")
async def confess(ctx):
    last_author = ctx.author
    await ctx.response.send_message("Confessing " + last_author)

bot.run(token)
