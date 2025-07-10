gradpdfn
==============================================

Purpose
----------------

Computes the probability density function (PDF) of a non-standard univariate normal distribution for multiple observations. 

Format
----------------
.. function:: gs = gradpdfn(s)


    :param s: (Qx1) vector of abscissae, where Q corresponds to the number of observations.
    :type s: (Specify type)

    :return gs: (Qx1) vector of gradients of the normal PDF with respect to s.
    :rtype gs: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - This function calculates the derivative of the standard normal PDF at each value in s.
- - The gradient is computed as: gs = -s * pdfn(s), where pdfn(s) is the standard normal density.

Source
------------

gradients-mvn.src
