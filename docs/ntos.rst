
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

    :param prec: optional argument, the number of significant digits to display, from 1 to 17, or ``"exact"``. Default = 6.

        ``"exact"`` writes each number with the fewest digits that read back as exactly the same number, so 0.1 is ``0.1`` and 0.1+0.2 is ``0.30000000000000004``. 17 digits are enough for any number to read back exactly, but 0.1 becomes ``0.10000000000000001``.

    :type prec: scalar or string

    :return str: contains the string representation of the input.

    :rtype str: string or NxK string array

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

Example 4
+++++++++

::

    x = 0.1 | 0.1 + 0.2;

    print ntos(x, 15);
    print ntos(x, "exact");

returns

::

                 0.1
                 0.3

                 0.1
    0.30000000000000004

The two numbers are not equal, but 15 digits write them as 0.1 and 0.3. ``"exact"`` writes the shortest string that reads back as each number.

Remarks
-------

This function will convert numbers to either decimal representation or
scientific notation, depending upon which is most compact. The behavior
is equivalent to the '%g' format specifier to the 'C' language function
``printf``. The precision of an individual number will be the smaller of the
*prec* input and the maximum number of significant digits.

Missing values are written as ``.`` and infinities as ``+INF`` and ``-INF``.
Numbers smaller than about 2.2e-308 are written as digits, for example
``2.5e-310``, at any precision.

.. seealso:: Functions :func:`ftos`, :func:`stof`
