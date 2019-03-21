
reclassify
==============================================

Purpose
----------------
Replaces specified values of a matrix, array or string array

Format
----------------
.. function:: reclassify(x, from, to)

    :param x: string array or NxKxP array to be recoded (changed)
    :type x: NxK matrix

    :param from: or string array of values to change
    :type from: kx1 vector

    :param to: or string array  containing the new values to be
        assigned to the recoded variable
    :type to: kx1 vector

    :returns: x_new (*Matrix*), multi-dimensional array or string array with the same dimensions as the input x, containing the recoded values of
        x

Examples
----------------

Change instances of 1, 2 and 3 to 'low', 'medium' and 'high'.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Vector to be changed
    x = { 2,
          3,
          2,
          1,
          2,
          3 };
    
    from = { 1,
             2,
             3 };
    
    //Create a 3x1 string array using
    //string vertical concatenation operator
    to = "low" $| "medium" $| "high";
    
    x_new = reclassify(x, from, to);
    print	x_new ;

After the code above, x_new is equal to:

::

    medium
      high
    medium
       low
    medium
      high

Change instances of tea types: 'black', 'green', 'oolong' to 9.95, 11.95 and 10.50, respectively.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    string orders  = {   "green",
                         "green",
                        "oolong",
                         "green",
                         "green",
                         "green",
                         "black" };
    
    string tea_types   = {   "black",
                             "green",
                            "oolong" };
    
    price = { 9.95, 11.95, 10.50 }; 
    
    order_prices = reclassify(orders, tea_types, price);
    print order_prices;

After the code above, order_prices is equal to:

::

    11.95
    11.95
    10.50
    11.95
    11.95
    11.95
    9.95

Source
------

datatran.src

.. seealso:: Functions :func:`code`, :func:`recode`, :func:`reclassifyCuts`, :func:`substute`, :func:`rescale`, :func:`dummy`, :func:`contains`
