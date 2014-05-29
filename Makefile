test:
	nosetests test_table_sync.py

test-conf:
	cp tests_service.conf .tests.conf
	- nosetests test_table_sync.py
	rm .tests.conf
