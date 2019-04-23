
makevars
==============================================

Purpose
----------------

Creates separate global vectors from the columns of a matrix.

Format
----------------
.. function:: makevars(x, vnames, xnames)

    :param x: columns to be converted into individual vectors
    :type x: NxK matrix

    :param vnames: names of global vectors to create. If 0, all names in *xnames* will be used.
    :type vnames: string or Mx1 character vector

    :param xnames: names to be associated with the columns of the matrix *x*
    :type xnames: string or Kx1 character vector

Remarks
-------

If *xnames* = 0, the prefix ``X`` will be used to create names. Therefore, if
there are 9 columns in *x*, the names will be ``X1-X9``, if there are 10, they
will be ``X01-X10``, and so on.

If *xnames* or *vnames* is a string, the individual names must be separated
by spaces or commas:

::

   vnames = "age pay sex";

Since these new vectors are created at execution time, the compiler will
not know they exist until after :func:`makevars` has executed once. This means
that you cannot access them by name unless you previously clear them or
otherwise add them to the symbol table. (See :func:`setvars` for a quick
interactive solution to this.)

This function is the opposite of :func:`mergevar`.


Examples
----------------

::

    let x[3,3] = 101 35 50000
                 102 29 13000
                 103 37 18000;
    let xnames = id age pay;
    let vnames = age pay;
    makevars(x,vnames,xnames);

Two global vectors, called *age* and *pay*, are created from the
columns of *x*.

::

    let x[3,3] = 101 35 50000
                 102 29 13000
                 103 37 18000;
    xnames = "id age pay";
    vnames = "age pay";
    makevars(x,vnames,xnames);

This is the same as the example above, except that strings are used
for the variable names.

Globals
------------

\__vpad

Source
------

vars.src

.. seealso:: Functions :func:`mergevar`, :func:`setvars`

