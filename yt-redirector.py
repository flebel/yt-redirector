#!/usr/bin/env python

import argparse
import ConfigParser
import urllib2
from xml.etree import ElementTree

from flask import Flask, redirect

app = Flask(__name__)
parser = argparse.ArgumentParser(description='Flask app that redirects to the most relevant YouTube video based on a given query.')
parser.add_argument('--config', default='default.conf', dest='config_file', help='Configuration file', type=str)

url = u'https://gdata.youtube.com/feeds/api/videos?q={query}&orderby=relevance&max-results=1&v=2'


@app.route('/<query>')
def query(query, api_key):
  video_url = url.format(QUERY=query, YOUR_API_KEY=api_key)
  xml = urllib2.urlopen(video_url)
  tree = ElementTree.parse(xml)
  root = tree.getroot()

  entry = root.find('{http://www.w3.org/2005/Atom}entry')
  media = entry.find('{http://search.yahoo.com/mrss/}group')
  player = media.find('{http://search.yahoo.com/mrss/}player')
  player_url = player.attrib['url']

  return redirect(player_url, 301)


if __name__ == '__main__':
    args = parser.parse_args()
    config = ConfigParser.SafeConfigParser()
    config.read(args.config_file)
    API_KEY = config.get('youtube', 'api_key')
    app.run(debug=True)

