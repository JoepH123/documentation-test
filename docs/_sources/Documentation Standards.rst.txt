.. _documentation-standards:
Documentation Standards
============================

Decisions on software and formatting
--------------------------------------------------------------
As has been discussed, Sphinx is the tool that is used for the creation of the documentation of the KGA project. It uses the documentation extracted from docstrings in python files together with other hand-written documentation files to form a complete and well-structured documentation page, which can be viewed in the browser. For the composition of docstrings, we use numpydoc. This is the documentation format which is used for the development of the NumPy project. It is a easily interpretable and well organized documentation format, which can be viewed in more detail on their website (numpydoc_). For the hand-written documentation files, which are used to create more in-depth and topic specific documentation, reStructuredText (RST) is used. This is a markup language that can be used to write beautiful documentations with many customizing options. This (.rst) file type and the language allow you to add in pictures, videos, code blocks, hyperlinks etc. to the documentation. For some examples, you can visit reStructuredText_, sphinx-RST_ and sphinx-RST-syntax-guide_ or you can google more specific questions.



.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/install.html
.. _reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html#external-hyperlink-targets
.. _sphinx-RST: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _sphinx-RST-syntax-guide: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
