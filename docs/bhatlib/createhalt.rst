createhalt
==============================================
Purpose
----------------
Generates Halton sequences for quasi-random number generation for simulation.

Format
----------------
.. function:: createhalt(datainunif, datainbrat, nrep, nobs, ndim, mu, cov, runno)

    :param datainunif: File path for uniform Halton data.
    :type datainunif: string

    :param datainbrat: File path for Bratley Halton data.
    :type datainbrat: string

    :param nrep: Number of repetitions.
    :type nrep: scalar

    :param nobs: Number of observations.
    :type nobs: scalar

    :param ndim: Number of dimensions.
    :type ndim: scalar

    :param mu: Mean vector for simulation.
    :type mu: vector

    :param cov: Covariance matrix for simulation.
    :type cov: matrix

    :param runno: Run identifier number.
    :type runno: scalar

Library
-------
bhatlib

Source
------
vecup.src