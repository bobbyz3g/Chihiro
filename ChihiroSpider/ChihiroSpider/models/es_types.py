from elasticsearch_dsl import DocType, Text, Completion, Keyword
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
from typing import Dict

connections.create_connection(hosts=['localhost'])


class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self) -> Dict:
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


class ArticleType(DocType):
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer='ik_max_word')
    url = Keyword()
    content = Text(analyzer='ik_max_word')
    author = Text(analyzer='ik_max_word')

    class Meta:
        index = "chihiro"
        doc_type = "article"


if __name__ == "__main__":
    ArticleType.init()