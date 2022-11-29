import disnake

from disnake.ext import commands

bot = commands.Bot(
    command_prefix='!',
    test_guilds=[1044997386314993715]
)

@bot.slash_command(name="confess",description="Confess to the server")
async def confess(ctx):
    await ctx.response.send_message("Confessing")

bot.run("MTA0NDc0NDMwNTkxNjUyNjY5Nw.GJ0fci.g1WIdx2nTwML59iDEe-RElMDnxHm0kB1_J7Wlg")