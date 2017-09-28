#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse_index_html(self, index_html):
        data = json.loads(index_html)
        urls = [ item.get('article_url') for item in data.get('data') ]
        # 经过简单测试，发现上面的urls还包含一些不符合后续爬取规则的页面，将他们过滤掉
        page_urls = [ url for url in urls if 'toutiao.com' in url ]
        return page_urls

    def parse_page_html(self, page_html):
        soup = BeautifulSoup(page_html, 'html.parser')
        title = soup.find("title").text
        result = re.search(r"gallery: (.*?),\n", page_html)
        if result:
            data = json.loads(result.group(1))
            if data and 'sub_images' in data.keys():
                img_urls = [ item.get('url') for item in data['sub_images'] ]
        page_data = {
            'title': title,
            'img_urls': img_urls,
        }
        return page_data