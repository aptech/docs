
intrsect
==============================================

Purpose
----------------
Returns the intersection of two vectors, with duplicates removed.

Format
----------------
.. function:: y = intrsect(v1, v2[, flag])

    :param v1: data
    :type v1: Nx1 vector or string array

    :param v2: data

        .. NOTE:: *v2* must be the same type as *v1*

    :type v2: Mx1 vector or string array

    :param flag: Optional argument, if 1, *v1* and *v2* are numeric; if 0, character. Default is *flag* equal to 1 (numeric).
    :type flag: scalar

    :returns: **y** (*Lx1 vector*) - all unique values that are in both *v1* and *v2* sorted in ascending order.

Remarks
-------

#. If not matches are found, :func:`intrsect` will return a scalar error code
   that can be tested for with :func:`scalmiss`.
#. Place smaller vector first for fastest operation.
#. If there are a lot of duplicates within a vector, it is faster to
   remove them with the function :func:`unique` before calling :func:`intrsect`.


Examples
----------------

Basic usage, numeric
++++++++++++++++++++

::

    // Subject ID's from study 'a'
    id_a = { 3758,
             3773,
             2615,
             2511 };

    // Subject ID's from study 'b'
    id_b = { 3779,
             3773,
             2001,
             3758,
             1585,
             2511 };

    // Find the ID's that are in both groups
    id_common = intrsect(id_a, id_b);

After the code above, *id_common* is equal to:

::

    2511
    3758
    3773

Basic usage, string array
+++++++++++++++++++++++++

::

    /*
    ** Variable names from dataset 'a'
    ** Create string array with the string
    ** vertical concatenation operator ($|)
    */
    names_a = "oil" $| "copper" $| "silver" $| "cocoa";

    // Variable names from dataset 'b'
    names_b = "oil" $| "coffee" $| "cocoa" $| "tea";

    // Find the variable names that are in both groups
    names_common = intrsect(names_a, names_b);

After the code above, *names_common* is equal to:

::

    cocoa
      oil

Character vectors
+++++++++++++++++

A character vector is different from a string array. A character vector is up to eight characters inside of the element of a numeric matrix.

::

    /*
    ** Variable names from dataset 'a'
    ** Create character vector array with the
    ** numeric vertical concatenation operator (|)
    */
    names_a = "oil" | "copper" | "silver" | "cocoa";

    // Variable names from dataset 'b'
    names_b = "oil" | "coffee" | "cocoa" | "tea";

    // Set flag to tell 'intrsectsa' to treat input as character data
    flag = 0;

    // Find the variable names that are in both groups
    names_common = intrsect(names_a, names_b, flag);

    /*
    ** Notice the $ in front of 'names_common'
    ** tells GAUSS to print as character data
    */
    print $names_common;

The code above, will print the following output:

::

    cocoa
      oil

Source
------

intrsect.src

.. seealso:: Functions :func:`intrsectsa`
