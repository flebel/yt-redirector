#!/usr/bin/env python

import argparse
import ConfigParser
import requests

from flask import Flask, redirect

app = Flask(__name__)
parser = argparse.ArgumentParser(description='Flask app that redirects to the most relevant YouTube video based on a given query.')
parser.add_argument('--config', default='default.conf', dest='config_file', help='Configuration file', type=str)
url = u'https://www.googleapis.com/youtube/v3/search?key={YOUR_API_KEY}&maxResults=1&order=relevance&part=snippet&q={QUERY}&safeSearch=moderate'

@app.route('/<query>')
def query(query):
  video_url = url.format(QUERY=query, YOUR_API_KEY=API_KEY)
  video_id = requests.get(video_url).json()['items'][0]['id']['videoId']
  player_url = 'https://www.youtube.com/watch?v=%s' % (video_id,)
  return redirect(player_url, 301)

if __name__ == '__main__':
    args = parser.parse_args()
    config = ConfigParser.SafeConfigParser()
    config.read(args.config_file)
    API_KEY = config.get('youtube', 'api_key')
    app.run(debug=True)

