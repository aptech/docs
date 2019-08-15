
varputl
==============================================

Purpose
----------------
Allows a matrix, array, string, or string array to be assigned to a local symbol given as a string argument.

Format
----------------
.. function:: y = varputl(x, n)

    :param x: data which is to be assigned to the target variable.
    :type x: matrix or array or string or string array 

    :param n: the name of the local symbol which will be the target variable
    :type n: string

    :return y: 1 if the operation is successful and 0 if the operation fails.

    :rtype y: scalar

Remarks
-------

*x* and *n* may be global or local. The variable, whose name is in *n*, that *x* is assigned to is always a local.


Examples
----------------

::

    proc myProc(x);
       local a,b,c,d,e,vars,putvar;
       a=1;b=2;c=3;d=5;e=7;
       vars = { a b c d e };
       putvar = 0;
       
       // Keep looping until the user enters a letter 
       // a-e or A-E
       do while putvar $/= vars;
          // Two semi-colons at the end of a print statement, 
          // prevents a 'new line' from being printed
          print "Assign x (" $vars "): ";;
          putvar = upper(cons);
          print;
       endo;
       
       // Assign the variable whose letter/name was entered by 
       // the user to be the value passed into 'myProc'
       call varputl(x,putvar);
       retp(a+b*c-d/e);
    endp;
    
    // Format printing of numbers to allow 2 spaces between them 
    // and 1 digit after the decimal place
    format /rds 2,1;
    
    z = myProc(17);
    print " z is " z;

.. NOTE:: This example will ask for user input at the GAUSS command prompt

produces:

::

    Assign x ( A  B  C  D  E ): a
    
     z is 22.3

.. seealso:: Functions :func:`vargetl`

