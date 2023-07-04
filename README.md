# ElasticManager

The ElasticManager is a Python class designed to streamline the process of connecting and interacting with an Elasticsearch instance. The class provides methods to connect to Elasticsearch, check the connection status, retrieve the client instance, and close the connection.

The `ElasticManager` class is initialized with parameters such as the hosts, certificates verification settings, SSL warning settings, and an API key if needed. After initialization, a connection can be established to Elasticsearch using the `connect()` method.

The `is_connected()` method can be used to check if the ElasticManager is successfully connected to an Elasticsearch instance by pinging it. If the connection is successful, it returns `True`; otherwise, it returns `False`.

The `get_client()` method returns the current Elasticsearch client instance, which can be used to interact with Elasticsearch.

The `close()` method allows to safely close the connection to the Elasticsearch instance when it's no longer needed.

The class uses the Elasticsearch Python client for handling connections and operations.

## Usage

To use the ElasticManager, you'll first need to import the Elasticsearch module and the ElasticManager class. After that, create an instance of the ElasticManager, providing the necessary connection details:

```python
from elasticsearch import Elasticsearch
from elastic_manager import ElasticManager

es_manager = ElasticManager(hosts=[...], verify_certs=True, ssl_show_warn=False, api_key=None)
```

You can then establish a connection, verify its status, retrieve the client instance, perform Elasticsearch operations, and finally, close the connection:

```python
es_manager.connect()

if es_manager.is_connected():
    es = es_manager.get_client()
    # Perform Elasticsearch operations...

es_manager.close()
```

## Contribution

Contributions to the code are always welcome. If you encounter any issues or have any improvement suggestions, please open an issue or a pull request.

## License

The code is distributed under the MIT license. Please see the LICENSE file for more details.