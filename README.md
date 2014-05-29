CartoDB table metadata sync client
==================================
[![Build Status](http://travis-ci.org/CartoDB/cartodb-table-sync.png)](http://travis-ci.org/CartoDB/cartodb-table-sync)

Client abstracting the calls to Rails endpoints to notify tables changes: table creations, modifications and deletions.

## Project status
NOT READY: this project is under development, tests do not represent the real/final expectations for the endpoints.

## Dependencies
* [requests](http://python-requests.org/)

For testing it also requires:

* [httpretty](https://github.com/gabrielfalcao/HTTPretty)
* [nose](https://github.com/nose-devs/nose/)

You can install them with [pip](http://pip.readthedocs.org/):
```sh
pip install -r requirements.txt
```

## Example
```python
from cartodb.db import TableSync

table_sync = TableSync('localhost', 8000, False)
table_sync.created('table_name_created', 'table_id_1')
```

## Tests
Tests can be run as unit tests or can run against a real service using the values specified in `tests_service.conf`.

```sh
make test # will run tests as unit tests
make test-conf # will run tests based on the endpoint configuration specified in tests_service.conf
```