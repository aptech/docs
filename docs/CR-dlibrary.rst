
dlibrary
==============================================

Purpose
----------------

Dynamically links and unlinks shared libraries.

Format
----------------
.. function:: dlibrary [-a] [-d] [lib1 [lib2]]...

    :param lib1: the base name of the library or the pathed name of the library.
        `dlibrary` takes two types of arguments, ''base'' names and
        file names. 

        * Arguments without any "``/``" path separators are assumed to be library base names, and are expanded by adding
          the suffix :file:`.so`, :file:`.dll` or :file:`.dylib`, depending on the platform. They are searched
          for in the default dynamic library directory. 
        
        * Arguments that include "``/``" path separators
          are assumed to be file names, and are not expanded. Relatively pathed file names are assumed to be specified relative to the
          current working directory, not relative to the dynamic library directory.
    :type lib1: literal

    :param -a: append flag. the shared libraries listed are added to the current set of shared libraries rather than replacing them. For search purposes,
        the new shared libraries follow the already active ones. Without the ``-a`` flag, any previously linked libraries are dumped.

    :param -d: dump flag. ALL shared libraries are unlinked and the functions they contain are no longer available
        to your programs. If you use :func:`dllcall` to call one of your functions after executing a
        :code:`dlibrary -d` your program will terminate with an error.

Remarks
-------

-  If no flags are used, the shared libraries listed are linked into
   GAUSS and any previously linked libraries are dumped. When you call
   :func:`dllcall`, the shared libraries will be searched in the order listed
   for the specified function. The first instance of the function found
   will be called.

-  `dlibrary` with no arguments prints out a list of the currently linked
   shared libraries. The order in which they are listed is the order in
   which they are searched for functions.

-  `dlibrary` recognizes a default directory in which to look for dynamic
   libraries. You can specify this by setting the variable *dlib_path* in
   :file:`gauss.cfg`. Set it to point to a single directory, not a sequence of
   directories. `sysstate`, `case 24`, may also be used to get and set this
   default.

-  GAUSS maintains its own shared libraries which are listed when you
   execute `dlibrary` with no arguments, and searched when you call
   `dllcall`. The default shared library or libraries are searched last.
   You can force them to be searched earlier by listing them explicitly
   in a `dlibrary` statement. They are always active and are not unlinked
   when you execute

   ::

      dlibrary -d

For more information, see **Foreign Language Interface**, Chapter 1.


Examples
----------------

Loading a shared library and unloading previously loaded shared libraries
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    dlibrary mylib;

The above command passes the base name of the shared library to load. GAUSS will expand this base name to a platform specific shared library name. The expanded name on Windows is :file:`mylib.dll`. On Linux it is :file:`libmylib.so` and on Mac, :file:`libmylib.dylib`. Since we did not pass the ``-a`` flag, GAUSS, will unload any shared libraries that were previously loaded with the `dlibrary` command.

Loading a shared library and keeping previously loaded shared libraries
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    dlibrary -a mylib;

Since we passed the ``-a`` flag, GAUSS will not unload any libraries when it loads ``mylib``.

.. seealso:: Functions :func:`dllcall`, :func:`sysstate`
