
printfmt
==============================================

Purpose
----------------

Prints character, numeric, or mixed matrix using a default
format controlled by the functions formatcv and formatnv.

Format
----------------
.. function:: printfmt(x, mask)

    :param x: 
    :type x: NxK matrix which is to be printed

    :param mask: 1 if x is numeric or 0 if x is character.
        
        
        - or -
        
        1xK vector of 1's and 0's.
        
        The corresponding column of x will be printed as numeric
        where  mask = 1 and as character where  mask = 0.
    :type mask: scalar

    :returns: y (*scalar*), 1 if the function is successful and 0 if it fails.

Remarks
-------

Default format for numeric data is: ''*.*lg '' 16 8

Default format for character data is: ''*.*s '' 8 8


Examples
----------------

::

    c1 = { "age", "height", "weight" };
    c2 = { 31, 70, 160 };
    
    //Horizontally concatenate c1 and c2
    c = c1~c2;
    
    //Print 'c' as numeric data
    print c;
    
    //Print 'c' as character data
    print $c;
    
    //Print column 1 of 'c' as character data and column 2 as 
    //numeric data
    //Note: call disregards the return value
    mask = { 0 1 };
    call printfmt(c, mask);

The output from the three different print statements will be:

::

    +DEN        31.000000
    +DEN        70.000000
    +DEN        160.00000

::

    age
    height
    weight

::

    age               31
    height            70
    weight           160

Only the final print statement from printfmt correctly prints both columns.

Source
++++++

gauss.src

Globals
+++++++

\__fmtcv, \__fmtnv

.. seealso:: Functions :func:`formatcv`, :func:`formatnv`
