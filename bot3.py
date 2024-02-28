import discord
import asyncio

SERVER_ID = 1212168833859715092
TOKEN = "MTIxMjE1MzEzOTU1NDI5MTgwMg.Gnypzp.26kFNjqUOrNwMaacIh_VUXm6dY9lFZiiU2BrY8"
CHANNEL_ID = 1212168834346393692

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await send_message()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "":
        await message.channel.send("sexo")

async def send_message():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        loop = asyncio.get_event_loop()
        while True:
            user_input = await loop.run_in_executor(None, input, "Type your message: ")
            await channel.send(user_input)
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")

client.run(TOKEN)
