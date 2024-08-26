# -*- coding: utf-8 -*-
import os
import glob
import yaml
from collections import OrderedDict
from bs4 import BeautifulSoup

indices = {}
for f in glob.glob("docs/**/*.html"):
    soup = BeautifulSoup(open(f, "r").read(), features="html.parser")
    tags = soup.find_all('div', {'class': [
        'algorithm', 'definition', 'example', 'lemma', 'proposition', 'theorem'
        ]})
    for tag in tags:
        indices[tag['id']] = {
                'class': tag['class'][0],
                'name': tag['name'],
                'title': tag['title'],
                'path': os.path.relpath(f, 'docs'),
                'id': tag['id']
                }

with open('data/indices.yaml', 'w+') as out:
    yaml.dump(indices, out, allow_unicode=True, sort_keys=False)
