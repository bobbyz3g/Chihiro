# -*- coding: utf-8 -*-

# Define item pipelines here

from typing import Any


class ChihirospiderPipeline(object):
    def process_item(self, item: Any, spider: Any) -> Any:
        item.save()
        return item
