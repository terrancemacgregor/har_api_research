# -*- coding: utf-8 -*-
"""har python reader

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Todo:
    * Build command line tool.

Author: Terrance Macgregor
License:

"""

import json


data = json.load(open('./sample_input/har_file_sample.json'))
urls = []
request_types = []

for entry in data["log"]["entries"]:
    request = entry["request"]
    urls.append(request["method"]+ ","+request["url"])
    request_types.append(request["method"])

def method_count (type):
    print(type+ " methods are: ")
    count = 0;
    for url in set(urls):
        if type in url:
            print(url)
            count += 1

    print("The total "+ type + " count = " + str(count))
    print()


for method in set(request_types):
    method_count(method);