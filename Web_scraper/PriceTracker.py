"""
Name: Heecheon Park
Description: Please look at the README
"""

import requests
import string
import re
import smtplib
import time
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Evlution-Pre-workout-Pre-Workout-Watermelon-Pikatropin-Free/dp/B01EE5DCT2/ref=sr_1_2_sspa?crid=4UX4N7TQLX3T&keywords=engine%2Bshred%2Bpre%2Bworkout&qid=1563679668&s=gateway&sprefix=engine%2Bshred%2Caps%2C171&sr=8-2-spons&smid=A2PLYW0DW8DU2C&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

def check_price():
        
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

# Inefficient way..... found the better solution.
#title = str(soup.find(id="title_feature_div").find_all("span")).strip()
#title = re.split(r'\s{2,}', title)[1]

    """
    Beautiful Soup find() may not find a tag or element,
    because some websites run JS DOM manipulation.
    A tag that I am looking for might not show up if I turn off the javascript.
    If find() cannot find a tag, try to look for parent tag and then find a child tag.
    Like below.
    """
    title = soup.find(id="title_feature_div").find("span", id="productTitle").get_text()
    print("Product: "+title.strip())

    price = soup.find(id="priceblock_snsprice_Based").get_text()
# First time that strip could not remove white space.
    price = re.split(r"^\s+|\s+$", price)[1].strip()
# Additional measure to remove white space.
    """
    From the documentation of the string.whitespace:
    A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
    """
    price = price.translate({ord(c): None for c in string.whitespace})
    converted_price = float(price[1:6])
    print("Current Price: $"+str(converted_price))

    if (converted_price < 28.00):
        send_mail()

"""
In order to use send_mail() function, the user of this program must go through some steps in his or her google account.
    1. Enable less secure app.
    2. Activate two step verification.
    3. Enable Google App Password and select Mail to use google mail server.
    4. Once you enable App Password, the user will get a password.
    5. The user can use this password on this program instead of actual Google account password.
"""
def send_mail():
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("your_username@gmail.com", "your password")
    subject = "Price fell down!"
    body = "Check the Amazon link https://www.amazon.com/Evlution-Pre-workout-Pre-Workout-Watermelon-Pikatropin-Free/dp/B01EE5DCT2/ref=sr_1_2_sspa?crid=4UX4N7TQLX3T&keywords=engine%2Bshred%2Bpre%2Bworkout&qid=1563679668&s=gateway&sprefix=engine%2Bshred%2Caps%2C171&sr=8-2-spons&smid=A2PLYW0DW8DU2C&th=1"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
            "your_send_username@gmail.com",
            "your_receive_username@anothermail.com",
            msg
    )

    print("Notification mail has been sent!")
    server.quit()

if __name__ == "__main__":
    while(True):
        check_price()
        time.sleep(60*60*24)
