GAUSS Machine Learning (GML)
==============================================

Description
----------------
Provides tools to model, analyze, and predict data using fundamental machine learning techniques.

Installation
--------------
Please `contact us <https://www.aptech.com/contact-us/>`_ directly to request a copy of the GAUSS Machine Learning library.

Requires GAUSS 22 or higher. 

Commands
----------------------

=============================== ========================================================================================================================================
:func:`binaryClassMetrics`       Computes statistics to assess the quality of binary predictions and prints out a report.
:func:`classificationMetrics`    Computes statistics to assess the quality of classification predictions and prints out a report.
:func:`cvSplit`                  Returns the test and training set for the ith of k cross validation splits for a given set of dependent and independent variables.
:func:`decForestCFit`            Fit a decision forest classification model.
:func:`decForestPredict`         Predicts responses using the output from :func:`decForestCFit` or :func:`decForestRFit` and matrix of independent variables.
:func:`decForestRFit`            Fit a decision forest regression model.
:func:`kmeansFit`                Partitions data into k clusters, using the kmeans algorithm.
:func:`kmeansPredict`            Partitions data into k clusters, based upon k user supplied centroids.
:func:`knnFit`                   Creates a K-D tree model from training data for efficient KNN predictions.
:func:`knnClassify`              Creates nearest neighbor predictions.
:func:`lassoFit`                 Fit a linear model with an L1 penalty.
:func:`lmPredict`                Predict response using output from :func:`lassoFit`, :func:`ridgeFit`, or :func:`ridgeCFit` and matrix of independent variables.
:func:`logisticRegFit`           Fit a logistic regression model with an optional L1 and/or L2 penalty.   
:func:`meanSquaredError`         Returns the mean squared error between two input vectors, or sets of vectors.
:func:`oneHot`                   Returns a matrix of one-hot (indicator) variables from a vector or dataframe column.
:func:`pcaFit`                   Performs principal component dimension reduction.
:func:`pcaTransform`             Reduces the dimension of a matrix using principal component vectors previously returned by :func:`pcaFit`.
:func:`pcaTransformInv`          Transforms a matrix back to the original feature space of the X which was input to :func:`pcaFit`.
:func:`plotClasses`              Plots predicted classes in color coded scatter plot.
:func:`plotLR`                   Plots parameter path and mse path over regularization path after :func:`lassoFit` or :func:`ridgeFit`.
:func:`plotVariableImportance`   Plots variable importance table after decision forest regression.
:func:`ridgeFit`                 Fit a linear model with an L2 penalty.
:func:`ridgeCFit`                Fit a binary classification model with an L2 penalty.
:func:`ridgeCPredict`            Predict binary classifications from :func:`ridgeCFit` model.
:func:`splitData`                Returns test and training splits for a single matrix of variables.
:func:`trainTestSplit`           Returns test and training splits for a given set of dependent and independent variables.
=============================== ========================================================================================================================================

.. toctree::
   :maxdepth: 1
   :hidden:

   binaryclassquality
   classificationmetrics
   cvsplit
   decforestcfit
   decforestpredict
   decforestrfit
   kmeansfit
   kmeanspredict
   knnfit
   knnclassify
   lassofit
   lmpredict
   logisticregfit
   meansquarederror
   onehot
   pcafit
   pcatransform
   pcatransforminv
   plotclasses
   plotlr
   plotvariableimportance 
   ridgecfit
   ridgecpredict
   ridgefit
   splitdata
   traintestsplit
