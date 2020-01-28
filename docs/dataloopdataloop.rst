
dataloop (dataloop)
==============================================

Purpose
----------------
Specifies the beginning of a data loop.

Format
----------------
.. function:: dataloop infile outfile

    :param infile: the name of the source dataset.
    :type infile: string variable or literal

    :return outfile: the name of the output dataset.

    :rtype outfile: string variable or literal

Examples
----------------

::

    src = "source";

    // Dataloop section
    dataloop ^src dest;
      make newvar = x1 + x2 + log(x3);
      x6 = sqrt(x4);
      keep x6, x5, newvar;
    endata;

Here, ``src`` is a string variable requiring the caret (``^``) operator,
while ``dest`` is a string literal.

Remarks
-------

The statements between the ``dataloop... endata`` commands are assumed to be
metacode to be translated at compile time. The data from *infile* is
manipulated by the specified statements, and stored to the dataset
*outfile*. Case is not significant within the ``dataloop... endata`` section,
except for within quoted strings. Comments can be used as in any GAUSS code.


