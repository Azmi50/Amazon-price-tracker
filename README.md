# 📦 Amazon Price Tracker

A simple Python script that monitors the price of a product on Amazon and sends you an email when the price drops below your defined threshold.

---

## 🔍 Features

- ✅ Scrapes real-time prices from Amazon
- ✅ Sends an email alert if price falls below your target
- ✅ Customizable product URL and price threshold
- ✅ Environment variables for secure credentials
- ✅ Uses BeautifulSoup and requests for scraping

---

## 💻 Tech Stack

- Python 3
- BeautifulSoup (bs4)
- Requests
- smtplib (standard library)
- dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/amazon-price-tracker.git
cd amazon-price-tracker



### 2. Install Dependencies
pip install -r requirements.txt

### 3. Create .env File
Create a .env file in the root directory:
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SMTP_ADDRESS=smtp.gmail.com

🔒 Use an App Password if you're using Gmail with 2FA.

### 4. Customize the Script
Open price_tracker.py and:

Update the url variable to your product’s link

Change BUY_PRICE to your target price

### 5. Run the Script
python price_tracker.py


🛑 Disclaimer
This tool is for educational purposes only.

Web scraping may violate the terms of service of certain websites.

Use responsibly and at your own risk.
