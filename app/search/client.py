from elasticsearch import Elasticsearch
from app.core.config import ELASTICSEARCH_URL

es = Elasticsearch(ELASTICSEARCH_URL)