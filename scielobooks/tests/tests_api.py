import unittest

from pyramid.config import Configurator
from pyramid import testing

class BooksListingTests(unittest.TestCase):
    def setUp(self):
        self.config = Configurator(autocommit=True)
        self.config.begin()

    def tearDown(self):
        self.config.end()

    def test_response_schema(self):
        from scielobooks.api.views import listing_books
        import tests_api_assets
        request = testing.DummyRequest()
        request.db = tests_api_assets.DummyCouchdb()
        request.route_path = tests_api_assets.route_path
        response = listing_books(request, tests_api_assets.DummyMonograph)

        for key in ['count', 'params', 'results']:
            self.assertTrue(key in response)

            if key == 'count':
                self.assertTrue(isinstance(response[key], int))
            elif key == 'params':
                self.assertTrue(isinstance(response[key], dict))
            elif key == 'results':
                self.assertTrue(isinstance(response[key], list))
            else:
                self.assertFalse()

    def test_results_schema(self):
        from scielobooks.api.views import listing_books
        import tests_api_assets
        self.maxDiff = None
        request = testing.DummyRequest()
        request.db = tests_api_assets.DummyCouchdb()
        request.route_path = tests_api_assets.route_path
        response = listing_books(request, tests_api_assets.DummyMonograph)
        results = response['results']
        self.assertTrue(isinstance(results, list))

        expected_book_meta = {
            'sbid': '329',
            'title': 'Capacita\u00e7\u00e3o docente e responsabilidade social: aportes pluridisciplinares',
            'isbn': '9788523206758',
            'creators': [
                            [
                                ['role','organizer'],
                                ['full_name','Ten\u00f3rio, Robinson Moreira'],
                                ['link_resume',None]
                            ],
                            [
                                ['role','organizer'],
                                ['full_name','Silva, Reginaldo de Souza'],
                                ['link_resume',None]
                            ]
                        ],
            'publisher': 'EDUFBA',
            'language': 'pt',
            'synopsis': 'Publicado pela Editora da Universidade Federal da Bahia',
            'year': '2010',
            'city': None,
            'country': 'BR',
            'pages': '326',
            'primary_descriptor': None,
            'edition': None,
            'format': [['height',None],['width',None]],
            'use_licence': 'CC BY-NC-SA 3.0',
            'doi_number': None,
            'chapters_count': 19,
            'pdf_url': 'catalog.pdf_file',
            'epub_url': 'catalog.epub_file',
            'cover_url': 'catalog.cover',
            'cover_thumbnail_url': 'catalog.cover_thumbnail',
            }
        self.assertEqual(expected_book_meta, results[0])


