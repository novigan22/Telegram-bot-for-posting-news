 📰 News Parser Telegram Bot  

This Telegram bot automatically scrapes news articles from a selected website, summarizes them using an AI model, and posts them to a Telegram channel every 3 hours.  

---

## ✨ Features  
- Fetches the latest news from a source 
- Summarizes articles using an AI model (Gemini 2.5 Flash)
- Automatically posts summaries to a Telegram channel  
- Notifies the admin when each post cycle starts and finishes  

---

## ⚙️ Tech Stack  
- **Python 3.10+**  
- **aiogram** — Telegram Bot API framework  
- **asyncio** — asynchronous scheduling  
- **BeautifulSoup4** — HTML parsing  
- **aiohttp** — async HTTP requests  
- **Gemini API** — text summarization

- ## 🚀 Installation  

1. **Clone the repository:**  
   git clone https://github.com/username/news-parser-bot.git
   cd news-parser-bot

2. **Install dependencies:**
    pip install -r requirements.txt

3. **Configure environment:**
   Create or edit config.py with your credentials:
  
   BOT_TOKEN = "your_telegram_bot_token"
  
   CHANNEL_ID = "your_channel_name"
  
   USER_ID = "admin Telegram user ID"
  
   OPENAI_API_KEY = "your_openai_api_key"

4. **Run the bot:**
    python main.py
