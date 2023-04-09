"""
Project: discord-chatgpt-bot
Author: ameyxd
Copyright (c) 2023 Amey Ambade
Description: Test connections to the services used
"""
import unittest
from pymongo import MongoClient
import requests
from config.settings import DISCORD_BOT_TOKEN, GPT_API_KEY, GPT_API_URL, MONGO_CONNECTION_STRING, MONGO_DB_NAME


class TestConnections(unittest.TestCase):
    def test_discord_connection(self):
        # Check if the Discord bot token is set and is not empty
        self.assertIsNotNone(DISCORD_BOT_TOKEN)
        self.assertNotEqual(DISCORD_BOT_TOKEN, '')

    def test_openai_connection(self):
        # Check if the GPT API key is set and is not empty
        self.assertIsNotNone(GPT_API_KEY)
        self.assertNotEqual(GPT_API_KEY, '')

        # Send a test request to the OpenAI API and check if the response is valid
        headers = {'Authorization': f'Bearer {GPT_API_KEY}'}
        response = requests.get(GPT_API_URL, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mongodb_connection(self):
        # Check if the MongoDB connection string is set and is not empty
        self.assertIsNotNone(MONGO_CONNECTION_STRING)
        self.assertNotEqual(MONGO_CONNECTION_STRING, '')

        # Try to connect to MongoDB and list databases to check if the connection is valid
        mongo_client = MongoClient(MONGO_CONNECTION_STRING)
        db_list = mongo_client.list_database_names()
        self.assertIsNotNone(db_list)


if __name__ == '__main__':
    unittest.main()
