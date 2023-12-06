
plotVariableImportance
==============================================

Purpose
----------------

Plots variable importance table after decision forest regression.

Format
----------------
.. function:: plotVariableImportance(dfm)

    :param dfm: A filled instance of the :class:`dfModel` structure. 
    :type dfm: Struct


Examples
----------------

::

  new;
  library gml;
  rndseed 23423;

  /*
  ** Load data and prepare data
  */
  // Load hitters dataset
  dataset = getGAUSSHome("pkgs/gml/examples/hitters.xlsx");

  // Load data from dataset and split 
  // into (70%) training and (30%) test sets
  { y_train, y_test, X_train, X_test } = trainTestSplit(dataset, "ln(salary)~ AtBat + Hits + HmRun + Runs + RBI + Walks + Years + PutOuts + Assists + Errors", 0.7);

  /*
  ** Train model
  */
  // Structure to hold trained model
  struct dfModel out;

  // Use constrol structure for settings
  struct dfControl dfc;
  dfc = dfControlCreate();

  // Turn on variable importance
  dfc.variableImportanceMethod = 1;

  // Fit training data using decision forest
  out = decForestRFit(y_train, X_train, dfc);

  /*
  ** Set up plot of variable importance
  */
  plotVariableImportance(out);

.. seealso:: Functions :func:`decForestRFit`
