.. _compilation-libraries:

Compilation and Libraries
===============================================

As your GAUSS projects grow beyond a single script, you need ways to
organize code into reusable pieces and share procedures across programs.
GAUSS provides three mechanisms for this:

- **#include** — insert a source file directly into your program
- **Libraries** — index files (``.lcg``) that tell GAUSS where to find
  procedures and globals
- **Compilation** — compile source to binary (``.gcg``) for faster
  loading and code protection

This page explains each mechanism and when to use it.

.. note::

    If you are coming from Python or C:

    - ``#include`` works like C's ``#include`` — text substitution at
      compile time.
    - A GAUSS **library** (``.lcg``) is an index file that maps symbol
      names to source files — similar in spirit to a Python package's
      ``__init__.py``, but it is a passive lookup table, not executable
      code.
    - A ``.gcg`` compiled file is like Python's ``.pyc`` bytecode —
      faster to load, not human-readable, and platform-specific.


``#include`` — Including Source Files
--------------------------------------------

The ``#include`` directive inserts the contents of another source file
directly into your program at compile time, as if you had typed the code
inline:

::

    #include myutils.src

    y = addtwo(5);
    print y;

If ``myutils.src`` defines the procedure ``addtwo``, it is available
immediately — no library setup required.

How ``#include`` searches for files
++++++++++++++++++++++++++++++++++++

GAUSS searches for the included file in this order:

1. The current working directory
2. Each directory listed in the ``src_path`` configuration variable

.. tip::

    Use ``#include`` for small utility files or shared definitions.
    For larger projects with many procedures, libraries provide a more
    scalable approach.

Rules for ``#include``
++++++++++++++++++++++++++++++++++++

- The filename follows ``#include`` on the same line with **no quotes
  and no semicolon**.
- ``#include`` directives are resolved at compile time. They can appear
  anywhere in a source file.
- Do not ``#include`` compiled (``.gcg``) files — include only source
  files.
- Nested includes are allowed: an included file can ``#include`` other
  files.


Libraries
--------------------------------------------

A **library** in GAUSS is a text file with the extension ``.lcg``
(Library Catalog) that maps source file names to the symbols they
contain. Libraries let GAUSS find and load procedures **on demand**,
without requiring you to ``#include`` every source file.

The ``library`` command
++++++++++++++++++++++++++++++++++++

The ``library`` command tells GAUSS which libraries to make available:

::

    // Load the TSMT time series library
    library tsmt;

    // Load multiple libraries
    library tsmt, pgraph;

Two libraries are always active:

- **user.lcg** — loaded first (your personal library, if it exists)
- **gauss.lcg** — loaded last (the built-in GAUSS library)

When you issue a ``library`` command, the specified libraries are
inserted between ``user.lcg`` and ``gauss.lcg`` in the search order.
Any previously loaded user-specified libraries are unloaded.

.. note::

    ``library`` does not load any code into memory. It only tells the
    autoloader where to *search* when it encounters an undefined symbol.

Library file format (``.lcg``)
++++++++++++++++++++++++++++++++++++

A ``.lcg`` file is plain text. Each source filename appears flush left,
followed by indented lines listing the symbols it contains:

::

    /*
    ** myproject.lcg — Library catalog for my project
    */

    mathutils.src
        onenorm         : proc : 1
        infnorm         : proc : 5
        euclidnorm      : proc : 9

    globals.dec
        _my_tolerance   : matrix : 1
        _my_verbose     : matrix : 2

Each indented line has the format::

    symbol_name    : type : line_number

The *line_number* field tells the autoloader which line of the source
file defines the symbol. It is optional but improves loading speed.
The *type* is one of:

.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - Type
      - Description

    * - ``proc``
      - Procedure

    * - ``fn``
      - Single-line function (``fn`` statement)

    * - ``keyword``
      - Keyword procedure

    * - ``matrix``
      - Matrix or scalar global variable

    * - ``string``
      - String global variable

    * - ``array``
      - N-dimensional array global variable

    * - ``sparse matrix``
      - Sparse matrix global variable

    * - ``struct TypeName``
      - Structure instance (e.g., ``struct DS``). Used for global
        structure variables in source files.

    * - ``definition``
      - Structure type definition (in ``.sdf`` files)

Comments in ``.lcg`` files recognize lines beginning with ``/*``,
``**``, or ``*/`` as comments. Single-line ``//`` comments are not
supported in library files.

Where library files are stored
++++++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Library
      - Location

    * - ``gauss.lcg``
      - ``GAUSSHOME/lib/``

    * - ``user.lcg``
      - ``GAUSSHOME/lib/`` (created by user if needed)

    * - Add-on libraries
      - ``GAUSSHOME/pkgs/<package>/lib/``

