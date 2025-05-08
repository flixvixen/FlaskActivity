import feedparser
from flask import Flask, render_template

app = Flask(__name__)

# RSS Feed URLs
rss_feeds = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'nytimes': 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'rappler': 'https://www.rappler.com/rss',
    'inquirer': 'https://newsinfo.inquirer.net/feed',
}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    try:
        if publication not in rss_feeds:
            return "<h1>Error: Invalid publication</h1><p>Please enter a valid news source.</p>"

        feed = feedparser.parse(rss_feeds[publication])
        if not feed.entries:
            return "<h1>Error: No articles found</h1><p>No news available at the moment.</p>"

        return render_template("news.html", articles=feed.entries, publication=publication.upper())

    except Exception as e:
        return f"<h1>Error retrieving news</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
