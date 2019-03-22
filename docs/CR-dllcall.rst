
dllcall
==============================================

Purpose
----------------

Calls functions located in dynamic libraries.

Format
----------------
.. function:: dllcall [-r] [-v] func(arg1...argN) 

    :param func: the name of a function contained in a shared library (linked into GAUSS with dlibrary). If *func* is not specified or cannot be located in a shared library, :func:`dllcall` will fail.

    :param arg#: optional. arguments to be passed to *func*. These must be simple variable references; they cannot be expressions.

    :param -r: optional flag. If ``-r`` is specified, :func:`dllcall` examines the value returned by
        *func*, and fails if it is nonzero.

    :param -v: optional flag. Normally, :func:`dllcall` passes parameters to *func* in a list. If
        -v is specified, :func:`dllcall` passes them in a vector. See below for more details.


Remarks
-------

:func:`dllcall` works in conjunction with :func:`dlibrary`.  
:func:`dlibrary` is used to link shared libraries into GAUSS  
:func:`dllcall` is used to access the functions contained in those shared libraries. :func:`dllcall` searches the shared libraries  
(see :func:`dlibrary` for an explanation of the search order) for a function named func, and calls the first instance it finds.  
The default shared libraries are searched last.

*func* should be written to:

+----+--------------------------------------------------+
| 1. | Take 0 or more pointers to doubles as arguments. |
+----+--------------------------------------------------+
| 2. | Take arguments either in a list or a vector.     |
+----+--------------------------------------------------+
| 3. | Return an integer.                               |
+----+--------------------------------------------------+

In C syntax, *func* should take one of the following forms:

.. csv-table::
    :widths: auto

    "1.",":code:`intfunc(void);`"
    "2.",":code:`intfunc(double \*arg1 [, arg2...argN]);`"
    "3.",":code:`intfunc(double \*arg[]);`"

:func:`dllcall` can pass a list of up to 100 arguments to *func*; if it requires
more arguments than that, you MUST write it to take a vector of
arguments, and you MUST specify the ``-v`` flag when calling it. :func:`dllcall` can
pass up to 1000 arguments in vector format. In addition, in vector
format :func:`dllcall` appends a null pointer to the vector, so you can write
*func* to take a variable number of arguments and just test for the null
pointer.

Arguments are passed to *func* by reference. This means you can send back
more than just the return value, which is usually just a success/failure
code. (It also means that you need to be careful not to overwrite the
contents of matrices or strings you want to preserve.) To return data
from *func*, simply set up one or more of its arguments as return matrices
(basically, by making them the size of what you intend to return), and
inside *func* assign the results to them before returning.

For more information, see **Foreign Language Interface**, Chapter 1.

.. seealso:: :func:`dlibrary`, :func:`sysstate`

