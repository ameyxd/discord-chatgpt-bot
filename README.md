# ChatGPT Discord Bot 🤖

Welcome to the ChatGPT Discord Bot! This is an awesome bot that brings the power of OpenAI's GPT-3.5 Turbo model right into your Discord server. With this bot, you can have interactive and dynamic conversations with one of the most advanced language models available!


## Why did I build this bot? Answer: Privacy 📖

The idea for this ChatGPT Discord Bot was born out of a deep concern for privacy and data security. As technology enthusiasts, we love the idea of bringing AI-powered chatbots to Discord servers to enhance interactions and provide value. However, during our exploration of existing solutions, I realized that many chatbots lacked transparency in how they handled user data.

I wanted to create a bot that respects user privacy while delivering powerful AI chat capabilities. We were particularly mindful of the fact that data tracking and lack of privacy control are prevalent in many existing bots. Therefore, I designed our bot with privacy and user control at its core, allowing users to toggle between public and private modes.

I built the ChatGPT Discord Bot using OpenAI's GPT-3.5 Turbo model, and we implemented a MongoDB-backed solution to store interactions securely. My goal is to provide users with dynamic and interactive AI-powered conversations while upholding the highest standards of privacy.

## Features 💡

- 🗨️ Interactive Chat: Chat with the AI in real-time and get instant responses to your questions and prompts.
- 🔒 Public and Private Modes: Set the bot to public mode for everyone to use, or private mode for admin-only access.
- 📜 Context-Aware: The bot maintains the context of the conversation for meaningful interactions.
- 📈 Scalable: Built with MongoDB for data storage and easy scalability.

## Adding the Bot to Your Discord Server

To invite the bot to your Discord server, follow these steps:

1. Click on the following invite link: [Invite the Bot](https://discord.com/api/oauth2/authorize?client_id=1094658194091024444&permissions=76816&scope=bot)

2. You will be redirected to a page where you can select the server you want to add the bot to.

3. In the "Add Bot to Server" dropdown, select the server where you want the bot to be added.

4. Click the "Authorize" button to add the bot to the selected server.

5. Complete the CAPTCHA verification if prompted.

The bot should now be successfully added to your server and ready to use!

## Using the Bot 🕹️

To interact with the bot, use the following commands in a Discord text channel:

- Use the `/ask` command to chat with the AI. For example:

/ask Where is the tallest building in Atlantis?

- Use the `/public` command to set the bot to public mode. Everyone in the server can use the `/ask` command.
- Use the `/private` command to set the bot to private mode. Only the admins can use the  `/ask` command. 
- Use the `/ask` command to ask GPT for answers to your prompts.

## Limitations ⛔

- The bot currently does not support context since the underlying model (GPT-3.5-turbo) is stateless
- The limit to the output response is 4096 characters, which is another limitation of the underlying model

This is a Work In Progress! I am trying to build a better version of the bot with session history, context and longer response support, so any comments or issues reported are appreciated! 

----------------------------------------

## (OPTIONAL) Getting Started: Development 🚀

### Prerequisites

- Python 3.7 or higher
- Discord Bot Token
- OpenAI GPT-3.5 Turbo API Key
- MongoDB Cluster Connection String

### Installation

1. Clone the repository

git clone https://github.com/ameyxd/chatgpt-discord-bot.git

2. Navigate to the project directory

cd chatgpt-discord-bot

3. Install the required Python packages

pip install -r requirements.txt

4. Create a `.env` file and add your Discord Bot Token, OpenAI API Key, and MongoDB Connection String

DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
GPT_API_KEY=YOUR_GPT_API_KEY
MONGO_CONNECTION_STRING=YOUR_MONGO_CONNECTION_STRING

5. Run the bot

python bot/main.py

## Contributing 🤝

Contributions are welcome! Feel free to open issues, make pull requests, or suggest new features.

## License 📄

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Disclaimer 🛑

This bot uses the OpenAI GPT-3.5 Turbo model to generate responses. The responses are generated by the model and may not always be accurate or appropriate. Please use the bot responsibly.

## Contact 📧
@ameyzer on Twitter

For any questions, feedback, or inquiries, please feel free to reach out:

- GitHub: [github.com/ameyxd](https://github.com/ameyxd)
