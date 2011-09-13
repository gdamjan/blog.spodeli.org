#! /usr/bin/env python2
# -*- coding: utf8 -*-
from jinja2 import Environment, FileSystemLoader
from os import path
import sys, glob

BASEPATH = path.dirname(__file__)
TEMPLATES = path.join(BASEPATH, 'templates')

loader = FileSystemLoader(TEMPLATES)
env = Environment(loader=loader)

def template_glob(pathname):
    pathname = path.join(TEMPLATES, pathname)
    for fn in glob.iglob(pathname):
        if fn.startswith(TEMPLATES):
            yield fn[len(TEMPLATES):]
        else:
            yield fn

template = env.get_template('master.html')
print template.render(glob=template_glob).encode('utf-8')
