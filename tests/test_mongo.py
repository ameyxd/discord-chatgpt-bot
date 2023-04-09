# tests/test_mongo.py
import unittest
from pymongo import MongoClient
from bot.main import MONGO_CONNECTION_STRING, MONGO_DB_NAME, store_interaction

class TestMongoDB(unittest.TestCase):
    def setUp(self):
        self.mongo_client = MongoClient(MONGO_CONNECTION_STRING)
        self.db = self.mongo_client[MONGO_DB_NAME]
        self.interactions = self.db.interactions

    def test_store_interaction(self):
        interaction_data = {
            'user_id': 12345,
            'prompt': "Hello, how are you?",
            'response': "I'm doing well, thank you!"
        }
        store_interaction(interaction_data)  # Example function to store interaction in MongoDB
        # Verify that the interaction was stored in the database
        self.assertTrue(self.interactions.find_one(interaction_data))

    def tearDown(self):
        # Clean up the test data from the database
        self.interactions.delete_many({})

if __name__ == '__main__':
    unittest.main()