Library files must be located on the ``lib_path`` configuration
variable. Source files (``.src``, ``.dec``, ``.ext``, ``.sdf``)
referenced by the library must be on the ``src_path``. These are
separate configuration variables — placing a ``.lcg`` file on
``src_path`` will not make it discoverable as a library.


The Autoloader
--------------------------------------------

The **autoloader** is the mechanism that connects libraries to your
running code. When GAUSS encounters a symbol that has not been defined
yet, the autoloader searches for it and loads the containing source
file automatically.

How the autoloader resolves symbols
++++++++++++++++++++++++++++++++++++

When GAUSS encounters an undefined symbol on the **right-hand side** of
a statement (used as a value, function call, etc.), it searches in this
order:

1. **user.lcg** — your personal library catalog
2. **User-specified libraries** — libraries loaded via the ``library``
   command, in the order specified
3. **gauss.lcg** — the built-in GAUSS library catalog
4. **Loose ``.g`` files** — files matching ``symbol_name.g`` in the
   current directory, then in each ``src_path`` directory (only when
   ``autodelete`` is ON — see below)

When the autoloader finds the symbol in a ``.lcg`` file, it locates
the source file listed above the symbol and compiles it. All symbols
in that source file become available.

.. warning::

    If a symbol appears on the **left-hand side** of a statement
    (being assigned to) and has not been defined, GAUSS creates it as
    a new matrix variable — the autoloader is **not** invoked. This
    means accidentally assigning to a procedure name silently creates
    a variable instead of calling the procedure::

        // WRONG: creates a matrix, does not call onenorm
        onenorm = {1, 2, 3};

        // RIGHT: right-hand side triggers the autoloader
        result = onenorm({1, 2, 3});

Example: Autoloader in action
++++++++++++++++++++++++++++++++++++

Suppose ``mathutils.src`` contains:

::

    // mathutils.src
    proc (1) = onenorm(x);
        retp(sumc(abs(x)));
    endp;

    proc (1) = infnorm(x);
        retp(maxc(abs(x)));
    endp;

And ``myproject.lcg`` contains:

::

    mathutils.src
        onenorm         : proc : 1
        infnorm         : proc : 5

After running ``library myproject;``, you can call ``onenorm`` or
``infnorm`` directly. The autoloader finds the symbol in
``myproject.lcg``, compiles ``mathutils.src``, and makes both
procedures available.

The ``autodelete`` setting
++++++++++++++++++++++++++++++++++++

By default, ``autodelete`` is ON. This means:

- When the autoloader loads a source file, it marks the symbols for
  automatic deletion.
- If a later source file defines the same symbol, the old definition
  is automatically replaced.

With ``autodelete`` OFF, the autoloader is stricter:

- The ``.g`` file search (step 4 above) is disabled. Every symbol must
  be listed in an active library or declared with ``external``.
- Forward references to undefined symbols within the same file require
  ``external`` declarations.
- Redefining a symbol that was loaded by the autoloader produces an
  error, catching accidental name collisions.

::

    // Turn off automatic deletion of autoloaded symbols
    autodelete off;


Global Declaration Files
--------------------------------------------

Libraries often need global variables shared across procedures. GAUSS
uses two types of declaration files to manage this: ``.dec`` files
*define* the variable (one per library), and ``.ext`` files *reference*
it (included in every source file that uses the variable).

Declaration files (.dec)
++++++++++++++++++++++++++++++++++++

A ``.dec`` file contains ``declare`` statements that create global
variables with default values:

::

    // myproject.dec
    declare matrix _my_tolerance = 1e-8;
    declare matrix _my_verbose = 1;
    declare string _my_outfile = "results.txt";

``declare`` creates the variable **only if it does not already exist**.
If the variable is already in memory, ``declare`` is silently ignored.
This makes ``.dec`` files safe to include multiple times.

.. note::

    Legacy code uses ``!=`` instead of ``=`` in ``declare`` statements
    (e.g., ``declare matrix _tol != 1e-8;``). Both forms have the same
    behavior: initialize only if the variable does not already exist.

.. tip::

    By convention, global variables in libraries use an underscore
    prefix (``_my_tolerance``) to avoid name collisions with user
    variables.

External declaration files (.ext)
++++++++++++++++++++++++++++++++++++

An ``.ext`` file contains ``external`` statements that tell the
compiler a symbol is defined elsewhere:

::

    // myproject.ext
    external matrix _my_tolerance, _my_verbose;
    external string _my_outfile;
    external proc onenorm, infnorm;

``external`` does not create the variable or assign a value — it only
tells the compiler that the symbol exists so the program compiles
without errors.

Structure definition files (.sdf)
++++++++++++++++++++++++++++++++++++

