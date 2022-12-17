from sentiment_analysis_flask import app
import json


my_sentence = "I am reading a blog post on AnalyticsVidhya. I am loving it!"


def test_on_sentiment_analysis():
    response = app.test_client().get(
        "/sentiment/I am reading a blog post on AnalyticsVidhya. I am loving it!"
    )
    res = json.loads(response.data.decode("utf-8")).get(my_sentence)
    assert res == "0.75"
