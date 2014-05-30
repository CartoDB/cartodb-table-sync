from distutils.core import setup

REQUIRES = ['requests']

setup(
    name='cartodb-table-sync',
    author='CartoDB',
    author_email='support@cartodb.com',
    description='Client abstracting the calls to Rails endpoints to notify tables changes',
    version='0.0.1',
    url='https://github.com/CartoDB/cartodb-table-sync',
    download_url='https://github.com/CartoDB/cartodb-table-sync/tarball/0.0.1',
    install_requires=REQUIRES,
    packages=['cartodb'],
    requires=REQUIRES,
    test_suite='test_table_sync'
)
