import subprocess

def run_bot():
    subprocess.Popen(["python", "bot/bot.py"])

def run_api():
    subprocess.Popen(["python", "api/tgmindbot-api.py"])

def run_app():
    subprocess.Popen(["python", "app/tgmindbot.py"])

if __name__ == '__main__':
    run_bot()
    run_api()
    run_app()
