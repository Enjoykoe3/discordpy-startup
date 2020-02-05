from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='~')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ontest(ctx):
    await ctx.send('テストに成功しました！オンラインになっています')

bot.run(token)


@bot.command()
async def hey(ctx):
    await ctx.send('やあ！こんにちは！')
