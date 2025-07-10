univariatenormaltrunc
==============================================
Purpose
----------------
Computes the mean and variance of a univariate normal distribution after truncation.

Format
----------------
.. function:: { mu_trunc, sigma_trunc } = univariatenormaltrunc(mu_untrunc, sigma_untrunc, trpoint)

:param mu_untrunc: Untruncated mean.
:type mu_untrunc: scalar

:param sigma_untrunc: Untruncated variance.
:type sigma_untrunc: scalar

:param trpoint: Truncation point.
:type trpoint: scalar

:return mu_trunc: Truncated mean.
:rtype mu_trunc: scalar

:return sigma_trunc: Truncated variance.
:rtype sigma_trunc: scalar

Library
-------
bhatlib

Source
------
vecup.src