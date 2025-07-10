gradnoncdqtvn
==============================================

Purpose
----------------

Develops gradients with respect to the ratio of a standard approximated quadrivariate normal cumulative function to a standard bivariate  

Format
----------------
.. function:: { gmu,gcov,gx } = gradnoncdqtvn(mu,cov,x)



Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Global Variables
------------

- x = { x1,x2,x3,x4 };
- mu = { mu1,mu2,mu3,mu4 };
- cov = { cov11  cov12  cov13   cov14,               cov is a covariance matrix
- S    = { S11   S12    S13    S14,              cov = S'*S;
- gmu      =           { dP/dmu1,
- gcov      =          { dP/dcov11
- gcov      =          { dP/dS11
- gx      =            { dP/dx1,
- gradcdfqvnbycdfbvn.src
- 

Source
------------

gradients-mvn.src
