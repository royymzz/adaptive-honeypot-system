"""Sanitized portfolio version of the thesis alerting script.

Configure credentials outside source control before use.
"""

import os
import sys

import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text: str) -> None:
    if not TOKEN or not CHAT_ID:
        raise RuntimeError("Telegram configuration is missing.")

    endpoint = "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(endpoint, data=payload, timeout=10)
    response.raise_for_status()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Provide an alert message.")
    send_message(" ".join(sys.argv[1:]))
