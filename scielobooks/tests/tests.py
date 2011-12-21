import unittest
import os
from pyramid.config import Configurator
from pyramid import testing

HERE_PATH = os.path.abspath(os.path.dirname(__file__))

CONFIG_PATH = os.path.join(HERE_PATH, '..', '..')
for conf in ['production.ini', 'development.ini']:
    f = os.path.join(CONFIG_PATH, conf)
    if os.path.isfile(f):
        CONFIG_FILE = f
        break
else:
    raise IOError()

class DummyCouchDB(object):
    """
    Mock of couchdbkit database interface
    """
    def get(self, sbid):
        import json
        return json.load(open('fakedoc-w2.json'))

    def view(self, *args, **kwargs):
        return []

def _get_fresh_db():
    """
    Returns a dummy CouchDB database object
    """
    return DummyCouchDB()

def _dummy_route_path(*args, **kwargs):
    """Dummy route path method"""


class ConfigTests(unittest.TestCase):
    def test_couchdb_connection(self):
        """
        Check connectivity with CouchDB, and
        the existance of the configured db.
        """
        import couchdbkit
        import ConfigParser
        config = ConfigParser.ConfigParser()
        config.read(CONFIG_FILE)
        server = couchdbkit.Server(config.get('app:scielobooks', 'db_uri'))

        self.assertTrue(config.get('app:scielobooks', 'db_name') in server)

# Unit tests
class CatalogViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_book_details(self):
        """
        Check the existance of mandatory data on
        the view return.
        """
        from scielobooks.catalog.views import book_details

        request = testing.DummyRequest()
        request.matchdict['sbid'] = 'w2'
        request.db = _get_fresh_db()
        request.route_path = _dummy_route_path
        request.registry.settings['solr_url'] = ''
        response = book_details(request)

        for key in ['document', 'book_attachments', 'parts', 'cover_thumb_url',
                    'cover_full_url', 'breadcrumb', 'main', 'current_language']:
            self.assertTrue(key in response)