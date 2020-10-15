import feedparser
from chalice import Chalice


app = Chalice(app_name='rss2json')


@app.route('/')
def index():
    request = app.current_request
    query_params = request.query_params

    rss_url = query_params.get('rss') if query_params else ''
    if rss_url:
        code = 0
        data = feedparser.parse(rss_url)
    else:
        code = 1
        data = {}

    return {
        'code': code,
        'data': data,
    }

