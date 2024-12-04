qfitSlopeTest
==============================================

Purpose
----------------
Performs a test of slope equality after :func:`quantileFit`.

Format
----------------
.. function:: { waldTest, p_value } =  qFitSlopeTest 

    :param qout: Post-estimation filled :class:`qfitOut` output structure.
    :type out: Struct

    :param joint: Indicator variable specifying to perform joint test.
    :type joint: Scalar

    :return waldTest: The statistic for testing the null joint hypothesis specified by the R and q inputs.
    :rtype waldTest: Vector

    :return p_value: The p-value associated with the Wald statistic.
    :rtype p_value: Vector

Examples
----------------

Basic test with estimation output structure
++++++++++++++++++++++++++++++++++++++++++++
The default settings of the :func:`waldTest` procedure test the joint hypotheses that all variables equal zero. 

::

    // Data file name
    fname = __FILE_DIR $+ "regsmpl.dta"; 

    // Set up tau for regression
    tau = 0.35|0.55|0.85;

    // Set up control structure
    struct qfitControl qCtl;
    qCtl = qfitControlCreate();

    // Call quantileFit
    struct qfitOut qOut;
    qOut = quantileFit(fname, "ln_wage~age + age:age + tenure", tau, qCtl);

    // Test slope equality
    qfitSlopeTest(qOut, 1);

The code above will print a test summary.

::

    ===================================
    Joint Test of Equality in Slopes : 
    tau in { 0.35 , 0.55 , 0.85 }
    Model: ln_wage ~ 
    age + age_age + tenure 
    -----------------------------------
    F( 9, 28097 ):             138.2428 
    Prob > F :                   0.0000 
    ===================================

.. seealso:: :func:`waldTest`