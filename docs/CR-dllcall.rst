
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