Structure definitions are stored in ``.sdf`` (Structure Definition
File) files. These define the fields of a structure type:

::

    // myresult.sdf
    struct myResult {
        matrix coefficients;
        matrix stderr;
        scalar retcode;
        string method;
    };

Structure definition files are listed in library catalogs with the
type ``definition``.

Putting it all together
++++++++++++++++++++++++++++++++++++

A typical library project has this file structure::

    myproject/
        src/
            myproject.dec      Global variable defaults
            myproject.ext      External declarations
            myproject.sdf      Structure definitions
            mathutils.src      Procedure source code
            ioutils.src        More procedures
        lib/
            myproject.lcg      Library catalog

The ``.lcg`` file lists all the source, declaration, and definition
files:

::

    myproject.dec
        _my_tolerance       : matrix : 1
        _my_verbose         : matrix : 2

    myproject.sdf
        struct myResult            : definition : 1

    mathutils.src
        onenorm             : proc : 1
        infnorm             : proc : 5

    ioutils.src
        loadresults         : proc : 1
        saveresults         : proc : 12

Users activate the library with ``library myproject;`` and can then
call any of its procedures.


Compiling Programs
--------------------------------------------

The ``compile`` command converts a GAUSS source file (``.e``) into a
compiled binary file (``.gcg``):

::

    compile myprogram.e;

This creates ``myprogram.gcg``. You can also specify an output name:

::

    compile myprogram.e myoutput;

This creates ``myoutput.gcg``. Run a compiled file with:

::

    run myprogram.gcg;

.. note::

    The ``run`` command assumes a ``.gcg`` extension if none is given.
    So ``run myprogram;`` is equivalent to ``run myprogram.gcg;``.

When to compile
++++++++++++++++++++++++++++++++++++

Compilation is useful when you want to:

- **Distribute code** without revealing source — compiled files are
  binary and cannot be easily read.
- **Speed up loading** — compiled files skip the parsing step.
- **Freeze a version** — the compiled file captures library
  dependencies at compile time.

Compilation rules
++++++++++++++++++++++++++++++++++++

- **Libraries must be present at compile time.** The compiler resolves
  ``library`` statements and autoloader references during compilation.
  The resulting ``.gcg`` file does **not** store library references —
  all needed code is compiled in.
- **Libraries are not needed at run time.** Since library code is
  compiled into the ``.gcg`` file, users can run the compiled program
  without having the original ``.lcg`` files or source.
- **DLLs/shared libraries must be present at run time.** If your
  program uses ``dlibrary`` to load external shared libraries, those
  files must be available when the compiled program runs.
- **Compiled files are platform-specific.** A ``.gcg`` file compiled
  on macOS will not run on Windows, and vice versa. 64-bit and 32-bit
  builds are also incompatible.

.. tip::

    Place ``new;`` at the top of your source file before compiling to
    ensure that no extraneous symbols from the current workspace are
    included in the compiled image.

Debug line numbers
++++++++++++++++++++++++++++++++++++

By default, compiled files do not include source line numbers in error
messages. To include line number information for debugging, add
``#lineson`` to your source file before compiling:

::

    #lineson

    x = rndn(3, 3);
    y = inv(x);
    print y;


File Type Reference
--------------------------------------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Extension
      - Description

    * - ``.e``
      - GAUSS program source file (main entry point)

    * - ``.src``
      - Procedure source file (contains ``proc``/``endp`` definitions)

    * - ``.g``
      - Single-procedure source file (autoloader convention: one
        procedure per file, filename matches procedure name)

    * - ``.dec``
      - Global declaration file (``declare`` statements)

    * - ``.ext``
      - External declaration file (``external`` statements)

    * - ``.sdf``
      - Structure definition file

    * - ``.lcg``
      - Library catalog file (maps source files to symbols)

    * - ``.gcg``
      - Compiled GAUSS binary (output of ``compile``)


Quick Reference
--------------------------------------------

.. list-table::
    :widths: 35 65
    :header-rows: 1

    * - Task
      - How

    * - Include a source file
      - ``#include myutils.src``

    * - Activate a library
      - ``library tsmt;``

    * - Activate multiple libraries
      - ``library tsmt, pgraph;``

    * - Compile a program
      - ``compile myprogram.e;``

    * - Run a compiled program
      - ``run myprogram.gcg;``

    * - Declare a global with default
      - ``declare matrix _tol = 1e-8;``

    * - Declare an external symbol
      - ``external proc myproc;``

    * - Disable autoload replacement
      - ``autodelete off;``

    * - Enable debug line numbers
      - ``#lineson`` (at top of source file)


.. seealso:: :doc:`/user-guide/fundamentals/procedures`, :doc:`/user-guide/advanced/structures`
