#coding: utf-8

class MutantList(list):
    def __init__(self, *args, **kwargs):
        super(MutantList, self).__init__(*args, **kwargs)

    @property
    def total_rows(self):
        return len(self)

    def count(self):
        return len(self)

class DummyCouchdb(object):
    def view(self, *args, **kwargs):
        if args[0] == 'scielobooks/visible_books' and kwargs['include_docs'] == True:
            data = MutantList()
            data.append({'id':'329',
                    'key':'329',
                    'value':None,
                    'doc':{
                        '_id':'329',
                        '_rev':'4-e21e40711969222791b6337545ecaf83',
                        'isbn':'9788523206758',
                        'pdf_file':{
                            'uid':'pdfuid',
                            'filename':'cap_doc_res_soc_full.pdf'
                        },
                        'translated_synopses':[],
                        'collection':[
                            ['individual_author',None],
                            ['corporate_author',None],
                            ['title',None],
                            ['english_translated_title',None],
                            ['total_number_of_volumes',None]
                        ],
                        'visible':True,
                        'use_licence':'CC BY-NC-SA 3.0',
                        'year':'2010',
                        'pages':'326',
                        'translated_primary_descriptors':[],
                        'publisher':'EDUFBA',
                        'cover_thumbnail':{
                            'uid':'',
                            'filename':'cover.jpg.thumb.jpeg'
                        },
                        'language':'pt',
                        'title':'Capacita\u00e7\u00e3o docente e responsabilidade social: aportes pluridisciplinares',
                        'country':'BR',
                        'format':[['height',None],['width',None]],
                        'cover':{
                            'uid':'coveruid',
                            'filename':'cover.jpg'
                        },
                        'synopsis':'Publicado pela Editora da Universidade Federal da Bahia',
                        'translated_titles':[],
                        'creators':[
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
                        'TYPE':'Monograph',
                        'serie':[
                            ['title',None],
                            ['issue',None],
                            ['issue_number',None],
                            ['issn',None]
                        ],
                        '_attachments':{
                            'cover.jpg.thumb.jpeg':{
                                'content_type':'image/jpeg',
                                'revpos':4,
                                'digest':'md5-NCSS3m1gTzXQQJQeeV5gbw==',
                                'length':4871,
                                'stub':True
                            },
                            'cover.jpg':{
                                'content_type':'image/jpeg',
                                'revpos':3,
                                'digest':'md5-pjzJlSVs/uWkmGJnm9kPKA==',
                                'length':3373926,
                                'stub':True
                            },
                            'cap_doc_res_soc_full.pdf':{
                                'content_type':'application/pdf',
                                'revpos':2,
                                'digest':'md5-J1cA76AvSJLMc00gRfgPkw==',
                                'length':1194977,
                                'stub':True
                            }
                        }
                    }
                })

        elif args[0] == 'scielobooks/visible_monographs_and_parts' and kwargs['include_docs'] == False:
            data = MutantList()
            data += [{'id':'32b','key':['329',1],'value':None},
                    {'id':'32c','key':['329',1],'value':None},
                    {'id':'32d','key':['329',1],'value':None},
                    {'id':'32f','key':['329',1],'value':None},
                    {'id':'32g','key':['329',1],'value':None},
                    {'id':'32h','key':['329',1],'value':None},
                    {'id':'32j','key':['329',1],'value':None},
                    {'id':'32k','key':['329',1],'value':None},
                    {'id':'32m','key':['329',1],'value':None},
                    {'id':'32n','key':['329',1],'value':None},
                    {'id':'32p','key':['329',1],'value':None},
                    {'id':'32q','key':['329',1],'value':None},
                    {'id':'32r','key':['329',1],'value':None},
                    {'id':'32s','key':['329',1],'value':None},
                    {'id':'32t','key':['329',1],'value':None},
                    {'id':'32v','key':['329',1],'value':None},
                    {'id':'32w','key':['329',1],'value':None},
                    {'id':'32x','key':['329',1],'value':None},
                    {'id':'32y','key':['329',1],'value':None}]
        else:
            data = ''

        return data

def route_path(route_name, **kwargs):
    if route_name == 'catalog.pdf_file':
        return 'catalog.pdf_file'
    elif route_name == 'catalog.epub_file':
        return 'catalog.epub_file'
    elif route_name == 'catalog.cover_thumbnail':
        return 'catalog.cover_thumbnail'
    elif route_name == 'catalog.cover':
        return 'catalog.cover'

class DummyMonograph(object):
    @classmethod
    def get(cls, *args, **kwargs):
        return cls()

    def shortname(self):
        return 'tenorio-9788523206758'