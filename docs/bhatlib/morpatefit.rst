morpateFit
==============================================

Purpose
----------------
Estimates average treatment effects (ATE) using a multivariate ordered response probit (MORP) model by systematically modifying selected covariates and computing the resulting predicted probabilities.

Format
----------------
.. function:: out = morpATEFit(fname, dvordname, davordname, ivord, changevar, changeval[, ctl])

    :param fname: Name of the dataset file to load.
    :type fname: string

    :param dvordname: Vector of dependent ordinal variable names.
    :type dvordname: Kx1 string vector

    :param davordname: Vector of alternative availability variable names.
    :type davordname: Kx1 string vector

    :param ivord: Matrix of independent variable names for the ordered response.
    :type ivord: KxM string matrix

    :param changevar: Vector of variable names to modify for counterfactual evaluation.
    :type changevar: Px1 string vector

    :param changeval: Vector of values to assign to `changevar` for counterfactual evaluation.
    :type changeval: Px1 vector

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

    :return out: Matrix containing each evaluated combination of ordinal levels and its corresponding predicted mean probability.
    :rtype out: Cx(L+1) matrix, where C = total combinations evaluated, L = number of ordinal variables

Details
-------
- Loads the dataset, modifies `changevar` columns to `changeval` for counterfactual estimation.
- Evaluates all possible combinations of ordinal outcome levels systematically.
- Computes predicted probabilities for each combination using the fitted MORP model (`lpr1_morp`).
- Outputs a matrix combining the evaluated level combinations with their average predicted probabilities.
- Reports average predicted probabilities for specific target levels (e.g., level 3) for key outcomes such as happiness, meaningfulness, stress, and tiredness.

Library
-------
bhatlib

Source
------
morpfit.src

.. seealso:: :func:`morpfit`
