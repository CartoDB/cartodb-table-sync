# ⚠️ ARCHIVED - This repository is no longer maintained

**This repository has been archived and is no longer actively maintained.**

This project was last updated on 2024-05-20 and is preserved for historical reference only.

- 🔒 **Read-only**: No new issues, pull requests, or changes will be accepted
- 📦 **No support**: This code is provided as-is with no support or updates
- 🔍 **For reference only**: You may fork this repository if you wish to continue development

For current CARTO projects and actively maintained repositories, please visit: https://github.com/CartoDB

---

CartoDB table metadata sync client
==================================
[![Build Status](http://travis-ci.org/CartoDB/cartodb-table-sync.png)](http://travis-ci.org/CartoDB/cartodb-table-sync)

Client abstracting the calls to Rails endpoints to notify tables changes: table creations, modifications and deletions.

## Project status
NOT READY: this project is under development, tests do not represent the real/final expectations for the endpoints.

## Installation
For now the package can be installed like in:
```sh
pip install git+https://github.com/CartoDB/cartodb-table-sync.git#egg=cartodb-table-sync
```

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