import discord
from discord.ext import commands
from pymongo import MongoClient
import requests
from config.settings import DISCORD_BOT_TOKEN, GPT_API_KEY, GPT_API_URL, MONGO_CONNECTION_STRING, MONGO_DB_NAME
import aiohttp
import asyncio
import logging

# Configure logging to print log messages to the console with level INFO
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')

# The rest of your bot code...

intents = discord.Intents.default()  # Use default intents
intents.message_content = True
intents.messages = True  # Enable the messages intent
intents.reactions = True  # Enable the reactions intent (if needed)

# Create an instance of the discord bot and specify a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Create a MongoClient instance to connect to MongoDB Atlas
mongo_client = MongoClient(MONGO_CONNECTION_STRING)
db = mongo_client[MONGO_DB_NAME]
interactions = db.interactions

# Define a variable to keep track of the bot's mode (public or private)
bot_mode = 'public'


# Define a command to set the bot to public mode
@bot.command()
async def public(ctx):
    global bot_mode
    bot_mode = 'public'
    await ctx.send('Bot mode set to public.')


# Define a command to set the bot to private mode
@bot.command()
async def private(ctx):
    global bot_mode
    bot_mode = 'private'
    await ctx.send('Bot mode set to private.')


# Function to interact with ChatGPT
import aiohttp
import logging

logger = logging.getLogger(__name__)


async def interact_with_gpt(prompt):
    headers = {
        'Authorization': f'Bearer {GPT_API_KEY}',
        'Content-Type': 'application/json'
    }
    # Format the request body for the Chat API
    data = {
        'model': 'davinci',  # Specify the GPT-3 model to use
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}  # Use the user's prompt as the input message
        ],
        'max_tokens': 100  # Limit the response length
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(GPT_API_URL, headers=headers, json=data) as response:
            response_json = await response.json()
            logger.info(f"API response: {response_json}")  # Log the full API response
            gpt_response = response_json['choices'][0]['message']['content']
            # gpt_response = response_json.get('choices', [{}])[0].get('text', 'No response.')
            if gpt_response == 'No response.':
                logger.error(f"Failed to get a response from ChatGPT. Prompt: {prompt}")  # Log an error message
            return gpt_response.strip()


# Function to store interactions in MongoDB
def store_interaction(interaction_data):
    interactions.insert_one(interaction_data)


# Define a command to interact with ChatGPT
@bot.command()
async def ask(ctx, *, prompt):
    global bot_mode

    # Check if the bot is in private mode and the author is not an admin
    if bot_mode == 'private' and not ctx.author.guild_permissions.administrator:
        await ctx.send('Bot is currently in private mode. Only admins can use this command.')
        return

    # Interact with ChatGPT and send the response
    gpt_response = await interact_with_gpt(prompt)
    await ctx.send(gpt_response)

    # Store the interaction in MongoDB
    interaction_data = {
        'user_id': ctx.author.id,
        'prompt': prompt,
        'response': gpt_response
    }
    store_interaction(interaction_data)


# Run the Discord bot using the bot token
bot.run(DISCORD_BOT_TOKEN)
