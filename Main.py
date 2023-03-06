import discord
import openai
import os

# Set up OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Set up Discord client
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Ignore messages sent by the bot
    if message.author == client.user:
        return

    # Generate a response using OpenAI
    prompt = f'{message.content}\n'
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text.strip()

    # Send the response back to the user
    await message.channel.send(response)

# Start the bot
client.run('YOUR_DISCORD_BOT_TOKEN')
