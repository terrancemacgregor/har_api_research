# -*- coding: utf-8 -*-
"""har python reader

Todo:
    * Build command line tool.

Author: Terrance Macgregor
License: MIT License

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