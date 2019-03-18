
dlibrary
==============================================

Purpose
----------------

Dynamically links and unlinks shared libraries.

Format
----------------
.. function:: dlibrary lib1 [[lib2]]... 
			  dlibrary -a lib1 [[lib2]]...  
			  dlibrary -d 
			  dlibrary

    :param lib1 lib2...: the base name of the library or the pathed name of the library.
        dlibrary takes two types of arguments, ''base'' names and
        file names. Arguments without any "/" path separators are assumed to be library base names, and are expanded by adding
        the suffix .so, .dll or .dylib, depending on the platform. They are searched
        for in the default dynamic library directory. Arguments that include "/" path separators
        are assumed to be file names, and are not expanded. Relatively pathed file names are assumed to be specified relative to the
        current working directory, not relative to the dynamic library directory.
    :type lib1 lib2...: literal

    :param -a: the shared libraries listed are added to the current set of shared libraries rather than replacing them. For search purposes,
        the new shared libraries follow the already active ones. Without the -a flag, any previously linked libraries are dumped.
    :type -a: append flag

    :param -d: ALL shared libraries are unlinked and the functions they contain are no longer available
        to your programs. If you use dllcall to call one of your functions after executing a
        dlibrary -dyour program will terminate with an error.
    :type -d: dump flag

Examples
----------------

Loading a shared library and unloading previously loaded shared libraries
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    dlibrary mylib;

The above command passes the base name of the shared library to load. GAUSS will expand this base name to a platform specific shared library name. The expanded name on Windows is mylib.dll. On Linux it is libmylib.so and on Mac, libmylib.dylib. Since we did not pass the -a flag, GAUSS, will unload any shared libraries that were previously loaded with the dlibrary command.

Loading a shared library and keeping previously loaded shared libraries
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    dlibrary -a mylib;

Since we passed the  -a flag, GAUSS will not unload any libraries when it loads mylib.

.. seealso:: Functions :func:`dllcall`, :func:`sysstate`
