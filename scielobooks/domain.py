# encoding: utf-8
import couchdbkit

from scielobooks.staff import models as documental_models


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
        Add only if the chapter does not exist.
        """
        if item in self:
            return None
        super(Chapters, self).append(item)

    def append_or_update(self, item):
        """
        If an item already exists, it replaces the existing item with
        the new one.
        """
        if item in self:
            index = self.index(item)
            del(self[index])
        super(Chapters, self).insert(index, item)


class Book(object):


    __available_attrs = set(('title', 'titles_translated', 'isbn', 'creators', 'publisher',
            'publisher_url', 'language', 'synopsis', 'synopses_translated', 'publication_year',
            'publication_city', 'publication_country', 'total_pages', 'primary_descriptor',
            'primary_descriptors_translated', 'edition',
    ))

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.__chapters = Chapters()
        self.__creators = []

    def validate(self):
        return self.__check_mandatory()

    def __check_mandatory(self):
        """
        Check if all mandatory fields had been filled. Raises a
        TypeError if there is something missing.
        """
        mandatory = ['title', 'isbn', 'publisher',]
        for field in mandatory:
            if not hasattr(self, field):
                raise TypeError('Missing attribute %s' % field)

    def __setattr__(self, name, value):
        """
        Allows attribution only for the attributes referenced at __available_attrs
        or the ones with the names mangled (private scope).
        """
        if name not in self.__available_attrs and not name.startswith(
            '_{0}__'.format(self.__class__.__name__)):
            raise AttributeError
        super(Book, self).__setattr__(name, value)


    @property
    def chapters(self):
        return self.__chapters

    @property
    def creators(self):
        return self.__creators


class BookDbAdapter(object):
    """
    An adapter to handle domain and mapper objects integration.

    Retains a ``request`` instance only to access configurations
    and resource objects. Request attributes, GET POST or Cookies,
    are ignored.

    ``__attr_match`` holds the correspondence between Monograph and
    Book objects attributes. The match is defined by::

      (``Book attr``, ``Monograph attr``)
    """
    __attr_match = (('title', 'title'), ('titles_translated', 'translated_titles'),
            ('isbn', 'isbn'), ('creators', 'creators'), ('publisher', 'publisher'),
            ('publisher_url', 'publisher_url'), ('language', 'language'),
            ('synopsis', 'synopsis'), ('synopses_translated', 'translated_synopses'),
            ('publication_year', 'year'), ('publication_city', 'city'),
            ('publication_country', 'country'), ('total_pages', 'pages'),
            ('primary_descriptor', 'primary_descriptor'),
            ('primary_descriptors_translated', 'translated_primary_descriptors'),
            ('edition', 'edition'),
    )

    def __init__(self, request):
        self.__request = request

    def load(self, sbid):
        self.monograph = documental_models.Monograph.get(self.__request.db, sbid)

    def create_book_from_isisdm(self, data):
        book = Book()
        for domain_attr, isisdm_attr in self.__attr_match:
            if not data.has_key(isisdm_attr):
                continue

            if isisdm_attr == 'creators':
                creator_gen = (dict(creator) for creator in data[isisdm_attr])
                for creator in creator_gen:
                    creator_attrs = {}
                    if creator.get('full_name', None):
                        creator_attrs['full_name'] = creator['full_name']
                    if creator.get('link_resume', None):
                        creator_attrs['link_to_resume'] = creator['link_resume']
                    if creator['role'] == 'individual_author':
                        c = IndividualAuthor(**creator_attrs)

                    book.creators.append(c)
                continue

            setattr(book, domain_attr, data[isisdm_attr]) #simple attrs

        return book

