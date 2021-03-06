import copy
import urllib2
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import deform
from isis import model

from ..utilities import functions

class Monograph(model.CouchdbDocument):
    title = model.TextProperty(required=True)
    translated_titles = model.MultiCompositeTextProperty(subkeys=['title','language'])
    isbn = model.TextProperty(required=False)
    eisbn = model.TextProperty(required=False)
    is_comercial = model.BooleanProperty()
    shopping_info = model.MultiCompositeTextProperty(subkeys=['store','book_url'])
    creators = model.MultiCompositeTextProperty(subkeys=['role','full_name', 'link_resume'])
    publisher = model.TextProperty(required=True)
    publisher_url = model.TextProperty()
    language = model.TextProperty()
    synopsis = model.TextProperty()
    translated_synopses = model.MultiCompositeTextProperty(subkeys=['synopsis','language'])
    year = model.TextProperty()
    city = model.TextProperty()
    country = model.TextProperty()
    pages = model.TextProperty()
    primary_descriptor = model.TextProperty()
    translated_primary_descriptors = model.MultiCompositeTextProperty(subkeys=['primary_descriptor','language'])
    bisac_code =  model.MultiCompositeTextProperty(subkeys=['code'])
    edition = model.TextProperty()
    collection = model.CompositeTextProperty(subkeys=['individual_author', 'corporate_author', 'title', 'english_translated_title', 'total_number_of_volumes'])
    format = model.CompositeTextProperty(subkeys=['height', 'width'])
    serie = model.CompositeTextProperty(subkeys=['title', 'issue', 'issue_number', 'issn'])
    use_licence = model.TextProperty()
    doi_number = model.TextProperty()
    notes = model.TextProperty()
    pdf_file = model.FileProperty()
    epub_file = model.FileProperty()
    cover = model.FileProperty()
    toc = model.FileProperty()
    editorial_decision = model.FileProperty()

    cover_thumbnail = model.FileProperty()
    visible = model.BooleanProperty()
    creation_date = model.TextProperty()
    created_by = model.TextProperty() #TODO
    publication_date = model.TextProperty()

    class Meta:
        hide = ('cover_thumbnail', 'visible', 'creation_date', 'created_by')

    def _creators_by_roles(self):
        creators_by_role = OrderedDict()
        try:
            for creator in self.creators:

                creators_by_role.setdefault(creator['role'], []).append(
                    (creator['full_name'], creator['link_resume']))
        except AttributeError:
            return {}

        return copy.deepcopy(creators_by_role)

    def formatted_creators(self, formatting_func=None):
        # {'author': 'Babbage, Charles; Turing, Alan.'}
        if formatting_func is None:
            def formatting_func(creators):
                """
                accept a list of creators and returns it in a formatted form.
                """
                if len(creators) > 3:
                    return creators[0][0] + ' et al.'

                return '; '.join([creator[0] for creator in creators])

        creators_by_role = self._creators_by_roles()

        return OrderedDict((key, formatting_func(value)) for key, value in creators_by_role.items())

    def __get_cleaned_lastname(self, author):
        return functions.slugify(author).split('-')[0]

    @property
    def shortname(self):
        shortname_format = '%s-%s'
        creators_by_role = self._creators_by_roles()
        precedence = ('individual_author', 'organizer', 'coordinator', 'translator', 'collaborator', 'editor', 'corporate_author', 'other')
        for role in precedence:
            if role in creators_by_role:
                first_author = creators_by_role[role][0][0]
                first_author_lastname = self.__get_cleaned_lastname(first_author)

                try:
                    prefered_isbn = self.eisbn
                except AttributeError:
                    prefered_isbn = self.isbn

                return shortname_format % (first_author_lastname, prefered_isbn)
        else:
            raise AttributeError()

    def html_formatted_creators(self):
        """
        Calls self.formatted_creators passing a custom formatting function.
        """
        def formatting_func(creators):

            linked_creators = []
            for creator in creators:
                if creator[1]:
                    linked_creators.append(u'<a href="'+creator[1]+u'" target="_blank">'+creator[0]+u'</a>')
                else:
                    linked_creators.append(creator[0])

            if len(linked_creators) > 3:
                return linked_creators[0] + ' <i>et al.</i>'

            return '; '.join(linked_creators)

        return self.formatted_creators(formatting_func)

class Part(model.CouchdbDocument):
    title = model.TextProperty(required=True)
    translated_titles = model.MultiCompositeTextProperty(subkeys=['title','language'])
    order = model.TextProperty(required=True)
    creators = model.MultiCompositeTextProperty(required=False, subkeys=['role','full_name', 'link_resume'])
    pages = model.CompositeTextProperty(subkeys=['initial','final',])
    pdf_file = model.FileProperty()
    descriptive_information = model.TextProperty()
    text_language = model.TextProperty()
    notes = model.TextProperty()

    monograph = model.TextProperty(required=False)
    monograph_title = model.TextProperty(required=False)
    monograph_isbn = model.TextProperty(required=False)
    monograph_creators = model.MultiCompositeTextProperty(subkeys=['role','full_name', 'link_resume'])
    monograph_publisher = model.TextProperty(required=True)
    monograph_language = model.TextProperty()
    monograph_year = model.TextProperty()
    visible = model.BooleanProperty()
    publication_date = model.TextProperty()

    class Meta:
        hide = ('monograph', 'monograph_title', 'monograph_isbn', 'monograph_creators',
            'monograph_publisher', 'monograph_language', 'monograph_year', 'visible')
