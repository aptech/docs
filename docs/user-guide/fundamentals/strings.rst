.. _strings:

Strings and String Arrays
===============================================

GAUSS has two text data types: **strings** and **string arrays**. A
string holds a single text value of any length. A string array is an
NxK matrix of strings — each element is a separate string.

This page covers creating strings, string operators, string arrays,
common string functions, and converting between strings and numbers.

.. note::

    If you are coming from Python, a GAUSS string is like a Python
    ``str``. A GAUSS string array is like a NumPy array of strings
    (``np.array(["a", "b", "c"])``).
    If you are coming from R, a GAUSS string array is like a character
    vector (``c("a", "b", "c")``).


Creating Strings
--------------------------------------------

Strings are created with double quotes:

::

    s = "Hello World";
    print s;

This prints:

::

    Hello World

Strings can contain any characters, including newlines and special
characters inserted with **escape sequences**:

.. list-table::
    :widths: 15 45 40
    :header-rows: 1

    * - Escape
      - Character
      - ASCII code

    * - ``\n``
      - Newline
      - 10

    * - ``\t``
      - Tab
      - 9

    * - ``\r``
      - Carriage return
      - 13

    * - ``\"``
      - Double quote
      - 34

    * - ``\\``
      - Literal backslash
      - 92

Example: Escape sequences
+++++++++++++++++++++++++++++++++

::

    s = "Line 1\nLine 2";
    print s;

    t = "col1\tcol2\tcol3";
    print t;

    p = "C:\\gauss\\data";
    print p;

This prints:

::

    Line 1
    Line 2
    col1	col2	col3
    C:\gauss\data

.. tip::

    On macOS and Linux, forward slashes work in file paths, so escape
    sequences are rarely needed: ``"/home/user/data"``.


String Operators
--------------------------------------------

.. list-table::
    :widths: 10 25 65
    :header-rows: 1

    * - Operator
      - Name
      - Description

    * - ``$+``
      - String concatenation
      - Joins strings end-to-end. Works element-wise on string arrays.

    * - ``$~``
      - Horizontal string array concatenation
      - Creates or extends a string array (side by side)

    * - ``$|``
      - Vertical string array concatenation
      - Creates or extends a string array (stacked)

    * - ``$==``
      - String equality
      - Returns 1 if strings match, 0 otherwise

    * - ``$/=``
      - String inequality
      - Returns 1 if strings differ, 0 otherwise

    * - ``$<``  ``$>``  ``$<=``  ``$>=``
      - String ordering
      - Lexicographic (alphabetical) comparison

The key distinction: ``$+`` produces a **single string** (text glued
together); ``$~`` and ``$|`` produce a **string array** (a collection
of separate strings). All string comparison operators (``$==``, ``$<``,
etc.) are **case-sensitive**.

Example: $+ vs. $~
+++++++++++++++++++++++++++++++++

::

    x = "age";
    y = "pay";
    z = "sex";

    // $+ joins into one string
    s = x $+ y $+ z;
    print s;
    print strlen(s);

    // $~ creates a 1x3 string array
    sa = x $~ y $~ z;
    print sa;
    print rows(sa) cols(sa);

This prints:

::

    agepaysex
       9.0000000

             age              pay              sex
       1.0000000        3.0000000

With ``$+``, the three words are glued into one 9-character string.
With ``$~``, they become three separate elements in a 1x3 string array.

Example: String comparison
+++++++++++++++++++++++++++++++++

::

    print "abc" $== "abc";
    print "abc" $== "xyz";
    print "abc" $/= "xyz";

This prints:

::

       1.0000000
       0.0000000
       1.0000000


String Arrays
--------------------------------------------

A string array is an NxK matrix where each element is a string. String
arrays are the standard way to work with collections of text in GAUSS —
column names, variable labels, file lists, categorical values, and more.

Creating string arrays
+++++++++++++++++++++++++++++++++

Use ``$~`` (horizontal) and ``$|`` (vertical) to build string arrays:

::

    // 1x3 row: horizontal concatenation
    row = "alpha" $~ "beta" $~ "gamma";
    print row;

    // 3x1 column: vertical concatenation
    col = "one" $| "two" $| "three";
    print col;

This prints:

::

           alpha             beta            gamma

             one
             two
           three

Build a 2D string array by combining both operators:

::

    m = ("a" $~ "b" $~ "c") $| ("x" $~ "y" $~ "z");
    print m;

This prints:

::

               a                b                c
               x                y                z

Indexing string arrays
+++++++++++++++++++++++++++++++++

String arrays use the same indexing syntax as numeric matrices
(see :ref:`operators`):

::

    sa = "alpha" $~ "beta" $~ "gamma";
    print sa[1, 2];        // "beta"

    sv = "one" $| "two" $| "three";
    print sv[2];           // "two"

    m = ("a" $~ "b" $~ "c") $| ("x" $~ "y" $~ "z");
    print m[2, 3];         // "z"

This prints:

::

    beta
    two
    z


Common String Functions
--------------------------------------------

