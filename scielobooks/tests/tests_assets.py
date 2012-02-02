# coding: utf-8
isisdm_should_fail = {
    'publisher': u'EDUFBA',
    'cover_thumbnail': {'uid': u'', 'filename': u'cover.jpg.thumb.jpeg'},
    'isbn': u'9788523204716',
    'language': u'pt',
    'title': u'Argamassas tradicionais de cal',
    'pdf_file': {'uid': u'pdfuid', 'filename': u'arg_tra_cal_full.pdf'},
    'country': u'BR',
    '_rev': u'10-624cf1c684abe61288cee55baac33284',
    'format': (('height', None), ('width', None)),
    'cover': {'uid': u'coveruid', 'filename': u'cover.jpg'},
    'collection': (
        ('individual_author', None),
        ('corporate_author', None),
        ('title', None),
        ('english_translated_title', None),
        ('total_number_of_volumes', None)
    ),
    '_id': u'w2',
    'serie': (
        ('title', None),
        ('issue', None),
        ('issue_number', None),
        ('issn', None)
    ),
    'synopsis': u'O livro faz uma retrospectiva sobre o que se pensava das argamassas de cal e alguns de seus constituintes ao longo dos s\xe9culos. Revela informa\xe7\xf5es \xfateis tanto do ponto de vista hist\xf3rico quanto para subsidiar obras de restaura\xe7\xe3o atrav\xe9s da an\xe1lise de textos italianos, franceses, portugueses, espanh\xf3is e brasileiros. \xc9 uma viagem no tempo, mostrando aspectos ligados \xe0 composi\xe7\xe3o, ao preparo e \xe0s propriedades das argamassas elaboradas com esse aglomerante comentados \xe0 luz da ci\xeancia contempor\xe2nea.',
    'use_licence': u'CC BY-NC-SA 3.0',
    'year': u'2007',
    'visible': True,
    'creators': (
        (
            ('role', u'individual_author'),
            ('full_name', u'Santiago, Cyb\xe8le Celestino'),
            ('link_resume', None)
        ),
    ),
    'TYPE': 'Monograph',
    'pages': u'202',
}

isisdm_should_work = {
    'publisher': u'EDUFBA',
    'cover_thumbnail': {'uid': u'', 'filename': u'cover.jpg.thumb.jpeg'},
    'isbn': u'9788523204716',
    'language': u'pt',
    'title': u'Argamassas tradicionais de cal',
    'pdf_file': {'uid': u'pdfuid', 'filename': u'arg_tra_cal_full.pdf'},
    'country': u'BR',
    '_rev': u'10-624cf1c684abe61288cee55baac33284',
    'format': (('height', None), ('width', None)),
    'cover': {'uid': u'coveruid', 'filename': u'cover.jpg'},
    'collection': (
        ('individual_author', None),
        ('corporate_author', None),
        ('title', None),
        ('english_translated_title', None),
        ('total_number_of_volumes', None)
    ),
    '_id': u'w2',
    'serie': (
        ('title', None),
        ('issue', None),
        ('issue_number', None),
        ('issn', None)
    ),
    'synopsis': u'O livro faz uma retrospectiva sobre o que se pensava das argamassas de cal e alguns de seus constituintes ao longo dos s\xe9culos. Revela informa\xe7\xf5es \xfateis tanto do ponto de vista hist\xf3rico quanto para subsidiar obras de restaura\xe7\xe3o atrav\xe9s da an\xe1lise de textos italianos, franceses, portugueses, espanh\xf3is e brasileiros. \xc9 uma viagem no tempo, mostrando aspectos ligados \xe0 composi\xe7\xe3o, ao preparo e \xe0s propriedades das argamassas elaboradas com esse aglomerante comentados \xe0 luz da ci\xeancia contempor\xe2nea.',
    'use_licence': u'CC BY-NC-SA 3.0',
    'year': u'2007',
    'visible': True,
    'creators': (
        (
            ('role', u'individual_author'),
            ('full_name', u'Santiago, Cyb\xe8le Celestino'),
            ('link_resume', r'http://avalidurl.com')
        ),
    ),
    'TYPE': 'Monograph',
    'pages': u'202',
}