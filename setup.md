# Setup Instructions

  

## Prerequisites

- Python 3.7 or higher

- Pip (Python package installer)

  

## Environment Variables

Create a `.env` file in the root directory with the following content:


```bash
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
API_URL=http://localhost:5000/command
API_PORT=5000
BOT_PORT=8000
APP_PORT=8001
APP_IP=127.0.0.1
```
## Installing Dependencies

Each component has its own `requirements.txt`. Install them as follows:

### Bot dependencies:
```bash
cd bot
pip install -r requirements.txt
```

### API dependencies:
```bash
cd ../api
pip install -r requirements.txt
```

### App dependencies:
```bash
cd ../app
pip install -r requirements.txt
```

## Running the Project

To run all components together, use the following command:

`python main.py` 

## Configuring IP and Ports

Make sure to set your own IP and port numbers in the `.env` file. The default values are:

-   API URL: `http://localhost:5000/command`
-   API Port: `5000`
-   Bot Port: `8000`
-   App Port: `8001`
-   App IP: `127.0.0.1`

## Creating a Telegram Bot

To create a Telegram bot and get the `TELEGRAM_BOT_TOKEN`, follow these steps:

1.  **Open Telegram:** Open the Telegram app on your phone or computer.
    
2.  **Search for BotFather:** In the search bar, type `BotFather` and select the verified account.
    
3.  **Start a Chat:** Start a chat with BotFather by clicking the "Start" button.
    
4.  **Create a New Bot:**
    
    -   Type `/newbot` and send the message.
    -   Follow the prompts to choose a name and username for your bot. The username must end with `bot` (e.g., `mindbot`).
5.  **Get the Token:** After creating the bot, BotFather will provide you with a token. Copy this token.
    
6.  **Set the Token in `.env`:** Paste the token into the `TELEGRAM_BOT_TOKEN` field in your `.env` file:
    
    `TELEGRAM_BOT_TOKEN=your_telegram_bot_token` 
    
7.  **Configure Commands (Optional):**
    
    -   To set commands for your bot, type `/setcommands` in the chat with BotFather.
    -   Select your bot and provide a list of commands in the following format:
    ```plaintext
    forward - Move forward
    backward - Move backward
    left - Turn left
    right - Turn right
    north - Move north
    south - Move south
    east - Move east
    west - Move west
    ```
