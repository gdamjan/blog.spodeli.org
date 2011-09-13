blog.spodeli.org
================

This is the build system for the blog.spodeli.org template on Blogger.

Self contained install and run::

    export PYTHONUSERBASE=$PWD/env
    pip install --user Jinja2
    ./build.py              # make sure everything is ok, then
    ./build.py > output.xml # make a file, or
    ./build.py | xclip      # copy it to your X clipboard
