#!/usr/bin/env python
# encoding: utf-8
import unittest

from pyramid import testing

from scielobooks.domain import IndividualAuthor
from scielobooks.domain import Chapter
from scielobooks.domain import Book
from scielobooks.domain import BookDbAdapter
from scielobooks.tests import tests
from scielobooks.tests import tests_assets


class ChapterTest(unittest.TestCase):


    def __basic_chapter(self):
        chapter = Chapter()
        chapter.title = u'Tópicos avançados'
        chapter.title_translations['us_EN'] = 'Advanced Topics'

        return chapter

    def test_basic(self):
        attrs = {'title': u'Introdução ao estudo da emancipação política do Brasil',}
        chapter = Chapter(**attrs)

        self.assertEqual(chapter.title, attrs['title'])

    def test_creator(self):
        emilia = IndividualAuthor(u'Costa, Emília Viotti da', u'http://pt.wikipedia.org/wiki/Emília_Viotti_da_Costa')
        chapter = self.__basic_chapter()

        chapter.creators.append(emilia)

        self.assertEqual(len(chapter.creators), 1)
        self.assertEqual(chapter.creators[0].full_name, u'Costa, Emília Viotti da')
        self.assertEqual(chapter.creators[0].link_to_resume, u'http://pt.wikipedia.org/wiki/Emília_Viotti_da_Costa')

    def test_translated_title(self):
        chapter = self.__basic_chapter()

        self.assertEqual(chapter.title, u'Tópicos avançados')
        self.assertEqual(chapter.title_translations['us_EN'], 'Advanced Topics')

    def test_translated_title_deletion(self):
        chapter = self.__basic_chapter()

        self.assertEqual(chapter.title_translations['us_EN'], 'Advanced Topics')
        del(chapter.title_translations['us_EN'])
        self.assertFalse('us_EN' in chapter.title_translations)

    def test_unicode(self):
        chapter = self.__basic_chapter()

        self.assertEqual(unicode(chapter), u'Tópicos avançados')


class BookTest(unittest.TestCase):


    def __basic_book(self):
        attrs = {'title': u'Gödel, Escher, Bach: An Eternal Golden Braid',
                 'isbn': '978-0465026562',
                 'publisher': 'Basic Books',
                 }
        book = Book(**attrs)

        return book

    def __basic_chapter(self):
        chapter = Chapter()
        chapter.title = u'Tópicos avançados'
        chapter.title_translations['us_EN'] = 'Advanced Topics'

        return chapter

    def test_basic(self):
        book = self.__basic_book()

        self.assertEquals(book.title, u'Gödel, Escher, Bach: An Eternal Golden Braid')

    def test_chapter(self):
        book = self.__basic_book()
        chapter = self.__basic_chapter()
        book.chapters.append(chapter)

        self.assertEqual(len(book.chapters), 1)

    def test_duplicated_chapter(self):
        book = self.__basic_book()
        chapter1 = self.__basic_chapter()

        book.chapters.append(chapter1)
        book.chapters.append(chapter1)

        self.assertEqual(len(book.chapters), 1)

    def test_updated_chapter(self):
        book = self.__basic_book()
        chapter1 = self.__basic_chapter()
        book.chapters.append(chapter1)

        self.assertEqual(len(book.chapters), 1)

        chapter2 = chapter1
        chapter2.title = 'Intermediate Topics'
        book.chapters.append_or_update(chapter2)

        self.assertEqual(len(book.chapters), 1)
        self.assertTrue(book.chapters[0] is chapter2)

    def test_missing_mandatory_attribute(self):
        """
        Missing a mandatory attribute
        """
        attrs = {'isbn': '978-0465026562',
                 'publisher': 'Basic Books',
                 }
        book = Book(**attrs)
        self.assertRaises(TypeError, book.validate)

    def test_unknown_attribute(self):
        attrs = {'title': u'Gödel, Escher, Bach: An Eternal Golden Braid',
                 'reversed_title': u'diarB nedloG lanretE nA :hcaB ,rehcsE ,ledöG',
                 'isbn': '978-0465026562',
                 'publisher': 'Basic Books',
                 }
        self.assertRaises(AttributeError, Book, **attrs)


class BookDbAdapterTest(unittest.TestCase):


    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    # def test_load(self):
    #     request = testing.DummyRequest()
    #     request.matchdict['sbid'] = 'w2'
    #     request.db = tests._get_fresh_db()

    #     db_adapter = BookDbAdapter(request)
    #     book = db_adapter.load(request.matchdict['sbid'])

    #     self.assertTrue(isinstance(book, Book))

    #tests for create_book_from_isisdm
    def test_from_isisdm_missing_attr(self):
        request = testing.DummyRequest()
        db_adapter = BookDbAdapter(request)

        self.assertRaises(TypeError, db_adapter.create_book_from_isisdm, tests_assets.isisdm_should_fail)


    def test_from_isisdm_creators(self):
        request = testing.DummyRequest()
        db_adapter = BookDbAdapter(request)

        #testing creators attr
        book = db_adapter.create_book_from_isisdm(tests_assets.isisdm_should_work)

        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.title, u'Argamassas tradicionais de cal')
        self.assertEqual(len(book.creators), 1)
        self.assertTrue(isinstance(book.creators[0], IndividualAuthor))
        self.assertEqual(book.creators[0].full_name, u'Santiago, Cybèle Celestino')
