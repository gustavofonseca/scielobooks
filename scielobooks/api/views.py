#coding: utf-8
from pyramid.response import Response
import couchdbkit

from ..staff.models import Monograph

def listing_books(request, monograph=Monograph):
    try:
       books = request.db.view('scielobooks/visible_books', include_docs=True)
    except couchdbkit.ResourceNotFound:
        raise exceptions.NotFound()

    results = []
    for book in books:
        try:
            parts = request.db.view('scielobooks/visible_monographs_and_parts', include_docs=False, key=[book['id'], 1])
        except couchdbkit.ResourceNotFound:
            raise exceptions.NotFound()

        mono = monograph.get(request.db, book['id'])

        book_meta = {
            'sbid': book['id'],
            'title': book['doc'].get('title', None),
            'isbn': book['doc'].get('isbn', None),
            'creators': book['doc'].get('creators', None),
            'publisher': book['doc'].get('publisher', None),
            'language': book['doc'].get('language', None),
            'synopsis': book['doc'].get('synopsis', None),
            'year': book['doc'].get('year', None),
            'city': book['doc'].get('city', None),
            'country': book['doc'].get('country', None),
            'pages': book['doc'].get('pages', None),
            'primary_descriptor': book['doc'].get('primary_descriptor', None),
            'edition': book['doc'].get('edition', None),
            'format': book['doc'].get('format', None),
            'use_licence': book['doc'].get('use_licence', None),
            'doi_number': book['doc'].get('doi_number', None),
            'chapters_count': parts.count(),
            'pdf_url': request.route_path('catalog.pdf_file', sbid=book['id'], part=mono.shortname),
            'epub_url': request.route_path('catalog.epub_file', sbid=book['id'], part=mono.shortname),
            'cover_url': request.route_path('catalog.cover', sbid=book['id']),
            'cover_thumbnail_url': request.route_path('catalog.cover_thumbnail', sbid=book['id']),
            }
        results.append(book_meta)

    response = {'count': books.total_rows, 'params': {}, 'results': results}
    return response