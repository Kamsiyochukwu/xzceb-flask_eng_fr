from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(english_text):
    english_text = request.args.get("english_text")
    # Write your code here
    french_text = english_to_french(english_text)
    return "%s Translated text to French" %(french_text)

@app.route("/frenchToEnglish")
def french_to_english(french_text):
    french_text = request.args.get('french_text')
    # Write your code here
    english_text = french_to_english(french_text)
    return "%s Translated text to English" %(english_text)
   
@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)