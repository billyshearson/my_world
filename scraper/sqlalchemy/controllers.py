from bs4 import BeautifulSoup as bs4
import requests as rq

import http.client
import json
import pandas as pd


class Article(object):
    def __init__(self, id, title, src, content, updated_at):
        self.id = id
        self.title = title
        self.src = src
        self.content = content
        self.updated_at = updated_at


class Scraper(Article, object):

    # e71402546af8bd8e20443779f52d4486318bbd60
    def get_article_qiita(self):
        # r = rq.get('https://qiita.com/')
        # soup = bs4(r.content, 'html.parser')
        h = {'Authorization': 'Bearer e71402546af8bd8e20443779f52d4486318bbd60'}
        conn = http.client.HTTPSConnection("qiita.com")
        url = "/api/v2/items?"
        for i in range(100):
            i += 1
    # Qiita APIで記事情報を取得
        page = "page=" + str(i)
        conn.request("GET", url + page + "&per_page=100", headers=h)

        res = conn.getresponse()
        print(res.status, res.reason)
        data = res.read().decode("utf-8")
        # CSVに出力
        df = pd.read_json(data)
        df.to_csv("qiita.csv", columns=[
            'likes_count',  # いいね数
            'created_at',  # 作成日時
            'title',  # 記事タイトル
            'url'  # 記事URL
        ], mode='a', header=False, index=False)
