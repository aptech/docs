linearMDCEVFit
==========================

Purpose
-------

Estimates parameters for the Multiple Discrete-Continuous Extreme Value (MDCEV) model using linear utility for the outside good. Supports input data and specification strings for consumption quantities and explanatory variables.

Format
------

.. function:: beta_hat = linearMDCEVFit(fname, dvunordname, davunordname, ivmt, ivgt [, weight_var, varnam, varngam])

    :param fname: Path to the dataset.
    :type fname: string

    :param dvunordname: Labels of dependent variables (consumption quantities). Must include the outside good as the first entry.
    :type dvunordname: string array

    :param davunordname: Labels of price variables. Set to ``"none"`` if there is no price variation.
    :type davunordname: string or string array

    :param ivmt: Specification of independent variables (baseline utilities) for each alternative. Each row corresponds to an alternative, and each column to a variable.
    :type ivmt: string matrix

    :param ivgt: Specification of independent variables for translation (satiation) parameters for each alternative.
    :type ivgt: string matrix

    :param weight_var: Optional input. Label of the weight variable in the dataset. If not provided, all observations are treated as equally weighted.
    :type weight_var: string, default = ``"uno"``

    :param varnam: Optional input. Names of variables in the baseline utility specification.
    :type varnam: string vector, default = auto-generated from `dvunordname` and `ivmt`

    :param varngam: Optional input. Names of variables in the translation specification.
    :type varngam: string vector, default = auto-generated from `dvunordname` and `ivgt`

    :return beta_hat: Estimated model coefficients including baseline utility, translation, and scale parameters.
    :rtype beta_hat: column vector

Remarks
-------

- This function supports weighted estimation if a column name is passed for weights.
- The first good is treated as the outside good and normalized accordingly.
- Internally, the model uses two maximum likelihood steps to first estimate and then refine the scale parameter.
- Parameter names are optionally passed or auto-generated using variable specifications.

Examples
--------

Estimate an MDCEV model with linear utility using tourism expenditure data:

::

    new;
    cls;
    library bhatlib, maxlik;

    fname = __FILE_DIR $+ "WorkshopData_ToursimExp_rev.csv";

    string dvunordname = { "Transp" "Accomod" "FandB" "Shp" "Recr" };
    davunordname = "none";

    string ivmt = {
        "sero" "sero" "sero" "sero" "sero" "sero" "sero" "sero" "sero" "sero",
        "uno"  "sero" "sero" "sero" "urban" "sero" "sero" "sero" "stlt3" "st410",
        "sero" "uno"  "sero" "sero" "sero" "urban" "sero" "sero" "sero" "sero",
        "sero" "sero" "uno"  "sero" "sero" "sero" "urban" "sero" "sero" "sero",
        "sero" "sero" "sero" "uno"  "sero" "sero" "sero" "urban" "sero" "sero"
    };

    string ivgt = {
        "uno"  "sero" "sero" "sero" "sero" "sero" "sero" "sero" "sero" "sero" "sero" "sero" "sero",
        "sero" "uno"  "sero" "sero" "sero" "urban" "sero" "sero" "stlt3" "st410" "sero" "sero" "sero",
        "sero" "sero" "uno"  "sero" "sero" "sero" "urban" "sero" "sero" "sero"  "b51q11" "sero" "sero",
        "sero" "sero" "sero" "uno"  "sero" "sero" "sero" "urban" "sero" "sero" "sero"  "b51q11" "sero",
        "sero" "sero" "sero" "sero" "uno"  "sero" "sero" "sero" "sero" "sero" "sero"  "sero"  "b51q11"
    };

    beta_hat = linearMDCEVFit(fname, dvunordname, davunordname, ivmt, ivgt);

Library
-------

bhatlib

Source
------

bhatlib.src


