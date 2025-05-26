# ChatGPT Lite Messenger

A lightweight, customizable terminal-based messenger that uses OpenAI's GPT models using their API. Choose your preferred model and personality, and chat directly in the terminal. Designed for personal use and experimentation.

## Features

- Multiple GPT models (including GPT-4o support)
- Personality presets (friendly, coach, poet, etc.)
- Chat history loading and saving
- Color-coded terminal interface
- Easy to run and extend

## Requirements

- Python 3.8+
- OpenAI API key

## Dependencies

Install dependencies using pip:
```
pip install openai python-dotenv colorama
```

## Setup
```
git clone https://github.com/mariosevripidou/chatgpt-lite-messenger/tree/main
cd chatgpt-lite-messenger
```

## How to Run

```
python chatgtp_messenger_lite.py"
```
Follow the interactive prompts to:
  - Select a GPT model
  - Choose a personality
	- Start chatting!

Type exit or quit to end your session. Your conversation will be saved automatically.

## Files

- chatgtp_messenger_lite.py – Main terminal chat app
- .env – API key loader (excluded from GitHub)
- last_chat.json – Automatically created to persist last conversation
- chat_history_*.txt – Auto-saved chat logs
