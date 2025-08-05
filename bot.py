import requests
import datetime

API_URL = "https://api.coingecko.com/api/v3/simple/price"

# ⚠️ Pega aquí tu webhook de Discord
DISCORD_WEBHOOK = "https://discordapp.com/api/webhooks/1402376099261976736/eDLjY_3nZfFi6IKeSPaG6r4JSTmwV3SMmKpvtXk-krl6AiPHwXwWranuVu9JaHT8G6vt"

def get_price(coin="bitcoin", currency="usd"):
    r = requests.get(API_URL, params={"ids": coin, "vs_currencies": currency})
    data = r.json()
    return data[coin][currency]

def send_to_discord(message):
    payload = {"content": message}
    requests.post(DISCORD_WEBHOOK, json=payload)

def main():
    btc = get_price("bitcoin", "usd")
    eth = get_price("ethereum", "usd")
    xrp = get_price("ripple", "usd")

    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"📊 **Precios Cripto** ({now} UTC)\n"
    msg += f"🪙 BTC: **${btc:,}**\n"
    msg += f"💎 ETH: **${eth:,}**\n"
    msg += f"🌊 XRP: **${xrp:,}**\n"

    send_to_discord(msg)

if __name__ == "__main__":
    main()
