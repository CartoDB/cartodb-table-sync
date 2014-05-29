import json
import requests


class TableSync(object):

    API_ENDPOINT_PATH = 'api/v1/tables/%(table_id)s/registar'

    def __init__(self, host, port, secure=False):
        self.host = host
        self.port = port
        self.secure = secure

    def created(self, table_id, table_name):
        return self._request('POST', table_id, table_name)

    def updated(self, table_id, table_name):
        return self._request('PUT', table_id, table_name)

    def deleted(self, table_id, table_name):
        return self._request('DELETE', table_id, table_name)

    def _request(self, method, table_id, table_name):
        response = requests.request(
            method,
            self._get_url(table_id),
            data=self._get_params(table_id, table_name),
            headers={'Content-type': 'application/json', 'Accept': 'application/json'}
        )
        return SyncResponse(response)

    def _get_url(self, table_id):
        return "%(protocol)s://%(host)s:%(port)s/%(path)s" % {
            'protocol': self._get_protocol(),
            'host': self.host,
            'port': self.port,
            'path': self._get_path(table_id)
        }

    def _get_protocol(self):
        return "https" if self.secure else "http"

    def _get_path(self, table_id):
        return self.API_ENDPOINT_PATH % {'table_id': table_id}

    @staticmethod
    def _get_params(table_id, table_name):
        return json.dumps({
            'table_id': table_id,
            'table_name': table_name
        })


class SyncResponse(object):
    def __init__(self, response):
        self.response = response
        try:
            self.json = response.json()
        except Exception, e:
            raise InvalidJsonResponseException(e)

    def ok(self):
        return self.json['status'] == 'ok'


class TableSyncException(Exception):
    """Base class for TableSync Exceptions"""
    pass


class InvalidJsonResponseException(TableSyncException):
    """Failed to parse response as JSON"""

    def __init__(self, exception):
        self.original_exception = exception
