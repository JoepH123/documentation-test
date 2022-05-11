.. _documentation-with-sphinx:
Documentation with Sphinx
=================================

Project with Sphinx documentation (from scratch)
----------------------------------------------------------------------------
Explaining how to create a by Sphinx documented project helps to understand how Sphinx works, and can be useful if any new repository needs to be created.

- Make a project with a virtual environment (and make sure that you are navigated into this project within the command prompt).

- Activate the virtual environment

- In command prompt perform

    .. code-block:: php

       pip install sphinx
       pip install numpydoc
       pip install sphinx-rtd-theme
       mkdir docs (in the project directory)
       mkdir sphinx (in the project)
       cd sphinx (navigate to sphinx folder)

- During the quickstart, say ``[y]``, when asked to have separate build and source folders

    .. code-block:: php

       sphinx-quickstart

- Make some changes in the ``conf.py`` file

   - Add extensions

    .. code-block:: python

       'sphinx.ext.autodoc', 'numpydoc'

   - Uncomment

    .. code-block:: python

       import os
       import sys

   - Add the following code

    .. code-block:: python

        # ##### -> Code for the following structure of code folder:
        # folder with app.py and then all the folders other code files in this folder
        # or in sub-folders underneath the src folder

        directory = '../../src/'
        # How to get from the conf.py file to the code

        # Add the app.py to the sys.path which the conf.py file needs to make automatic documentation
        sys.path.insert(0, os.path.abspath('../../src/'))

        # Add all sub-folders in the src folder which contain the python files
        # This way all the python files can be accessed.
        for root, subdirectories, files in os.walk(directory):
            for subdirectory in subdirectories:
                sys.path.insert(0, os.path.abspath(os.path.join(root, subdirectory)))
            for file in files:
                # print(os.path.join(root, file))
                pass

   - Change the theme

   .. code-block:: python

      html_theme = 'sphinx_rtd_theme'

.. note::
   ``Add the following code`` makes sure that the conf.py file can actually find all the python files that it needs to supply to autodoc.
   Autodoc basically receives some python files and extracts all the docstrings to form a good-looking documentation page for these python files.
   It needs to be able to know where these files are located. Otherwise it cannot create the documentation for it. It now uses ``src``
   as the folder that contains all the code. All files and in this ``src`` folder and the sub-folders of ``src`` should be python files. Only these files
   python files will be included in the documentation. Unless other files are inserted or the code is changed, to include even more files.

.. warning::
   All python files not included in the ``src`` folder will not be included in the documentation.

- In order to now generate the documentation of the project, a few commands need to be executed within the command prompt.

- Make sure that all the files that need documentation are added to the ``sphinx/source`` directory with the use of the following commands:

    .. code-block:: php

       sphinx-apidoc -o sphinx\source src
       sphinx-apidoc -o sphinx\source src\utils_folder
       same for all folders in ``src`` folder

.. note::
   ``sphinx-apidoc -o sphinx\source src`` only make sure that all the loose python files in the ``src`` directory are converted
   to ``.rst`` files and saved into the ``sphinx\source`` directory. For the python files in sub-folder in the `src` directory,
   the same command needs to be ran for each of the folder within the ``src`` folder.

- Navigate to the sphinx folder and call:

    .. code-block:: php

       make html

- If anything goes wrong, or you need to reload the html files. You can clean (empty) the ``sphinx\build`` folder and regenerate the html files, by calling:

    .. code-block:: php

       make clean
       make html

- In the ``sphinx/source`` folder, you can create new files, and pages for the documentation which are not automatically generated. Using, this property, you can create additional more specific and detailed documentation pages. For example to explain how to use create documentation for the KGA project.

- In the index page, you can create the landing page for the documentation.

- A final important topic is the ``toctrees``. These are properties of the ``.rst`` files, which help to link everything together into a final documentation webpage. The use of these toctrees will be discussed later in this documentation.