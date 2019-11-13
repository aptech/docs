
external
==============================================

Purpose
----------------

Lets the compiler know about symbols that are referenced
above or in a separate file from their definitions.

Format
----------------
.. function:: external proc dog, cat
              external keyword dog
              external fn dog
              external matrixx, y, z
              external string mstr, cstr
              external array a, b
              external sparse matrix sma, smb
              external struct structure_type sta, stb

Examples
----------------
Let us suppose that you created a set of procedures defined in
different files, which all set a global matrix *_errcode*
to some scalar error code if errors were encountered.
You could use the following code to call one of the procedures
in the set and check whether it succeeded:

::

    external matrix _errcode;

    // Generate random data
    x = rndn(10, 5);

    // Call procedure
    y = myproc1(x);

    if _errcode;
       print "myproc1 failed";
       end;
    endif;

Without the `external` statement, the compiler would assume that *\_errcode*
was a procedure and incorrectly compile this program. The file
containing the *myproc1* procedure must also contain an `external` statement
that defines *\_errcode* as a matrix, but this would not be encountered by
the compiler until the `if` statement containing the reference to
*\_errcode* in the main program file had already been incorrectly
compiled.

Remarks
-------

See `Procedures and Keywords <PK-ProceduresandKeywords.html>`_.

You may have several procedures in different files that reference the
same global variable. By placing an `external` statement at the top of
each file, you can let the compiler know the type of the symbol.
If the symbol is listed and strongly typed in an active library, no
`external` statement is needed.

If a matrix, string, N-dimensional array, sparse matrix, or structure
appears in an `external` statement, it needs to appear once in a `declare`
statement. If no declaration is found, an ``Undefined symbol`` error message
will result.


.. seealso:: Functions `declare`
