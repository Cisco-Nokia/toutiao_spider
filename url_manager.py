#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import urlencode


class UrlManager(object):
    def __init__(self):
        self.index_urls = set()
        self.page_urls = set()

    def add_index_url(self, offset, keyword):
        data = {
            'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': 20,
            'cur_tab': 3,
        }
        base_index_url = "https://www.toutiao.com/search_content/"
        url_params = urlencode(data)
        index_url = base_index_url + "?" + url_params
        self.index_urls.add(index_url)

    def has_index_url(self):
        return len(self.index_urls) != 0

    def get_index_url(self):
        return self.index_urls.pop()

    def add_page_urls(self, page_urls):
        for url in page_urls:
            self.page_urls.add(url)

    def has_page_url(self):
        return len(self.page_urls) != 0

    def get_page_url(self):
        return self.page_urls.pop()
