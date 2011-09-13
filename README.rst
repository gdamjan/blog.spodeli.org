blog.spodeli.org
================

This is the build system for the blog.spodeli.org template on Blogger.

Self contained install and run::

    export PYTHONUSERBASE=$PWD/env
    pip install --user Jinja2
    ./build.py
    ./build.py > output.xml
