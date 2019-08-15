
ntos
==============================================

Purpose
----------------

Converts a floating point number to a string or string array with optionally specified precision.

Format
----------------
.. function:: str = ntos(num[, prec])

    :param num: the numbers to be converted to a string
    :type num: scalar or NxK matrix

    :param prec: optional argument. the number of digits to display. If the precision input is not specified, the default value is 6.
    
        Valid input values are: :math:`1 ≤ prec ≤ 15`.

    :type prec: scalar

    :return str: containing the string representation of the input.

    :rtype str: string or NxK string array

Remarks
-------

This function will convert numbers to either decimal representation or
scientific notation, depending upon which is most compact. The behavior
is equivalent to the '%g' format specifier to the 'C' language function
``printf``. The precision of an individual number will be the smaller of the
*prec* input and the maximum number of significant digits.

Examples
----------------

Example 1
+++++++++

::

    // Set 'pi_num' equal to the constant 'pi'
    pi_num = pi;
    
    // Create a string containing the first 6 digits of pi
    pi_str = ntos(pi_num);
    print pi_str;

returns

::

    3.14159

Example 2
+++++++++

::

    roi = 6.725301;
    
    // Convert to string with 3 digits
    roi_str = ntos(roi, 3);
    
    // Combine strings
    out = "The project had an ROI of " $+ roi_str $+ "%";
    print out;

returns

::

    The project had an ROI of 6.73%

Example 3
+++++++++

::

    parm = { 1982 2.75000, 
             1983 2.20272, 
             1984 2.55102 };
    
    // Convert to string array with max of 5 digits per element
    parms = ntos(parm, 5);

    print parms;

returns

::

        1982             2.75 
        1983           2.2027 
        1984            2.551

.. seealso:: Functions :func:`ftos`, :func:`stof`

