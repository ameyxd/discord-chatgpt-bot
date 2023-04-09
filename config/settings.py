from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from the .env file

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
GPT_API_KEY = os.environ.get('GPT_API_KEY')
MONGO_CONNECTION_STRING = os.environ.get('MONGO_CONNECTION_STRING')
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
GPT_API_URL = 'https://api.openai.com/v1/chat/completions'
# MONGO_DB_NAME = 'chatgpt_bot'
