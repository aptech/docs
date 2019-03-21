
dllcall
==============================================

Purpose
----------------

Calls functions located in dynamic libraries.

Format
----------------
.. function:: dllcall [-r] [-v] func(arg1...argN) 
			  dllcall works in conjunction with  dlibrary.  
			  dlibrary is used to link shared libraries into GAUSS  
			  dllcall is used to access the functions contained in those shared libraries. dllcall searches the shared libraries  
			  (see dlibrary for an explanation of the search order) for a function named func, and calls the first instance it finds.  
			  The default shared libraries are searched last.

    :param func:  If  func is not
        specified or cannot be located in a shared library, dllcall will fail.
    :type func: the name of a function contained in a shared library (linked into GAUSS with dlibrary)

    :param arg#: optional. These must be simple variable references; they cannot be expressions.
    :type arg#: arguments to be passed to  func

    :param -r: optional flag. If -r is specified, dllcall examines the value returned by
        func, and fails if it is nonzero.
    :type -r: TODO

    :param -v: optional flag. Normally, dllcall passes parameters to func in a list. If
        -v is specified, dllcall passes them in a vector. See below for more details.
    :type -v: TODO



Remarks
-------

func should be written to:

+----+--------------------------------------------------+
| 1. | Take 0 or more pointers to doubles as arguments. |
+----+--------------------------------------------------+
| 2. | Take arguments either in a list or a vector.     |
+----+--------------------------------------------------+
| 3. | Return an integer.                               |
+----+--------------------------------------------------+

In C syntax, func should take one of the following forms:

+----+-----------------------------------------+
| 1. | intfunc(void);                          |
+----+-----------------------------------------+
| 2. | intfunc(double \*arg1 [, arg2...argN]); |
+----+-----------------------------------------+
| 3. | intfunc(double \*arg[]);                |
+----+-----------------------------------------+

dllcall can pass a list of up to 100 arguments to func; if it requires
more arguments than that, you MUST write it to take a vector of
arguments, and you MUST specify the -v flag when calling it. dllcall can
pass up to 1000 arguments in vector format. In addition, in vector
format dllcall appends a null pointer to the vector, so you can write
func to take a variable number of arguments and just test for the null
pointer.

Arguments are passed to func by reference. This means you can send back
more than just the return value, which is usually just a success/failure
code. (It also means that you need to be careful not to overwrite the
contents of matrices or strings you want to preserve.) To return data
from func, simply set up one or more of its arguments as return matrices
(basically, by making them the size of what you intend to return), and
inside func assign the results to them before returning.

For more information, see **Foreign Language Interface**, Chapter 1.

