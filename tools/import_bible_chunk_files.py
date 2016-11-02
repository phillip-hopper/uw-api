from __future__ import print_function, unicode_literals

import inspect
import json
import os

import re
from general_tools.file_utils import write_file
from general_tools.print_utils import print_ok
from general_tools.url_utils import get_url


def import_now():

    regex1 = re.compile(r'(\[)\s+(\d)', re.UNICODE)
    regex2 = re.compile(r'(,)\s+?(\d)', re.UNICODE)
    regex3 = re.compile(r'(\d)\s+(\])', re.UNICODE)
    regex4 = re.compile(r'\s+(\n)', re.UNICODE)

    base_url = 'https://api.unfoldingword.org/bible/txt/1/'
    output_dir = os.path.join(os.path.dirname(inspect.stack()[0][1]), 'output')

    # get the list of books
    books_url = 'https://raw.githubusercontent.com/unfoldingWord-dev/uw-api/develop/static/versification/ufw/books.json'
    unsorted_books = json.loads(get_url(books_url))
    sorted_books = []

    for book in unsorted_books:
        sorted_books.append((book.lower(), unsorted_books[book][1]))

    sorted_books.sort(key=lambda x: x[1])

    # get the chunk definitions
    for book in sorted_books:
        file_contents = []
        chap_num = ''
        current = None
        print('Processing {0}'.format(book[0]))

        chunk_url = '{0}/{1}/chunks.json'.format(base_url, book[0])
        chunk_defs = json.loads(get_url(chunk_url))

        for chunk in chunk_defs:

            # is this is a different chapter?
            if chap_num != chunk['chp']:
                chap_num = chunk['chp']
                if current:
                    file_contents.append(current)
                current = {'chapter': int(chunk['chp']), 'first_verses': []}

            current['first_verses'].append(int(chunk['firstvs']))

        if current:
            file_contents.append(current)

        # format the output
        file_contents_str = json.dumps(file_contents, sort_keys=True, indent=2)
        file_contents_str = regex1.sub(r'\1\2', file_contents_str)
        file_contents_str = regex2.sub(r'\1 \2', file_contents_str)
        file_contents_str = regex3.sub(r'\1\2', file_contents_str)
        file_contents_str = regex4.sub(r'\1', file_contents_str)

        write_file(os.path.join(output_dir, '{0}.json'.format(book[0])), file_contents_str)


if __name__ == '__main__':
    import_now()
    print_ok('FINISHED: ', 'Done importing chunk definitions.')
