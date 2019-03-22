
ntos
==============================================

Purpose
----------------

Converts a floating point number to a string or string array with optionally specified precision.

Format
----------------
.. function:: ntos(num, prec)

    :param num: 
    :type num: scalar or NxK matrix; the numbers to be converted to a string

    :param prec: optional argument; the number of digits to display. If the precision input is not specified, the default value is 6. Valid input values are: 1 ≤ prec ≤ 15.
    :type prec: Scalar

    :returns: str (*String or NxK string array*) containing the string representation of the input.

Examples
----------------

//Set 'pi_num' equal to the constant 'pi'
pi_num = pi;

//Create a string containing the first 6 digits of pi
pi_str = ntos(pi_num);
print pi_str;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    3.14159

roi = 6.725301;

//Convert to string with 3 digits
roi_str = ntos(roi, 3);

//Combine strings
out = "The project had an ROI of " $+ roi_str $+ "%";
print out;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    The project had an ROI of 6.73%

parm = { 1982 2.75000, 
         1983 2.20272, 
         1984 2.55102 };

//Convert to string array with max of 5 digits per element
parms = ntos(parm, 5);

print parms;
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    1982             2.75 
        1983           2.2027 
        1984            2.551

Remarks
-------

This function will convert numbers to either decimal representation or
scientific notation, depending upon which is most compact. The behavior
is equivalent to the '%g' format specifier to the 'C' language function
printf. The precision of an individual number will be the smaller of the
prec input and the maximum number of significant digits.

.. seealso:: Functions :func:`ftos`, :func:`stof`
