from flask import Flask, jsonify, render_template, request
import sys, yaml, os

app =  Flask(__name__)
environment = os.getenv("ENVIRONMENT", "development")

with open('links.yaml') as f:
    links = yaml.load(f, Loader=yaml.FullLoader)

@app.route("/bio")
def home():
    return render_template("bio.html")

if __name__ == "__main__":
    debug=True
    if environment == 'development':
        debug = True
    app.run(host="0.0.0.0", debug=debug)