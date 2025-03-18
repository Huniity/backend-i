import discord
from dotenv import load_dotenv
import os

# from google import genai

# client = genai.Client(api_key="YOUR_API_KEY")
# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="Explain how AI works"
# )
# print(response.text)

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome {member.name} to my Discord Server!")
    channel = client.get_channel(1117236640327417996)  # Make sure the channel ID is an integer
    embed = discord.Embed(title="NEW MEMBER", description=f"Thanks {member.mention} for joining!")
    embed.set_thumbnail(url=member.display_avatar.url)
    await channel.send(embed=embed)


client.run(os.getenv('DISCORD_TOKEN', None))