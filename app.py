from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_opensea_page(ethereum_address):
    opensea_url = f"https://opensea.io/accounts/{ethereum_address}"
    response = requests.get(opensea_url)

    if response.status_code == 200:
        return response.text
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    opensea_pages = []

    if request.method == "POST":
        ethereum_addresses = request.form.get("ethereum_addresses").split("\n")

        for address in ethereum_addresses:
            opensea_page = get_opensea_page(address.strip())
            if opensea_page:
                opensea_pages.append((address, opensea_page))

    return render_template("index.html", opensea_pages=opensea_pages)

if __name__ == "__main__":
    app.run(debug=True)
