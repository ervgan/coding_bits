import discord
import random
import requests
import json


async def send_message(message):
  try:
      response = f"Hello {message.author.name}!"
      await message.channel.send(response)
  except Exception as e:
     print(e)

async def send_random_quote(channel):
    response = requests.get("https://dummyjson.com/quotes")
    if response.status_code == 200:
        quotes = json.loads(response.text)
        quotes_list = quotes["quotes"]
        random_quote = random.choice(quotes_list)
        await channel.send(random_quote['quote'])

def run_discord_bot():
    TOKEN= ""
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
      print(f"{client.user} is now running!")

    @client.event
    async def on_message(message):
      if message.author == client.user:
        return
      if message.content == 'hello':
        await send_message(message)

      elif message.content == '!quote':
        await send_random_quote(message.channel)

    client.run(TOKEN)

