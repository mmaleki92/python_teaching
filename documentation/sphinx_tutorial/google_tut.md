# Google-Style Python Documentation with Sphinx

Google-style docstrings provide an alternative to the NumPy-style, and are clear, readable, and concise. Here's how you can integrate them into your Sphinx documentation.

## 1. Set Up `napoleon` extension

Ensure you have the `napoleon` extension enabled in your `conf.py` file:

\```python
extensions = [
    ...
    'sphinx.ext.napoleon',
    ...
]
\```

This extension allows Sphinx to understand Google-style docstrings.

## 2. Writing Google-Style Docstrings

Google-style docstrings have a slightly different format compared to NumPy-style:

\```python
def function_name(param1, param2):
    """
    Brief description of the function.

    Args:
        param1 (data_type): Description of param1.
        param2 (data_type): Description of param2.

    Returns:
        data_type: Description of the return value.
    """
    ...
\```

Differences include:

- Using `Args:` instead of `Parameters`.
- Parameter type is specified in parentheses after the parameter name.

### Comprehensive Example

\```python
def example_function(param1, param2=0):
    """
    This is an example function with Google-style docstrings.

    Args:
        param1 (int): The first parameter.
        param2 (int, optional): The second parameter. Defaults to 0.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If `param1` is equal to `param2`.

    Examples:
        >>> example_function(3, 2)
        True
        >>> example_function(2, 2)
        ValueError
    """
    ...
\```

## 3. Generate Documentation

Run Sphinx to generate the documentation:

\```bash
make html
\```

## 4. Optional Customizations

If you want to exclusively use Google-style and exclude NumPy-style:

\```python
napoleon_google_docstring = True
napoleon_numpy_docstring = False
\```

Add the above to your `conf.py` file.

## 5. Viewing the Documentation

Open the output (commonly `_build/html/index.html`) in a web browser to see the formatted Google-style docstrings.

## 6. Further Customization

For more advanced configurations of the `napoleon` extension, refer to the [official Napoleon documentation](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html).

And that's it! You're now ready to use Google-style docstrings in your Sphinx documentation.
