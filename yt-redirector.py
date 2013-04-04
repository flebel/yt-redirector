#!/usr/bin/env python

from flask import Flask, redirect
from xml.etree import ElementTree
import urllib2

app = Flask(__name__)
url = 'https://gdata.youtube.com/feeds/api/videos?q={{QUERY}}&orderby=relevance&max-results=1&v=2'


@app.route('/<query>')
def query(query):
  video_url = url.replace('{{QUERY}}', query)
  xml = urllib2.urlopen(video_url)
  tree = ElementTree.parse(xml)
  root = tree.getroot()

  entry = root.find("{http://www.w3.org/2005/Atom}entry")
  media = entry.find('{http://search.yahoo.com/mrss/}group')
  player = media.find('{http://search.yahoo.com/mrss/}player')
  player_url = player.attrib['url']

  return redirect(player_url, 301)


if __name__ == "__main__":
    app.run(debug=True)

