
library
==============================================

Purpose
----------------

Sets up the list of active libraries.

Format
----------------
.. function:: library lib1 [[,lib2,lib3,lib4...]] 
			  		library

Examples
----------------

If no arguments are given, the list of current libraries will be printed out. For example:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    library;

will produce output similar to:

::

    Library path: C:\gauss17\gaussplot\lib
                  C:\gauss17\lib
    
    Libraries:    C:\gauss17\lib\user.lcg
                  C:\gauss17\lib\gauss.lcg

Load multiple libraries by passing a comma-separated list of library names.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    library pgraph, cmlmt;

After executing the code above, entering the library command without any arguments will produce output similar to this:

::

    Library path: C:\gauss17\gaussplot\lib
                  C:\gauss17\lib
    
    Libraries:    C:\gauss17\lib\user.lcg
                  C:\gauss17\lib\pgraph.lcg
                  C:\gauss17\lib\cmlmt.lcg
                  C:\gauss17\lib\gauss.lcg

The output from the library command above is printed in the order in which GAUSS will search. For this particular example, GAUSS will first search the user library, then the pgraph library, followed by the cmlmt library and finally the gauss library.

Loading a library or list of libraries with the library command will also close any open libraries other than user and gauss which are always loaded.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Continuing with the last example in which the user, pgraph, cmlmt and gauss libraries were open, executing the command:

::

    library pgraph, tsmt;

would open tsmt, while closing pgraph and cmlmt.

Remarks
-------

For more information about the library system, see **Libraries**,
Chapter 1 .

The required extension for library files is .lcg.

**Library searching**
If a list of library names is given, they will be the new set of active
libraries. The two default libraries are user.lcg and gauss.lcg. Unless
otherwise specified, user.lcg will be searched first and gauss.lcg will
be searched last. Any other user-specified libraries will be searched
after user.lcg in the order they were entered in the library statement.

If the statement:

::

   y = myProc(x);

is encountered in a program, myProc will be searched for in the active
libraries. If it is found, it will be compiled. If it cannot be found in
a library, the deletion state determines how it is handled:

+-----------------+-----------------------------------------------------+
| autodelete on   | search for myproc.g                                 |
+-----------------+-----------------------------------------------------+
| autodelete off  | return Undefined symbol error message               |
+-----------------+-----------------------------------------------------+

If myProc calls myRegress and myRegress calls myUtil and they are all in
separate files, they will all be found by the autoloader.

The source browser and the help facility will search for myProc in
exactly the same sequence as the autoloader.

**Library file contents**
Library files are simple ASCII files that you can create with a text
editor. Here is an example:

::

   /*
   ** This is a GAUSS library file.
   */
    
   eig.src
       eig     : proc
       eigsym  : proc
       _eigerr : matrix
   svd.src
       cond    : proc
       pinv    : proc
       rank    : proc
       svd     : proc
       _svdtol : matrix

The lines not indented are the file names. The lines that are indented
are the symbols defined in that file. As you can see, a GAUSS library is
a dictionary of files and the global symbols they contain.

Any line beginning with /*, \**, or \*/ is considered a comment.
Currently, // comments are not supported in library files. Blank lines
are okay.

To make the autoloading process more efficient, you can put the full
pathname for each file in the library:

::

   /gauss/src/eig.src
       eig      : proc
       eigsym   : proc
       _eigerr  : matrix
   /gauss/src/svd.src
       cond     : proc
       pinv     : proc
       rank     : proc
       svd      : proc
       _svdtol  : matrix

Here's a debugging hint. If your program is acting strange and you
suspect it is autoloading the wrong copy of a procedure, use the Library
Tool on the Edit Page, or the CTRL+F1 hotkey to locate the suspected
function. It will use the same search path that the autoloader uses.

.. seealso:: Functions `declare`, `external`, `lib`, `proc`
