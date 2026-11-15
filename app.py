"""
Ghost Market Bot — Entry Point.
Run with: python app.py
"""

import asyncio
import sys
import threading
import os
from flask import Flask

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__))

from bot.main import run_bot

# 1. Simple Flask HTTP server for Render deployment and port binding
app = Flask(__name__)

@app.route("/")
def health_check():
    return "Zenkai OTP Bot is alive and running!", 200

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def start_web_server():
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()


def main() -> None:
    """Main entry point for hosting panels and Telegram bot."""
    try:
        # Web server ko background thread mein start karein
        start_web_server()
        
        # Bot ko async loop mein run karein
        asyncio.run(run_bot())
    except (KeyboardInterrupt, SystemExit):
        print("\n⚡ Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
