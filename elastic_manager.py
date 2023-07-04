from elasticsearch import Elasticsearch

class ElasticManager:
    def __init__(self, hosts, verify_certs=False, ssl_show_warn=False, api_key=None):
        self.hosts = hosts
        self.verify_certs = verify_certs
        self.ssl_show_warn = ssl_show_warn
        self.api_key = api_key
        self.es = None

    def connect(self):
        self.es = Elasticsearch(
            hosts=self.hosts,
            verify_certs=self.verify_certs,
            ssl_show_warn=self.ssl_show_warn,
            api_key=self.api_key
        )

    def is_connected(self):
        if self.es:
            return self.es.ping()
        return False

    def get_client(self):
        return self.es

    def close(self):
        if self.es:
            self.es.close()
            self.es = None