import time
import requests
from datetime import datetime
from keep_alive import keep_alive

# === CONFIGURATION ===
TOKEN = '7813344356:AAGqZV5YobJLMEQGxxxxx'  # Remplace si besoin
CHAT_ID = '7693572265'

# === LISTES À SUIVRE ===
CRYPTO_IDS = [
    "sei-network", "fetch-ai", "render", "arbitrum", "the-graph", "fantom",
    "echelon-prime", "api3", "ali", "ambi", "kaspa", "zeta", "aethir", "mode",
]

STOCK_SYMBOLS = [
    "BKSY", "HIVE", "TTE.PA", "META", "COST", "NVDA", "GOOG", "AAPL", "BABA",
    "01211.HK", "3750.HK", "JD", "TSLA", "MSFT", "CI"
]

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Erreur Telegram :", e)

def check_alerts():
    now = datetime.now().strftime("%H:%M:%S")
    message = f"✅ Bot actif à {now}.\nSuivi crypto & actions OK ✅"
    send_alert(message)

# === ACTIVER LE BOT EN LIGNE ===
keep_alive()

# === BOUCLE DE SURVEILLANCE ===
while True:
    check_alerts()
    time.sleep(3600)  # Toutes les 1h
