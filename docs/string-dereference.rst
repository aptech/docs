
string-dereference
==============================================

Purpose
----------------

Substitutes the value of a string variable into commands that expect literal strings.

Format
----------------

::

    command ^varname

Parameters
----------------

    :param varname: A string variable containing the value to substitute.
    :type varname: string

Examples
----------------

Output Command
++++++++++++++

Many GAUSS commands accept literal string arguments without quotes:

::

    // Direct literal string
    output file=/Users/jason/gauss26/foo.txt on;

To use a variable instead, use the ``^`` dereference operator:

::

    fname = "/Users/jason/gauss26/foo.txt";
    output file=^fname on;

Load Command
++++++++++++

::

    // Literal filename
    load x = mydata.fmt;

    // Using a variable
    datafile = "mydata.fmt";
    load x = ^datafile;

Open Command
++++++++++++

::

    filepath = "/data/myfile.dat";
    open fp = ^filepath for read;

Multiple Substitutions
++++++++++++++++++++++

::

    dirname = "/Users/jason/data/";
    filename = "results.csv";
    fullpath = dirname $+ filename;

    output file=^fullpath on;
    print "Results written";
    output off;

Remarks
-------

- The ``^`` operator is used with commands that traditionally expect literal (unquoted) string arguments.
- It allows dynamic file paths and names to be constructed at runtime.
- The variable must contain a string value.
- Common commands that support ``^`` include: ``output``, ``load``, ``save``, ``open``, ``run``, ``#include``.

.. note::

    The ``^`` character has different meanings in different contexts:

    - **String dereference** (this page): ``^varname`` substitutes a variable's value in literal string contexts
    - **Element-by-element power**: ``.^`` raises each element to a power (e.g., ``x .^ 2``)

    GAUSS uses ``.^`` for exponentiation, not ``^`` alone. The standalone ``^`` is reserved for string dereference.

.. seealso:: Commands ``output``, ``load``, ``save``, ``open``, Operators :doc:`element-by-element-power`
