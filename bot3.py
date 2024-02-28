import discord
import asyncio

SERVER_ID = 
TOKEN = ""
CHANNEL_ID = 

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
