import os
os.system("pip install discord.py==1.7.3")
import discord, asyncio, datetime, pytz,keepalive


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='+',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "sam", url = "https://www.twitch.tv/#"))


keepalive.keepalive()
client.run(os.getenv("token"), bot=False)
#Now press f5 to run the project
#credit of project goes to me 
