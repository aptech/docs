
reclassify
==============================================

Purpose
----------------
Replaces specified values of a matrix, array or string array

Format
----------------
.. function:: x_new = reclassify(x, from, to)

    :param x: data to be recoded (changed).
    :type x: NxK matrix or string array or NxKxP array

    :param from: values to change.
    :type from: Kx1 vector or string array

    :param to: contains the new values to be assigned to the recoded variable.
    :type to: Kx1 vector or string array

    :return x_new: Contains the recoded values of *x*, will have the same dimensions as the input *x*.

    :rtype x_new: NxK matrix or string array or NxKxP array

Examples
----------------

Change instances of 1, 2 and 3 to 'low', 'medium' and 'high'.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Vector to be changed
    x = { 2,
          3,
          2,
          1,
          2,
          3 };

    from = { 1,
             2,
             3 };

    // Create a 3x1 string array using
    // string vertical concatenation operator
    to = "low" $| "medium" $| "high";

    x_new = reclassify(x, from, to);
    print x_new;

After the code above, *x_new* is equal to:

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

    string orders  = { "green",
                       "green",
                       "oolong",
                       "green",
                       "green",
                       "green",
                       "black" };

    string tea_types   = { "black",
                           "green",
                           "oolong" };

    price = { 9.95, 11.95, 10.50 };

    order_prices = reclassify(orders, tea_types, price);
    print order_prices;

After the code above, *order_prices* is equal to:

::

    11.95
    11.95
    10.50
    11.95
    11.95
    11.95
     9.95

.. seealso:: Functions `code`, :func:`recode`, :func:`reclassifyCuts`, :func:`substute`, :func:`rescale`, :func:`dummy`, :func:`contains`
