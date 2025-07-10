gradcdfqvnbycdfbvn
==============================================

Purpose
----------------

Computes the gradients of the ratio of a non-standard approximated quadrivariate normal cumulative distribution function (CDF) to a non-standard bivariate normal CDF. P = cdf_quadrivariate(mu1, mu2, mu3, mu4; cov; x1, x2, x3, x4) / cdf_bivariate(mu1, mu2; cov[1:2,1:2]; x1, x2). 

Format
----------------
.. function:: { gw,grho } = gradcdfqvnbycdfbvn(w,cor)



Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