GAUSS provides many functions for working with strings. Here are the
most commonly used ones, grouped by task.

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Function
      - Description

    * - :func:`strlen`
      - Returns the length (number of characters) of a string

    * - :func:`strsect`
      - Extracts a substring: ``strsect(s, start, len)``

    * - :func:`strindx`
      - Finds the position of a substring: ``strindx(s, target, start)``

    * - :func:`strreplace`
      - Replaces all occurrences of a substring

    * - :func:`strsplit`
      - Splits a string into a string array by delimiter

    * - :func:`strjoin`
      - Joins a string array into a single string with a separator

    * - :func:`upper`
      - Converts to uppercase

    * - :func:`lower`
      - Converts to lowercase

    * - :func:`strtrim`
      - Removes leading and trailing whitespace

    * - :func:`contains`
      - Tests whether a string array contains a value (returns 1 or 0)

    * - :func:`sprintf`
      - Formats values into a string: ``sprintf("x = %6.3f", 3.14)``

.. note::

    String positions are 1-based: the first character is at position 1,
    not 0.

Example: Extracting and searching
++++++++++++++++++++++++++++++++++++

::

    s = "Hello World";

    // Extract substring: start at position 1, length 5
    print strsect(s, 1, 5);

    // Extract substring: start at position 7, length 5
    print strsect(s, 7, 5);

    // Find position of "World" starting from position 1
    print strindx(s, "World", 1);

This prints:

::

    Hello
    World
       7.0000000

Example: Replacing and splitting
++++++++++++++++++++++++++++++++++++

::

    s = "Hello World";
    print strreplace(s, "World", "GAUSS");

    // Split a delimited string into a string array
    parts = strsplit("one,two,three", ",");
    print parts;

    // Join a string array back into one string
    print strjoin(parts, " - ");

This prints:

::

    Hello GAUSS
             one              two            three
    one - two - three

Example: Case conversion
+++++++++++++++++++++++++++++++++

::

    s = "Hello World";
    print upper(s);
    print lower(s);

This prints:

::

    HELLO WORLD
    hello world


Converting Between Strings and Numbers
--------------------------------------------

GAUSS provides functions to convert between numeric values and their
string representations.

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Function
      - Description

    * - :func:`ntos`
      - Number to string: ``ntos(x)`` or ``ntos(x, prec)`` where *prec*
        is the number of significant digits (default 6)

    * - :func:`strtof`
      - String or string array to numeric value(s)

    * - :func:`stof`
      - Single string to number

    * - :func:`ftocv`
      - Matrix to character vector (legacy, for formatted display)

    * - :func:`ftostrC`
      - Matrix to string array using C format specifiers

Example: Numeric to string
+++++++++++++++++++++++++++++++++

::

    x = 3.14159;

    // Default: 6 significant digits
    print ntos(x);

    // Specify number of significant digits
    print ntos(x, 2);

This prints:

::

    3.14159
    3.1

Example: String to numeric
+++++++++++++++++++++++++++++++++

::

    // String array to numeric matrix
    sa = "1.5" $| "2.7" $| "3.9";
    y = strtof(sa);
    print y;

This prints:

::

       1.5000000
       2.7000000
       3.9000000


Data Types: String vs. String Array vs. Character Matrix
-------------------------------------------------------------

GAUSS has three text-related types. Understanding the differences helps
you choose the right one:

.. list-table::
    :widths: 20 20 60
    :header-rows: 1

    * - Type
      - ``type()``
      - Description

    * - Matrix
      - 6
      - An NxK numeric matrix (scalars, vectors, and matrices).

    * - String
      - 13
      - A single text value of any length.

    * - String array
      - 15
      - An NxK matrix of strings. Each element can be any length.

    * - Character matrix
      - 6
      - A numeric matrix where each element stores up to 8 characters.
        Reports the same ``type()`` value as a regular matrix.
        Legacy type — prefer string arrays for new code.

.. warning::

    **Character matrices** are a legacy feature. Each element is stored
    in 8 bytes (the size of a double-precision number), so each element
    is limited to 8 characters. String arrays have no such limit and
    should be used for all new code.

You can check a variable's type with the :func:`type` function:

::

    x = 42;
    s = "hello";
    sa = "a" $~ "b";

    print "matrix type:" type(x);
    print "string type:" type(s);
    print "string array type:" type(sa);

This prints:

::

    matrix type:       6.0000000
    string type:       13.000000
    string array type:       15.000000


Quick Reference
--------------------------------------------

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Task
      - How

    * - Create a string
      - ``s = "text";``

    * - Concatenate strings
      - ``s = a $+ b;``

    * - Build a string array (row)
      - ``sa = "a" $~ "b" $~ "c";``

    * - Build a string array (column)
      - ``sa = "a" $| "b" $| "c";``

    * - Index a string array
      - ``sa[2, 3]`` or ``sv[i]``

    * - String length
      - :func:`strlen`

    * - Substring extraction
      - :func:`strsect`

    * - Find substring
      - :func:`strindx`

    * - Replace substring
      - :func:`strreplace`

    * - Split by delimiter
      - :func:`strsplit`

    * - Join with separator
      - :func:`strjoin`

    * - Number to string
      - :func:`ntos`

    * - String to number
      - :func:`strtof`

    * - Compare strings
      - ``$==``, ``$/=``, ``$<``, ``$>``, ``$<=``, ``$>=``

    * - Format a string
      - :func:`sprintf`


.. seealso:: :ref:`operators`, :ref:`control-flow`, :doc:`/user-guide/formula-strings`, :func:`strcombine`, :func:`strtrim`
