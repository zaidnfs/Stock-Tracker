# Stock News Alert 🚀

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Twilio](https://img.shields.io/badge/Twilio-API-red.svg)](https://www.twilio.com/)
[![AlphaVantage](https://img.shields.io/badge/AlphaVantage-API-yellow.svg)](https://www.alphavantage.co/)
[![NewsAPI](https://img.shields.io/badge/NewsAPI-API-green.svg)](https://newsapi.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A Python script that monitors the daily stock price of a company (e.g., Tesla) and sends SMS notifications with the latest news if the stock price changes significantly.

---

## Features ✨

* 📈 Tracks daily stock prices using the [Alpha Vantage API](https://www.alphavantage.co/).
* 🔄 Calculates the percentage change between yesterday and the day before yesterday.
* 📰 Fetches the latest news for the company using [NewsAPI](https://newsapi.org/).
* 📲 Sends SMS alerts via [Twilio](https://www.twilio.com/) with stock movement and news headlines.
* Emoji indicators to quickly show if the stock went up 🔺, down 🔻, or stayed the same 🟰.
* ⚡ Quick notifications for significant stock movements.

---

## Requirements 🛠️

* Python 3.8+
* Packages:

  * `requests`
  * `twilio`
  * `python-dotenv`
* Accounts and API keys for:

  * [Alpha Vantage](https://www.alphavantage.co/)
  * [NewsAPI](https://newsapi.org/)
  * [Twilio](https://www.twilio.com/)

---

## Installation ⚡

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```
AV_API_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_news_api_key
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH=your_twilio_auth_token
```

4. Replace the recipient phone number in the script with your number.

---

## Usage ▶️

Run the script:

```bash
python stock_news_alert.py
```

You will receive SMS messages with the latest news headlines if the stock price changes significantly.

---

## Customization 🎨

* Change `STOCK` and `COMPANY_NAME` in the script to monitor different companies.
* Adjust the threshold for alerts by changing the condition on `diff_percent`.
* Modify `pageSize` in the News API request to control how many news articles you receive.
* Update the `.env` file with your own API keys and Twilio credentials.

---

## Security 🔒

Do **not** share your `.env` file publicly. Keep API keys and credentials secure.

---

## License 📄

This project is open source and free to use. See the [LICENSE](LICENSE) file for details.

---

## Badges & Notes 🏷️

* 🚀 Great for personal stock tracking and learning API integrations.
* 🛡️ Secure: API keys are loaded from `.env`.
* 🎨 Supports customization for any company or stock ticker.
