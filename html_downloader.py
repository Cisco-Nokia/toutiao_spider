#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


class HtmlDownloader(object):
    def download_index_html(self, index_url):
        response = requests.get(index_url)
        index_html = response.text
        return index_html

    def download_page_html(self, page_url):
        response = requests.get(page_url)
        page_html = response.text
        return page_html