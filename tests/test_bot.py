"""
Project: discord-chatgpt-bot
Author: ameyxd
Copyright (c) 2023 Amey Ambade
Description: Test discord bot functioning
"""
import unittest
from unittest.mock import AsyncMock, MagicMock
from bot.main import ask, private, public
import asyncio


class TestBot(unittest.TestCase):
    def setUp(self):
        self.ctx = MagicMock()
        self.ctx.send = AsyncMock()

    def test_public_mode(self):
        asyncio.run(public(self.ctx))
        self.ctx.send.assert_called_once_with('Bot mode set to public.')

    def test_private_mode(self):
        asyncio.run(private(self.ctx))
        self.ctx.send.assert_called_once_with('Bot mode set to private.')

    def test_ask_command(self):
        asyncio.run(ask(self.ctx, prompt="Hello, how are you?"))
        # Validate that the ctx.send method was called and the response is as expected
        # You can customize this part based on your expected behavior and response format
        self.assertTrue(self.ctx.send.called)


if __name__ == '__main__':
    unittest.main()
