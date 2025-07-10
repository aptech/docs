yjinvtrun
==============================================
Purpose
----------------
Computes the truncated inverse Yeo-Johnson transformation on input data.

Format
----------------
.. function:: y_trunc = yjinvtrun(mu, wdiag, lamnew, x)

:param mu: Location parameter vector.
:type mu: vector

:param wdiag: Diagonal weights.
:type wdiag: vector

:param lamnew: Lambda parameter (logit transformed).
:type lamnew: scalar or vector

:param x: Input data vector.
:type x: vector

:return y_trunc: Truncated inverse transformed vector.
:rtype y_trunc: vector

Library
-------
bhatlib

Source
------
vecup.src