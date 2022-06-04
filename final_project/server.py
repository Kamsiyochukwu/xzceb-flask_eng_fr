from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = input('Enter text in English - ')
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = input('Enter text in French - ')
    return "Translated text to English"

print(englishToFrench())
print(frenchToEnglish())

@app.route("/index.html")
def renderIndexPage():
    # Write the code to render template
    return "Translated text to French"
    return "Translated text to English"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
