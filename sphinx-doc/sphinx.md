# Sphinx docs

- [Sphinx docs](#sphinx-docs)
  - [Comments](#comments)
    - [Example](#example)
  - [Steps for installation](#steps-for-installation)

## Comments

1. **Each function comment** is encapsulated in triple quotation marks ("), each comment has to be placed after function definition
2. A brief **title** cal be displayed in the documentation by writing it straigt after the first 3 quotation marks
3. You can describe various function specifications
   - :param kind: Optional "kind" of ingredients.
     - To specify a function parameter, its usage or describing its content
   - :type kind: list[str] or None
     - To specify the tipe of the parameter
     - It will be displayed in between round brackets
   - :return: The ingredients list.
     - To specify the return describing its content
   - :rtype: list[str]
     - To specify the return type

### Example

```text
Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. py:function:: lumache.get_random_ingredients(kind=None)

   Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :return: The ingredients list.
   :rtype: list[str]
```

Which will render like this:

![renderExample][lumache_example]

## Steps for installation

1. `sudo apt install python-sphinx && sudo pip install sphinx_rtd_theme`
2. Aprire progetto python con tutti i moduli
3. Creare una directory "docs"
4. `sphinx-quickstart`
5. Default settings apart from:
   - Project name
   - Author Name
   - Autodoc -> "y"
   - Create Makefile -> "y"
   - Create Windows command file -> "n"
6. Edit "conf.py"
   - Uncomment
     - Import os
     - Import sys
   - change sys.path.insert from '.' to '..' since os.path.abspath is in the project source path
   - change html_theme to 'shinx_rtd_theme'
7. Edit "index.rst"
   - Add "modules" indented as "toctree::"
8. `sphinx-apidoc -o . ..` output path in current path and source modules in parent ("..") directory
9. make html
10. open _build/html/index.html too see documentation

[lumache_example]: ./lumache-py-function.png
