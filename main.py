import time
import requests
from datetime import datetime
from keep_alive import keep_alive

TOKEN = '7813344356:AAGqZV5YobJLMEQGxxxxx'  # ton token Telegram
CHAT_ID = '7693572265'  # ton chat ID

CRYPTO_IDS = [
    "fetch-ai", "sei-network", "render", "trump", "pepe", "ethereum", "solana",
    "avalanche", "ripple", "polkadot", "cardano", "ocean-protocol", "agix"
]

STOCK_SYMBOLS = [
    "BKSY", "HIVE", "JD", "META", "MSFT", "COST", "TTE.PA", "BNP.PA", "AAPL",
    "UPS", "TSLA", "GOOG", "CI", "NVDA", "IONQ", "BABA"
]

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Erreur Telegram :", e)

def check_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "ids": ",".join(CRYPTO_IDS)}
    r = requests.get(url, params=params)
    data = r.json()
    for coin in data:
        name = coin['id']
        price = coin['current_price']
        change = coin['price_change_percentage_24h']
        if change is not None:
            if change >= 8:
                send_alert(f"🚀 {name.upper()} explose (+{change:.1f}%) → {price}$")
            elif change <= -8:
                send_alert(f"🔻 {name.upper()} chute ({change:.1f}%) → {price}$")

def check_stocks():
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={','.join(STOCK_SYMBOLS)}"
    r = requests.get(url)
    data = r.json()["quoteResponse"]["result"]
    for stock in data:
        symbol = stock["symbol"]
        price = stock.get("regularMarketPrice")
        change = stock.get("regularMarketChangePercent")
        if price is not None and change is not None:
            if change >= 5:
                send_alert(f"📈 ACTION {symbol} +{change:.1f}% → {price}$")
            elif change <= -5:
                send_alert(f"📉 ACTION {symbol} {change:.1f}% → {price}$")

# Garde le bot actif sur Render
keep_alive()

while True:
    check_cryptos()
    check_stocks()
    time.sleep(600)  # vérifie toutes les 10 minutes
