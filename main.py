import time
import requests
from datetime import datetime

# === CONFIGURATION ===
TOKEN = '7813344356:AAGqZV5YobJLMEQG6uY3gqHBvBG4'
CHAT_ID = '7693572265'

# === LISTES ÉLARGIES – STABLE EFFICACES ===
CRYPTO_IDS = [
    "sei-network", "fetch-ai", "render", "arbitrum", "the-graph", "fantom", "mantle",
    "echelon-prime", "api3", "ali", "polkastarter", "vigorus", "tracer-dao", "aerodrome-finance",
    "arkham", "velodrome-finance", "starknet", "taiko", "tensor-hyperdrive", "trump", "pepe", "floki"
]

STOCK_SYMBOLS = [
    "BKSY", "HIVE", "TTE.PA", "META", "GOOG", "BNP.PA", "MSFT", "TSLA", "AAPL", "UPS", "ORGO", "CI",
    "ON", "NVDA", "IONQ", "COUR", "AHCO", "FROG", "LWCR.DE", "DUE.DE", "KER.PA", "ATO.PA", "JD.US",
    "BABA", "01211.HK", "3750.HK", "MBG.DE", "STZ", "BNGO"
]
