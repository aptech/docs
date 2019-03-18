
dataloop (dataloop)
==============================================

Purpose
----------------
Specifies the beginning of a data loop.

Format
----------------
.. function:: dataloop infile outfile

    :param infile: the name of the source data set.
    :type infile: string variable or literal

    :returns: outfile (*string variable or literal*), the name of the output data set.

Examples
----------------

::

    src = "source";
    dataloop ^src dest;
    make newvar = x1 + x2 + log(x3);
    x6 = sqrt(x4);
    keep x6, x5, newvar;
    endata;

Here, src is a string variable requiring the caret (^) operator,
while dest is a string literal.

