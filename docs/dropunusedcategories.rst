
dropUnusedCategories
==============================================

Purpose
----------------

Removes categories and keys from the meta data of a dataframe variable.

Format
----------------
.. function:: df = dropUnusedCategories(X, [, column])

    :param X: Data with metadata.
    :type X: NxK dataframe

    :param column: Optional argument, name or index of the categorical variable in *X* which contains categories to be removed. Must be specified if *X* contains more than one column. Default = 1.
    :type column: Scalar or string

    :return df: Data with specified categories removed.
    :rtype df: NxK dataframe


Examples
----------------

::

    // Load data
    fname = getGAUSSHome("examples/yarn.xlsx");
    yarn = loadd(fname, "amplitude + cycles");
    
    // Select the first 5 rows only
    yarn = yarn[1:5,.];
    
    print yarn;

This sample from the first five rows only contains the categories, *low* and *med*.

::

       amplitude           cycles 
             low        674.00000 
             low        370.00000 
             low        292.00000 
             med        338.00000 
             med        266.00000

However, when the dataframe was loaded, it also contained one more level, *high*. Using the :func:`getcategories` function, we can see that this information is still stored in *yarn*.

::

    print getCategories(yarn, "amplitude");

::

      categories 
            high 
             low 
             med

There are several reasons that this is, in most cases, convenient and dramatically improves performance. However, that discussion is beyond the scope of this page.


You can use :func:`dropunusedcategories` to remove these unused categories:

::

    // Drop all categories from the meta data
    // that are not represented in the column
    yarn = dropUnusedCategories(yarn, "amplitude");

Now we see that the category *high* is no longer recorded in the meta data for the *amplitude* variable.

::

    print getCategories(yarn, "amplitude");

::

          categories 
                 low 
                 med

.. seealso:: Functions :func:`getColLabels`, :func:`getCategories`, :func:`reordercatlabels`

