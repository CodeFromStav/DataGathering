# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import request

apikey = os.getenv("YT_DATA_API")


def search_videos(topic="04rlf", query, apikey=apikey):
    query_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&order=relevance&topicId={}&q={}&type=video&key={}".format(topic, query, apikey)
    response = request.get(query_url)
    data = response.json()
