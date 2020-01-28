
maxvec
==============================================

Purpose
----------------

Returns maximum vector length allowed.

Format
----------------
.. function:: y = maxvec()

    :return y: maximum vector length.

    :rtype y: scalar

Global Input
------------

:__maxvec: (*scalar*) maximum vector length allowed.

Examples
----------------

::

    y = maxvec;
    print y;

    20000.000

Remarks
-------

:func:`maxvec` returns the value in the global scalar *__maxvec*, which can be
reset in the calling program.

:func:`maxvec` is called by `Run-Time Library` functions and applications when
determining how many rows can be read from a dataset in one call to
readr.

Using a value that is too large can cause excessive disk thrashing. The
trick is to allow the algorithm making the disk reads to execute
entirely in RAM.


Source
------

system.src

