#!/usr/bin/env python
# encoding: utf-8
class Creator(object):
    def __init__(self, full_name, link_to_resume):
        self.full_name = full_name
        self.link_to_resume = link_to_resume


class IndividualAuthor(Creator):
    pass


class Chapter(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.__creators = []
        self.__title_translations = {}

    @property
    def creators(self):
        return self.__creators

    @property
    def title_translations(self):
        return self.__title_translations

    def __unicode__(self):
        return self.title

class Chapters(list):
    def append(self, item):
        """
        If an item already exists, it replaces the existing item with
        the new one.
        """
        if item in self:
            index = self.index(item)
            del(self[index])
        super(Chapters, self).append(item)

class Book(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.__chapters = Chapters()
        self.__check_mandatory()

    def __check_mandatory(self):
        """
        Check if all mandatory fields had been filled. Raises a
        TypeError if there is something missing.
        """
        mandatory = ['title', 'isbn', 'publisher',]
        for field in mandatory:
            if not hasattr(self, field):
                raise TypeError('Missing attribute %s' % field)

    @property
    def chapters(self):
        return self.__chapters