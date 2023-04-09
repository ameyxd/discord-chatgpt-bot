"""
Project: discord-chatgpt-bot
Author: ameyxd
Copyright (c) 2023 Amey Ambade
Description: Test GPT-3.5 interaction
"""
import unittest
from bot.main import interact_with_gpt


class TestGPT(unittest.TestCase):
    def test_gpt_interaction(self):
        prompt = "Hello, how are you?"
        response = interact_with_gpt(prompt)  # Example function to interact with GPT
        # Check if the response is not empty
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
