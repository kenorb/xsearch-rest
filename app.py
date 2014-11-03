#!/usr/bin/env python
# RESTful web service for search engines using xgoogle.
#
# Usage:
#   ./app.py
# Testing:
#   curl -i http://localhost:5000/xsearch/api/v1.0/cache
#   curl -i -H "Content-Type: application/json" -X POST -d '{"engine":"Google","query":"site:example.com"}' http://localhost:5000/xsearch/api/v1.0/search

from flask import Flask, jsonify
from flask import request
# TODO: import xgoogle

app = Flask(__name__)

cache = [
    {
        'pos': 1, # Position.
        'title': u'Buy groceries', # Site title.
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', # Site description.
        'url': u'https://www.example.com/foo/index.html', # URL.
        'url_cache': u'https://webcache.example.com/foo/index.html', # Cached URL.
        'query': u'site:example.com', # Original query.
        'done': False
    },
    {
        'pos': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'url': u'https://www.example.com/foo/',
        'url_cache': u'https://webcache.example.com/foo/index.html',
        'query': u'site:example.com',
        'done': False
    }
]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/xsearch/api/v1.0/cache', methods=['GET'])
def get_cache():
    # TODO: Get all available search items from memcached.
    return jsonify({'cache': cache})

@app.route('/xsearch/api/v1.0/search', methods=['POST'])
def create_task():
    if not request.json or not 'query' in request.json:
        abort(400)

    # search.append(task)
    # TODO:

    # cache = (memcached get) # TODO: If the same query exists already in cache, get from cache.
    result = cache

    return jsonify({'results': result}), 201

if __name__ == '__main__':
    app.run(debug=True)
