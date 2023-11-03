
isstring
==============================================

Purpose
----------------

Returns a 1 if the input is a string or string array, otherwise 0.

Format
----------------
.. function:: ret = isstring(x)

    :param x: the symbol to be checked.
    :type x: matrix, dataframe, string or string array

    :return ret: A 1 if the input is a string or string array, otherwise 0.

    :rtype ret: scalar

Examples
----------------

Basic cases
+++++++++++++

::

    // Test for string 
    ret_1 = isstring("This is a string");
    
    // Form string *sa*
    sa = "This is a " $| "string array";
    
    // Test if sa is string
    ret_2 = isstring(sa);

The code above assigns *ret_1* and *ret_2* to be equal to 1.

::

    x = { 1 2, 3 4 };
    ret_3 = isstring(x);
    

The code above assigns *ret_3* to be equal to 0.

Dataframes
+++++++++++++

As we would expect, the :func:`isstring` will return a 1 when passed the following string array.

::
    
    // Create string array
    sa = "hight" $| "medium" $| "high" $| "low";

    // Test if sa is a string
    ret = isstring(sa);

::

    ret = 1

However, if we convert it to a categorical or string dataframe :func:`isstring` will return a 0.

::

    
    // Create string array
    sa = "high" $| "medium" $| "high" $| "low";

    // Create a dataframe from the string data
    df = asdf(sa, "Fan speed");
    print df;

::

       Fan speed 
            high 
          medium 
            high 
             low

::

    ret = isstring(df);

After the above code *ret* will equal 0.


Remarks
-------

#. To find out if a dataframe or dataframe column is of type string, category, date or number, use :func:`getcoltypes`.


.. seealso:: Functions :func:`getcoltypes`, :func:`type`
