from flask import Flask, jsonify
from textblob import TextBlob


app = Flask(__name__)


@app.route("sentiment/<sentence>", methods=["GET"])
def sentiment_analysis(sentence):
    my_sentence = TextBlob(sentence)
    return jsonify({sentence: str(my_sentence.sentiment.polarity)})


if __name__ == "__main__":
    app.run(debug=True)
