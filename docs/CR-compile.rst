
compile
==============================================

Purpose
----------------

Compiles a source file to a compiled code file. See also `the Compiler chapter. <COM-Compiler.html>`_ 

.. _compile:
.. index:: copmile

Format
----------------

::

    compile source [fname]

**Parameters**

    :source: (*literal or ^string*) the name of the file to be compiled.
    
    
    :fname: (*literal or ^string*) optional, the name of the file to be created. If not given, the 
        file will have the same filename and path as source. It will have a :file:`.gcg` extension.

Examples
----------------

::

    compile qxy.e;

In this example, the `source path` would be searched for qxy.e, which
would be compiled to a file called :file:`qxy.gcg` on the same subdirectory *qxy.e* was found.

::

    compile qxy.e xy;

In this example, the `source path` would be searched for *qxy.e* which
would be compiled to a file called :file:`xy.gcg` on the current subdirectory.

Remarks
-------

-  The source file will be searched for in the `source path` if the full path
   is not specified and it is not present in the current directory.

-  The source file is a regular text file containing a GAUSS program.
   There can be references to global symbols, **Run-Time Library**
   references, etc.

-  If there are `library` statements in source, they will be used during
   the compilation to locate various procedures and symbols used in the
   program. Since all of these library references are resolved at
   compile time, the library statements are not transferred to the
   compiled file. The compiled file can be run without activating any
   libraries.

-  If you do not want extraneous stuff saved in the compiled image, put
   a `new` at the top of the source file or execute a `new` in interactive
   mode before compiling.

-  The program saved in the compiled file can be run with the `run`
   command. If no extension is given, the `run` command will look for a
   file with the correct extension for the version of GAUSS. The
   `source path` will be used to locate the file if the full path name is not
   given and it is not located on the current directory.

-  When the compiled file is run, all previous symbols and procedures
   are deleted before the program is loaded. It is therefore unnecessary
   to execute a `new` before running a compiled file.

-  If you want line number records in the compiled file you can put a
   `#lineson` statement in the source file or turn line tracking on from
   the main GAUSS menu, :menuselection:`Tools --> Preferences --> Advanced`.

-  Don't try to include compiled files with `#include`.

-  GAUSS compiled files are platform and bit-size specific. For example,
   a file compiled with GAUSS for Windows 64-bit will not run under
   GAUSS for Windows 32-bit or on Linux 64-bit

.. seealso:: Functions `run`, `use`, `saveall`

