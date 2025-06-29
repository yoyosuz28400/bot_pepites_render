import time
import requests
from datetime import datetime

# === CONFIGURATION ===
TOKEN = '7813344356:AAGqZV5YobJLMEQG'
CHAT_ID = '7693572265'

# === LISTES ÉLARGIES – STABLE EFFICACE ===
CRYPTO_IDS = [
    "sei-network", "fetch-ai", "render", "polkadot", "tron", "pepe", "dogecoin",
    "arbitrum", "the-graph", "fantom", "mantle", "osmosis", "vechain",
    "echelon-prime", "api3", "ali", "ambi", "kwenta", "looksrare", "iotex", "biconomy", "synapse"
]

STOCK_SYMBOLS = [
    "BKSY", "HIVE", "TTE.PA", "META", "COUR", "AHCO", "FROG", "AIR.PA", "MSFT", "COST", "STZ", "JD.US",
    "BABA", "01211.HK", "3750.HK", "GOOG", "AMD", "AAPL", "IONQ", "NVDA", "AMZN"
]

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': msg}
    try:
        requests.post(url, data=data)
    except:
        pass

def scan_cryptos():
    for name in CRYPTO_IDS:
        try:
            r = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={name}&vs_currencies=usd")
            data = r.json()
            price = data[name]["usd"]
            send_telegram_message(f"✅ {name.upper()} = {price:.4f} $")
        except Exception as e:
            send_telegram_message(f"❌ Erreur prix pour {name} : {e}")

def scan_stocks():
    for symbol in STOCK_SYMBOLS:
        try:
            url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
            r = requests.get(url)
            data = r.json()
            price = data["quoteResponse"]["result"][0]["regularMarketPrice"]
            send_telegram_message(f"✅ {symbol} = {price:.2f} $")
        except Exception as e:
            send_telegram_message(f"❌ Erreur action {symbol}: {e}")

while True:
    scan_cryptos()
    scan_stocks()
    time.sleep(180)  # toutes les 3 minutes
