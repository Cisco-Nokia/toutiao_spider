#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
在今日头条中，搜索街拍，抓取图集中的图片相关信息
索引url类似于https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=3
通过ajax，控制offest来持续获取索引页上的新闻列表信息
"""
import html_downloader
import html_parser
import url_manager
import result_processor


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.result_processor = result_processor.ResProcessor()

    def craw(self):
        # 首先添加索引url，类似https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=3
        # 控制爬取多少个索引页面，每个索引页面包含20条信息（由offset决定）
        index_range = [ x * 20 for x in list(range(0, 5)) ]
        keyword = "街拍"
        for offset in index_range:
            self.urls.add_index_url(offset, keyword)
        while self.urls.has_index_url():
            index_url = self.urls.get_index_url()
            print("开始对索引%s网页进行下载" % index_url)
            index_html = self.downloader.download_index_html(index_url)
            # 通过解析索引页内容中的信息，得到每个具体页的url集合
            page_urls = self.parser.parse_index_html(index_html)
            print("得到该索引页面下所有文章的url：", page_urls)
            self.urls.add_page_urls(page_urls)
            while self.urls.has_page_url():
                page_url = self.urls.get_page_url()
                print("开始对具体文章页进行下载：", page_url)
                page_html = self.downloader.download_page_html(page_url)
                # 通过解析具体页面内容中的信息，得到其中的图片地址，文章标题
                page_data = self.parser.parse_page_html(page_html)
                print("得到具体页面的标题：%s，和所有图片的url：%s" % (page_data['title'], page_data['img_urls']))
                # 下载图片
                print("开始下载图片")
                self.result_processor.download_img(page_data)


if __name__ == "__main__":
    spider_obj = SpiderMain()
    spider_obj.craw()