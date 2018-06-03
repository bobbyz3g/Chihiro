# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
from .models.es_types import ArticleType
from elasticsearch_dsl.connections import connections
from typing import Any, Tuple, List, Dict


class ChihirospiderItem(scrapy.Item):
    pass


def _remove_html_tags(value):
    return remove_tags(value)


_es = connections.create_connection(ArticleType._doc_type.using)


def _gen_suggests(index: Any, info_tuple: Tuple[str, int])-> List[Dict[str, List]]:

    # 根据字符串生成搜索建议数组
    used_words = set()
    suggests = []
    for text, weight in info_tuple:
        if text:
            # 调用es的analyze接口分析字符串
            words = _es.indices.analyze(index=index, params={'analyzer': "ik_max_word", 'filter': ["lowercase"]},
                                        body=text)
            anylyzed_words = set([r["token"] for r in words["tokens"] if len(r["token"]) > 1])
            new_words = anylyzed_words - used_words
        else:
            new_words = set()

        if new_words:
            suggests.append({"input": list(new_words), "weight": weight})

    return suggests


class JianshuItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field(
        input_processor=MapCompose(_remove_html_tags)
    )
    author = scrapy.Field()

    def save(self)-> None:
        article = ArticleType()
        article.title = self['title']
        article.url = self['url']
        article.content = self['content']
        article.author = self['author']

        article.suggest = _gen_suggests(ArticleType._doc_type.index,
                                        ((article.title, 10), (article.content, 7)))

        article.save()
        return


class JianshuItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
