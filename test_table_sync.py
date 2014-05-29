import ConfigParser
from cartodb import TableSync, InvalidJsonResponseException
import httpretty
import unittest


class TableSyncTest(unittest.TestCase):

    TABLE_ID = 'table_id_1'
    TABLE_NAME = 'table_name_created'

    JSON_CONTENT_TYPE = "application/json"
    STATUS_OK = 200
    RESPONSE_OK = '{"status": "ok"}'

    def setUp(self):
        tests_config = ConfigParser.RawConfigParser()
        try:
            tests_config.read(".tests.conf")
            self.host = tests_config.get('endpoint', 'host')
            self.port = tests_config.getint('endpoint', 'port')
            self.secure = tests_config.getboolean('endpoint', 'secure')
            self.mock_server = False
        except Exception:
            self.host = 'localhost'
            self.port = 8000
            self.secure = False
            self.mock_server = True

        if self.mock_server:
            httpretty.enable()
        self.table_sync = TableSync(self.host, self.port, self.secure)

    def tearDown(self):
        if self.mock_server:
            httpretty.disable()

    def test_created_happy_case(self):
        httpretty.register_uri(httpretty.POST, self._get_service_url(self.TABLE_ID),
                               body=self.RESPONSE_OK,
                               content_type=self.JSON_CONTENT_TYPE,
                               status=self.STATUS_OK)

        response = self.table_sync.created(self.TABLE_ID, self.TABLE_NAME)

        self.assertTrue(response.ok())

    def test_updated_happy_case(self):
        httpretty.register_uri(httpretty.PUT, self._get_service_url(self.TABLE_ID),
                               body=self.RESPONSE_OK,
                               content_type=self.JSON_CONTENT_TYPE,
                               status=self.STATUS_OK)

        response = self.table_sync.updated(self.TABLE_ID, self.TABLE_NAME)

        self.assertTrue(response.ok())

    def test_deleted_happy_case(self):
        httpretty.register_uri(httpretty.DELETE, self._get_service_url(self.TABLE_ID),
                               body=self.RESPONSE_OK,
                               content_type=self.JSON_CONTENT_TYPE,
                               status=self.STATUS_OK)

        response = self.table_sync.deleted(self.TABLE_ID, self.TABLE_NAME)

        self.assertTrue(response.ok())

    def test_invalid_json_raises_exception(self):
        httpretty.register_uri(httpretty.DELETE, self._get_service_url(self.TABLE_ID),
                               body='INVALIDJSON',
                               content_type=self.JSON_CONTENT_TYPE,
                               status=self.STATUS_OK)

        with self.assertRaises(InvalidJsonResponseException):
            self.table_sync.deleted(self.TABLE_ID, self.TABLE_NAME)

    def _get_service_url(self, table_id):
        return "%s://%s:%s/%s" % (
            'https' if self.secure else 'http',
            self.host,
            self.port,
            TableSync.API_ENDPOINT_PATH % {'table_id': table_id}
        )
