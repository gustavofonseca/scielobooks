__available_attrs = ('title', '')


Mapeamento entre esquema dos objetos de persistência e objetos de domínio
==========================================================================

Book:
------
+---------------------------------------------------------------------------------------------------------------------------------------+
| persistency class attr         | domain class attr                   | ref api | is required? | usage sample                                  |
+=======================================================================================================================================+
| title                          | book.title                          |         | x            | book.title = 'foo'
| translated_titled              | book.titles_translated              | dict    |              | book.titles_translated['en'] = 'bar'
| isbn                           | book.isbn                           |         | x            | book.isbn = 'foo'
| creators                       | book.creators                       | list    |              | chapter.creators.append(emilia)
| publisher*                     | book.publisher                      |         | x            | book.publisher = 'foo'
| publisher_url                  | book.publisher_url                  |         |              | book.publisher_url = 'http://foo.com/ref=9876'
| language                       | book.language                       |         |              | book.language = 'pt'
| synopsis                       | book.synopsis                       |         |              | book.synopsis = 'foo'
| translated_synopses            | book.synopses_translated            | dict    |              | book.synopses_translated['en'] = 'bar'
| year                           | book.publication_year               |         |              | book.publication_year = 2000
| city                           | book.publication_city               |         |              | book.publication_city = 'Santos'
| country                        | book.publication_country            |         |              | book.publication_country = 'Brazil'
| pages                          | book.total_pages                    |         |              | book.total_pages = 123
| primary_descriptor             | book.primary_descriptor             |         |              | book.primary_descriptor = 'foo'
| translated_primary_descriptors | book.primary_descriptors_translated | dict    |              | book.primary_descriptors_translated['en'] = 'foo'
| edition                        | book.edition                        |         |              | book.edition = 'foo'


Chapter:
--------

+-----------------------------------------------------------------------------------------------------------------------------------------+
| persistency class attr                | domain class attr       | ref api | is required? | usage sample                                  |
+=========================================================================================================================================+
| part.creators                         | chapter.title           |         | x            | book.title = 'foo'
| part.text_language                    | chapter.language        |         |              | book.language = 'pt'
| part.pages                            | chapter.pages           | dict    |              | book.pages['initial|final'] = 123


##title = model.TextProperty(required=True)
##translated_titles = model.MultiCompositeTextProperty(subkeys=['title','language'])
##isbn = model.TextProperty(required=True)
#creators = model.MultiCompositeTextProperty(subkeys=['role','full_name', 'link_resume'])
#publisher = model.TextProperty(required=True)
#publisher_url = model.TextProperty()
#language = model.TextProperty()
#synopsis = model.TextProperty()
#translated_synopses = model.MultiCompositeTextProperty(subkeys=['synopsis','language'])
#year = model.TextProperty()
#city = model.TextProperty()
#country = model.TextProperty()
#pages = model.TextProperty()
#primary_descriptor = model.TextProperty()
#translated_primary_descriptors = model.MultiCompositeTextProperty(subkeys=['primary_descriptor','language'])
#edition = model.TextProperty()
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
created_by = model.TextProperty()