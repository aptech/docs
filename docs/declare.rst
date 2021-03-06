
declare
==============================================

Purpose
----------------

Initializes global variables at compile time.

Format
----------------
.. function:: declare [[type]] symbol [[aop clist]]

    :param type: optional. specifying the type of the symbol.
    :type type: literal

        - matrix
        - string
        - array
        - sparse matrix
        - struct structure_type.

        if *type* is not specified, matrix is assumed. Set *type* to string to initialize a string or string array variable.

    :param symbol: the name of the symbol being declared
    :type symbol:

    :param aop: the type of assignment to be made. If *aop* is specified, *clist* must be also.

        .. csv-table::
            :widths: auto

            "``=``", "if not initialized, initialize. If already initialized, reinitialize."
            "``!=``", "if not initialized, initialize. If already initialized, reinitialize."
            "``:=``", "if not initialized, initialize. If already initialized, redefinition error."
            "``?=``", "if not initialized, initialize. If already initialized, leave as is."

    :type aop: literal

    :param clist: a list of constants to assign to *symbol*
        If *aop* *clist* is not specified, *symbol* is initialized as a scalar 0 or a null string.
    :type clist: varies

Examples
----------------

::

    declare matrix x,y,z;

After this code:

::

    x = 0   y = 0   z = 0

Now declare a string:

::

    declare string x = "This string.";

After this code:

::

    x = "This string."

In this example we reinitialize the matrix *x* and set *x* to specified values:

::

    /*
    ** Re-initialize 'x' with the specified values and
    ** return a warning if 'x' already exists AND
    ** the 'Compile Options: declare warnings' is
    ** selected
    */
    declare matrix x != { 1 2 3, 4 5 6, 7 8 9 };

After this the *x* matrix is no longer zero and is filled with the specified values:

::

        1 2 3
    x = 4 5 6
        7 8 9

Alternatively declare the *x* matrix dimensions and fill with values:

::

    declare matrix x[3,3] = 1 2 3 4 5 6 7 8 9;

This yields the same results as the previous case:

::

        1 2 3
    x = 4 5 6
        7 8 9

Now, fill a matrix of specific dimensions with a single value:

::

    declare matrix x[3,3] = 1;

::

        1 1 1
    x = 1 1 1
        1 1 1

If there is no value specified the matrix is filled with zeroes:

::

    declare matrix x[3,3];

::

        0 0 0
    x = 0 0 0
        0 0 0

The previous examples have been numeric matrices. This case will create a character matrix:

::

    // Create a 2x1 character matrix
    declare matrix x = alpha beta;

    /*
    ** To print character matrices, the '$' operator must
    ** be prepended to the variable name
    */
    print $x;

The code snippet directly above, produces:

::

    ALPHA
     BETA

Even if we include ``"`` when declaring the values in a matrix, it will create a character matrix:

::

    /*
    ** Since this is declared as a matrix, the text in
    ** quotes will create a character vector, rather
    ** than a string array
    */
    declare matrix x = "mean" "variance";

    print $x;

produces:

::

    mean variance


Structures can hold various members including scalars, arrays, matrices, strings, and string arrays, and other structures. The structure must first be defined before being declared:

::

    struct mystruct {
      matrix m;
      string s;
      string array sa;
      array a;
      sparse matrix sm;
     };

    declare struct mystruct ms;

*ms* is a :code:`mystruct` structure, with its members set as follows:

.. list-table::
    :widths: auto

    * - *ms.m*
      - empty matrix
    * - *ms.s*
      - null string
    * - *ms.sa*
      - 1x1 string array containing a null string
    * - *ms.a*
      - 1-dimensional array of length 1 containing 0
    * - *ms.sm*
      - empty sparse matrix

Remarks
-------

The `declare` syntax is similar to the `let` statement.

`declare` generates no executable code. This is strictly for compile time
initialization. The data on the right-hand side of the equal sign must
be constants. No expressions or variables are allowed.

`declare` statements are intended for initialization of global variables
that are used by procedures in a library system.

It is best to place `declare` statements in a separate file from procedure
definitions. This will prevent redefinition errors when rerunning the
same program without clearing your workspace.

The optional *aop* and *clist* arguments are allowed only for declaring
matrices, strings, and string arrays. When you declare an N-dimensional
array, sparse matrix, or structure, they will be initialized as follows:


====================  =====================================================
Variable Type          Initializes to
====================  =====================================================
N-dimensional array   1-dimensional array of size 1 containing 0
sparse matrix         empty sparse matrix
structure             structure containing empty and/or zeroed out members.
====================  =====================================================

Complex numbers can be entered by joining the real and imaginary parts
with a sign (+ or -); there should be no spaces between the numbers and
the sign. Numbers with no real part can be entered by appending an 'i'
to the number.

There should be only one declaration for any symbol in a program.
Multiple declarations of the same symbol should be considered a
programming error. When GAUSS is looking through the library to
reconcile a reference to a matrix or a string, it will quit looking as
soon as a symbol with the correct name is found. If another symbol with
the same name existed in another file, it would never be found. Only the
first one in the search path would be available to programs.

Here are some of the possible uses of the three forms of declaration:

.. list-table::
    :widths: auto

    * - ``!=``, ``=``
      - Interactive programming or any situation where a global by the same name
        will probably be sitting in the symbol table when the file containing
        the `declare` statement is compiled. The symbol will be reset.

        This allows mixing `declare` statements with the procedure definitions
        that reference the global matrices and strings or placing them in your
        main file.

    * - ``:=``
      - Redefinition is treated as an error because you have probably just
        outsmarted yourself. This will keep you out of trouble because it won't
        allow you to zap one symbol with another value that you didn't know was
        getting mixed up in your program. You probably need to rename one of
        them.

        You need to place `declare` statements in a separate file from the rest of
        your program and procedure definitions.

    * - ``?=``
      - Interactive programming where some global defaults were set when you
        started and you don't want them reset for each successive run even if
        the file containing the `declare`'s gets recompiled. This can get you into
        trouble if you are not careful.

The `declare` statement warning level is a compile option. Call :func:`config` in
the command line version of GAUSS or select :menuselection:`Tools --> Preferences --> Advanced` 
in the **User Interface** to edit this option. If ``declare warnings`` are on, you will be warned 
whenever a `declare` statement encounters a symbol that is already initialized. Here's what happens
when you `declare` a symbol that is already initialized when ``declare warnings`` are turned on:


.. list-table::
    :widths: auto

    * - :code:`declare !=`
      - Reinitialize and warn.
    * - :code:`declare :=`
      - End program with fatal error
    * - :code:`declare ?=`
      - Leave as is and warn.

If `declare warnings` are off, no warnings are given for the ``!=`` and ``?=`` cases.

.. seealso:: Functions `let`, `external`
