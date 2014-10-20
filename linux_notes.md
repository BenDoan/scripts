Commands
========

##Collapse newlines

    tr "\n" " "

##Setup Virtualenv

    virtualenv --no-site-packages env
    . env/bin/activate
    deactivate

## deploy python module to pypi

    python setup.py register sdist bdist_wheel upload
