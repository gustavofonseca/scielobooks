#!/usr/bin/env python
# encoding: utf-8
import unittest
from scielobooks.domain import IndividualAuthor
from scielobooks.domain import Chapter
from scielobooks.domain import Book


class testChapter(unittest.TestCase):

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



class testBook(unittest.TestCase):

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

    def test_unknown_attribute(self):
        attrs = {'title': u'Gödel, Escher, Bach: An Eternal Golden Braid',
                 'reversed_title': u'diarB nedloG lanretE nA :hcaB ,rehcsE ,ledöG',
                 'isbn': '978-0465026562',
                 'publisher': 'Basic Books',
                 }
        self.assertRaises(AttributeError, Book, **attrs)



