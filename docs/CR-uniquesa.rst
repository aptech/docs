
uniquesa
==============================================

Purpose
----------------
Removes duplicate elements from a string vector. NOTE: uniquesa is deprecated. Instances of this function should be replaced by unique.

Format
----------------
.. function:: uniquesa(sv)

    :param sv: 
    :type sv: Nx1 or 1xN string vector

    :returns: y (*sorted Mx1 string vector*) containing all unique
        elements found in  sv.

Examples
----------------

::

    //Create a 8x1 string array
    string comTrades = { "corn", "gold", "soybeans", "silver", "coffee",
                         "oil", "silver", "soybeans" };
    
    //Return an alphabetized string array containing the
    //unique elements from 'comTrades'
    commodity = uniquesa(comTrades);

After the code above, the variables comTrades and commodity will be equal to:

::

    corn
                     gold                  coffee
                 soybeans                    corn
    comTrades =    silver   commodity =      gold
                   coffee                     oil
                      oil                  silver
                   silver                soybeans
                 soybeans

Remarks
-------

It is important to note that the return from uniquesa will always be a
column vector, even if the input string array is a row vector.

Source
------

uniquesa.src

.. seealso:: Functions :func:`unique`, :func:`uniqindxsa`, :func:`uniqindx`
