# Prerequisites

## Step-by-Step Hands-on

1. Create a Python Project
```
my_project/
|-- my_module.py
```

```python
def greet(name: str) -> str:
    """Return a greeting message.
    
    Args:
    name (str): The name of the person.

    Returns:
    str: Greeting message.
    """
    return f"Hello, {name}!"
```

2. Install Sphinx and Related Tools

```
pip install sphinx sphinx_rtd_theme
```

3. Initialize Sphinx

```
cd my_project/
```
Run the Sphinx quickstart command:
```
sphinx-quickstart docs
```
or
```
python -m sphinx.cmd.quickstart
```
Answer the prompts as needed. For most options, the default is sufficient, but ensure that you enable autodoc when asked about extensions.

4. Configuration

Open docs/conf.py in an editor. Find and uncomment the following lines (they add the project to the sys.path and enable the sphinx_rtd_theme):

```python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
```
Also, set the theme to sphinx_rtd_theme:

```python
html_theme = 'sphinx_rtd_theme'
```
5. Generate API Documentation
From the docs/ directory, run:

```bash
sphinx-apidoc -o source/ ../
```
> in case f error:
> ```pip install -U sphinx```

This command will create .rst files for your modules in the source/ directory.

6. Add the API Documentation to the Main Documentation

Edit the docs/source/index.rst file to include the generated .rst files by adding your module's name to the toctree:

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   my_module
```

7. Build the Documentation
From the docs/ directory, run:

```bash
sphinx-build -b html source/ build/
```
