import feedparser
from flask import Flask, render_template

app = Flask(__name__)

rss_feeds = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'nytimes': 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'rappler': 'https://www.rappler.com/rss',
    'inquirer': 'https://newsinfo.inquirer.net/rss',
}

@app.route("/")
@app.route("/bbc")
def bbc_news():
    return get_new('bbc')

@app.route("/cnn")
def cnn_news():
    return get_new('cnn')

@app.route("/fox")
def fox_news():
    return get_new('fox')

@app.route("/nytimes")
def nytimes_news():
    return get_new('nytimes')

@app.route("/rappler")
def rappler_news():
    return get_new('rappler')

@app.route("/inquirer")
def inquirer_news():
    return get_new('inquirer')

def get_new(publication):
    try:
        if publication not in rss_feeds:
            return "<h1>Error: Invalid publication</h1><p>Please enter a valid news source.</p>"

        feed = feedparser.parse(rss_feeds[publication])

        if not feed.entries:
            return "<h1>Error: No articles found</h1><p>There are no news articles available at the moment.</p>"

        return render_template("news.html", articles=feed.entries, publication=publication.upper())

    except Exception as e:
        return f"<h1>Error retrieving news</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
