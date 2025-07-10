morpFit
==============================================

Purpose
----------------
Estimates a multivariate ordered response probit (MORP) model using flexible correlation structures and efficient maximum likelihood estimation.

Format
----------------
.. function:: result = morpFit(fname, dvordname, davordname, ivord[, ctl])

    :param fname: Name of the dataset file to load.
    :type fname: string

    :param dvordname: Vector of dependent ordinal variable names.
    :type dvordname: Kx1 string vector

    :param davordname: Vector of alternative availability variable names.
    :type davordname: Kx1 string vector

    :param ivord: Matrix of independent variable names for the ordered response.
    :type ivord: KxM string matrix

    :param ctl: Optional. Instance of a :class:`morpControl` structure for advanced control of estimation options. If not provided, defaults are used.

        .. list-table::
            :widths: auto

            * - **Member**
              - **Type**
              - **Default**
              - **Description**
            * - ctl.method
              - string
              - ``"OVUS"``
              - Analytic approximation method to use in estimation.
            * - ctl.spher
              - scalar
              - ``0``
              - If 1, uses spherical parameterization; if 0, uses radial parameterization.
            * - ctl.indep
              - scalar
              - ``0``
              - If 1, assumes independence across equations; if 0, allows correlation.
            * - ctl.indepfirst
              - scalar
              - ``0``
              - If 1, estimates the independence model first before correlated estimation.
            * - ctl.correst
              - matrix
              - ``{}``
              - Correlation restriction matrix for advanced restriction specifications.

    :type ctl: struct

    :return result: Returns 1 upon successful estimation.
    :rtype result: scalar

Details
-------
- Uses the `morpControl` structure to specify method, independence assumptions, spherical parameterizations, and correlation restrictions.
- Automatically initializes and structures threshold parameters, independent variable parameters, and correlation parameters for the ordered response model.
- Utilizes `maxlik` and `maxprt` for iterative maximum likelihood estimation with the appropriate likelihood gradient functions for initial estimation and final covariance computation.
- Handles estimation for both independent and correlated structures, including advanced correlation restriction handling and scaling.

Library
-------
bhatlib

Source
------
morpfit.src

.. seealso:: :func:`morpControlCreate`, :func:`maxlik`, :func:`maxprt`
