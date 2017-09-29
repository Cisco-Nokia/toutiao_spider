#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
对url网页内容进行下载，便于后续的parse
"""

import requests
from requests.exceptions import RequestException


class HtmlDownloader(object):

    def download_html(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html = response.text
                return html
            else:
                return None
        except RequestException:
            print('下载出错：', url)
            return None
