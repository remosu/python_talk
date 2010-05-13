#!/usr/bin/python

#try:
#    import locale
#    locale.setlocale(locale.LC_ALL, '')
#except:
#    pass

from docutils.core import publish_cmdline
from docutils.parsers.rst import directives


import rst_directive_old

#description = ('Generates S5 (X)HTML slideshow documents from standalone '
#               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer_name='s5')
