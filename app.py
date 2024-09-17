from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    cat_url = get_cat()
    return render_template('index.html', url=cat_url)

@app.route("/get_cat", methods=["GET"])
def get_cat():
    return requests.get("https://api.thecatapi.com/v1/images/search").json()[0]['url']

@app.route("/get_dog", methods=["GET"])
def get_dog():
    return requests.get("https://dog.ceo/api/breeds/image/random").json()['message']

if __name__ == "__main__":
    app.run(debug=True)