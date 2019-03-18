
declare
==============================================

Purpose
----------------

Initializes global variables at compile time.

Format
----------------
.. function:: declare [[type]] symbol [[aop clist]]

    :param type: specifying the type of the symbol.
    :type type: optional literal

    .. csv-table::
        :widths: auto

        "matrix"
        "string"
        "array"
        "sparse matrix"
        "struct structure_typeif  type is not specified, matrix is assumed. Set  type to string to initialize a string or string array variable."

    :param symbol: the name of the symbol being declared.
    :type symbol: TODO

    :param aop: the type of assignment to be made.
    :type aop: TODO

    .. csv-table::
        :widths: auto

        "=", "if not initialized, initialize.If already initialized, reinitialize."
        "!=", "if not initialized, initialize.If already initialized, reinitialize."
        ":=", "if not initialized, initialize.If already initialized, redefinition error."
        "?=", "if not initialized, initialize.If already initialized, leave as is."
        "If  aop is specified,  clist must be also."

    :param clist: a list of constants to assign to  symbol.
        
        If  aop clist is not specified,  symbol is initialized as a scalar 0
        or a null string.
    :type clist: TODO

Examples
----------------

::

    declare matrix x,y,z;
    
    x = 0   y = 0   z = 0
    declare string x = "This string.";
    
    x = "This string."
    
    declare matrix x;
    
    x = 0
    
    //Initialize 'x' with the specified values and 
    //return a warning if 'x'already exists AND 
    //the 'Compile Options: declare warnings' is 
    //selected
    declare matrix x != { 1 2 3, 4 5 6, 7 8 9 };
    
        1 2 3
    x = 4 5 6
        7 8 9
    
    declare matrix x[3,3] = 1 2 3 4 5 6 7 8 9;
    
        1 2 3
    x = 4 5 6
        7 8 9
    
    declare matrix x[3,3] = 1;
    
        1 1 1
    x = 1 1 1
        1 1 1
    
    declare matrix x[3,3];
    
        0 0 0
    x = 0 0 0
        0 0 0
    
    declare matrix x = 1 2 3 4 5 6 7 8 9;
    
        1
        2
        3
    x = 4
        5
        6
        7
        8
        9
    
    //Create a 2x1 character matrix
    declare matrix x = alpha beta;
    
    //To print character matrices, the '$' operator must
    //be prepended to the variable name
    print $x;

The code snippet directly above, produces:

::

    ALPHA 
     BETA
    
    //Since this is declared as a matrix, the text in
    //quotes will create a character vector, rather 
    //than a string array
    declare matrix x = "mean" "variance";
    
    print $x;

produces:

::

    mean variance
    declare array a;

a is a 1-dimensional array of 1 containing 0.

::

    declare sparse matrix sm;

sm is an empty sparse matrix.

::

    struct mystruct {
      matrix m;
      string s;
      string array sa;
      array a;
      sparse matrix sm;
     };
     
    declare struct mystruct ms;

ms is a mystruct structure, with its
members set as follows:
ms.m

empty matrix

ms.s

null string

ms.sa

1x1 string array containing a null string

ms.a

1-dimensional array of 1 containing 0

ms.sm

empty sparse matrix

.. seealso:: Functions :func:`let`, :func:`external`
