# chat_terminal.py

import os
import openai
import time
import json
from dotenv import load_dotenv
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Load API Key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Settings
HISTORY_JSON = "last_chat.json"

# Available models
models = {
    "1": ("gpt-3.5-turbo-0125", "Fast and cheap, good for everyday chat."),
    "2": ("gpt-4-0125-preview", "Stronger reasoning, good balance."),
    "3": ("gpt-4-turbo", "Powerful, huge memory (128k tokens)."),
    "4": ("gpt-4o-2024-05-13", "Fastest, smartest, newest (recommended!).")
}

# Available personalities
personalities = {
    "1": ("Friendly Assistant", "You are a friendly and helpful assistant. Answer kindly and clearly."),
    "2": ("Funny Friend", "You are a funny, sarcastic friend who jokes around but still answers seriously."),
    "3": ("Creative Brainstormer", "You are a creative brainstorming partner full of ideas."),
    "4": ("Calm Therapist", "You are a calm, supportive therapist helping the user."),
    "5": ("Direct Coach", "You are a direct, no-nonsense coach. Give strong, concise advice."),
    "6": ("Poet Mode", "You are a poet. Answer artistically."),
    "7": ("Storyteller Mode", "You are a storyteller. Answer with short stories."),
    "8": ("Wise Mentor", "You are a wise mentor sharing ancient life advice."),
    "9": ("Soft Encourager", "You are a very supportive and uplifting friend."),
    "10": ("Business Consultant", "You are a professional business consultant offering strategic advice.")
}

# Defaults (in case user skips selection)
model_name = "gpt-3.5-turbo"
personality_prompt = "You are a helpful and friendly assistant."
conversation = [{"role": "system", "content": personality_prompt}]

# Try loading previous conversation
def load_last_conversation():
    global conversation
    if os.path.exists(HISTORY_JSON):
        try:
            with open(HISTORY_JSON, "r", encoding="utf-8") as f:
                conversation = json.load(f)
            print(f"{Fore.YELLOW}Previous chat history loaded successfully!")
        except Exception as e:
            print(f"{Fore.RED}Failed to load previous chat: {e}")

# Save conversation to both .txt and .json
def save_conversation():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    txt_filename = f"chat_history_{timestamp}.txt"

    with open(txt_filename, "w", encoding="utf-8") as f:
        for msg in conversation:
            role = msg['role'].upper()
            content = msg['content']
            f.write(f"{role}: {content}\n\n")
    print(f"\n{Fore.YELLOW}Chat history saved to {txt_filename}!")

    with open(HISTORY_JSON, "w", encoding="utf-8") as f:
        json.dump(conversation, f, indent=4, ensure_ascii=False)

def chat():
    try:
        while True:
            user_input = input(f"\n{Fore.CYAN}You: {Style.RESET_ALL}")
            if user_input.lower() in ["exit", "quit"]:
                save_conversation()
                print(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
                break

            conversation.append({"role": "user", "content": user_input})

            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=conversation
                )
                reply = response.choices[0].message.content
                print(f"\n{Fore.GREEN}ChatGPT: {reply}{Style.RESET_ALL}")

                conversation.append({"role": "assistant", "content": reply})

            except Exception as e:
                print(f"\n{Fore.RED}Error: {e}{Style.RESET_ALL}")

    except KeyboardInterrupt:
        save_conversation()
        print(f"\n{Fore.YELLOW}\nSession ended by user. Chat history saved!{Style.RESET_ALL}")

# Picker Menus
def pick_model():
    global model_name
    print(f"\n{Fore.MAGENTA}Choose a model:")
    for key, (name, description) in models.items():
        print(f"{key}. {name} - {description}")
    choice = input(f"{Fore.CYAN}Enter number (default 1): {Style.RESET_ALL}")
    model_name = models.get(choice, models["1"])[0]
    print(f"{Fore.YELLOW}Model set to {model_name}{Style.RESET_ALL}")

def pick_personality():
    global personality_prompt, conversation
    print(f"\n{Fore.MAGENTA}Choose a personality:")
    for key, (name, _) in personalities.items():
        print(f"{key}. {name}")
    choice = input(f"{Fore.CYAN}Enter number (default 1): {Style.RESET_ALL}")
    personality_prompt = personalities.get(choice, personalities["1"])[1]
    conversation = [{"role": "system", "content": personality_prompt}]
    print(f"{Fore.YELLOW}Personality set.{Style.RESET_ALL}")

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}Welcome to ChatGTP Lite Messenger.")
    print(f"{Fore.MAGENTA}Type your message below. Type 'exit' or 'quit' to leave.{Style.RESET_ALL}")

    pick_model()
    pick_personality()
    load_last_conversation()
    chat()
