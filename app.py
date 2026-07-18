from flask import Flask, jsonify,send_file
from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
notion = Client(auth=os.environ["NOTION_TOKEN"])
datasource_id = os.environ["NOTION_DATASOURCE_ID"]

@app.route("/") 
def home():
    return "Book club backend running"

def clean_book(page):
    props = page["properties"]
    naziv = props["NAZIV KNJIGE"]["title"][0]["plain_text"] if props["NAZIV KNJIGE"]["title"] else "Bez naslova"
    autor = props["AUTOR"]["rich_text"][0]["plain_text"] if props["AUTOR"]["rich_text"] else "Nepoznat autor"
    status = props["STATUS"]["select"]["name"] if props["STATUS"]["select"] else "NEPOZNATO"
    zanr = [tag["name"] for tag in props["ZANR"]["multi_select"]]
    godina = props["GODINA IZDANJA"]["number"]
    return { 
        "naziv" : naziv,
        "autor" : autor,
        "status": status,
        "zanr": zanr,
        "godina": godina
    }
@app.route("/api/books")
def get_books():
    all_results = []
    has_more = True
    start_cursor = None

    while has_more:
        if start_cursor:
            response = notion.data_sources.query(
                data_source_id = datasource_id,
                start_cursor = start_cursor
            )
        else:
            response = notion.data_sources.query(data_source_id=datasource_id)
        all_results.extend(response["results"])
        has_more = response["has_more"]
        start_cursor = response.get("next_cursor")
    books = [clean_book(page) for page in all_results]
    return jsonify(books)

@app.route("/search")
def search_page():
    return send_file("index.html")


if __name__ == "__main__":
    app.run(debug=True)
