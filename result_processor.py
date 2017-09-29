#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from hashlib import md5

import requests


class ResProcessor(object):
    def download_img(self, page_data):
        # 根据title建立文件夹
        img_dir_name = page_data.get('title')
        current_dir = os.getcwd()
        img_dir = os.path.join(current_dir, img_dir_name)
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)
            # 下载对应网页的图片
            img_urls = page_data.get('img_urls')
            for img_url in img_urls:
                response = requests.get(img_url)
                if response.status_code == 200:
                    file_name = md5(response.content).hexdigest() + '.jpg'
                    file_path = os.path.join(img_dir, file_name)
                    print("正在下载图片：", img_url)
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                        f.close()
