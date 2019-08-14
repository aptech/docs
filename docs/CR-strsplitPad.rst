
strsplitPad
==============================================

Purpose
----------------
Splits a string vector into a string array of the individual tokens. Pads on the right with null strings.

Format
----------------
.. function:: sa = strsplitPad(sv, n_cols)

    :param sv: data
    :type sv: Nx1 string array

    :param n_cols: number of columns of output string array.
    :type n_cols: scalar

    :return sa: 

    :type sa: Nx n_cols string array

Remarks
-------

Rows containing more than *n_cols* tokens are truncated and rows
containing fewer than *n_cols* tokens are padded on the right with null
strings. The following characters are considered delimiters between
tokens:

+-----------------+----------+
| space           | ASCII 32 |
+-----------------+----------+
| tab             | ASCII 9  |
+-----------------+----------+
| comma           | ASCII 44 |
+-----------------+----------+
| newline         | ASCII 10 |
+-----------------+----------+
| carriage return | ASCII 13 |
+-----------------+----------+

Tokens containing delimiters must be enclosed in single or double quotes
or parentheses. Tokens enclosed in single or double quotes will NOT
retain the quotes upon translation. Tokens enclosed in parentheses WILL
retain the parentheses after translation. Parentheses cannot be nested.

Examples
----------------

::

    string sv = {
       "alpha beta gamma",
       "delta, epsilon, zeta, eta",
       "theta iota kappa"
    };
     
     sa = strsplitPad(sv, 4);

After the code above, *sa* will be equal to:

::

    "alpha"    "beta" "gamma"    ""
    "delta" "epsilon"  "zeta" "eta"
    "theta"    "iota" "kappa"    ""

.. seealso:: Functions :func:`strsplit`

