from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Amazon product URL
url = "https://www.amazon.in/ASUS-5050-8GB-Windows-Eclipse-G614PH-RV033WS/dp/B0FB9G9XVG/ref=sr_1_3?crid=2DAR2719N4II4&dib=eyJ2IjoiMSJ9.iWMCOPBy_Uvib7QaCPvsolgPTzCgSH5PplKvveBv3LbK-deivQFNbO7z6AHwFXM7WxFckwHacOPrHhp4ZFwcuf_HuGOcHL3hmarZ8KnxIHb6XGay7L84IP8q4U_op5WJgcU4tDg5zfkdP-nmhKb4JjUJJp7O7hOaPmWhYBHCisqKAOg967iyt-IeSrtClgK3DiXbqO722mOxdt5v_-40BJJcupWqURPjtV1BK_oCu74.KOlynDZvu0QcGSzGbKVnMJ5Bk29JcqzbCpbouznvvq8&dib_tag=se&keywords=asus+ryzen+9&nsdOptOutParam=true&qid=1754303800&sprefix=asus+ryzen+9%2Caps%2C276&sr=8-3"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Send request to Amazon
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# --------- Handle Price Extraction ----------
try:
    price = soup.find(class_="a-offscreen").get_text().strip()
    price_as_float = float(price.replace("₹", "").replace(",", ""))
except AttributeError:
    print("❌ Could not find the price on the page. The class may have changed.")
    exit()
except ValueError:
    print("❌ Failed to convert price to float. Format may be incorrect.")
    exit()

# --------- Extract Title ----------
try:
    title = soup.find(id="productTitle").get_text().strip()
except AttributeError:
    title = "Product Title Not Found"

print(f"✅ Product: {title}")
print(f" ₹ Current Price: ₹ {price_as_float}")

# --------- Price Threshold Alert ----------
BUY_PRICE = 130000  # Change this to your target price

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for ₹{price_as_float}!\n{url}"

    try:
        with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
            connection.starttls()
            connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
            connection.sendmail(
                from_addr=os.environ["EMAIL_ADDRESS"],
                to_addrs=os.environ["EMAIL_ADDRESS"],
                msg=f"Subject:Amazon Price Alert!\n\n{message}"
            )
            print("📧 Email alert sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
