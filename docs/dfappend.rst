
dfappend
==============================================

Purpose
----------------

Vertically concatenates two dataframes.

Format
----------------
.. function:: df_stacked = dfappend(df1, df2)

    :param df1: The dataframe to stack on top.
    :type df1: Dataframe

    :param df2: The dataframe to add to the bottom of ``df1``.
    :type df2: Dataframe

    :return df_stacked: The result of ``df1`` stacked on top of ``df2``.

    :rtype df_stacked: Dataframe

Examples
----------------

Example
+++++++++++++++

In the example below, we will load data from a Stata dataset and a CSV file and combine selected rows of the dataframes.

::

    // Create file name with full path and load data
    fname = getGAUSSHome() $+ "examples/tips2.dta";
    tips_dta = loadd(fname, "tip + day");

    // Create file name with full path and load data
    fname = getGAUSSHome() $+ "examples/tips2.csv";
    tips_csv = loadd(fname, "tip + cat(day)");

    // Take a small sample of rows
    tips_dta = tips_dta[1:3,.];
    tips_csv = tips_csv[220:223,.];

::

    tips_dta =        tip     day 
                1.0100000     Sun 
                1.6600000     Sun 
                3.5000000     Sun 

    tips_csv =       tip      day 
               1.4400000      Sat 
               3.0900000      Sat 
               2.2000000      Fri 
               3.4800000      Fri


Next we will vertically concatenate the dataframes:

::

    // Create a new dataframe with both
    tips_stacked = dfappend(tips_dta, tips_csv);

::

    tips_stacked =        tip     day 
                    1.0100000     Sun 
                    1.6600000     Sun 
                    3.5000000     Sun 
                    1.4400000     Sat 
                    3.0900000     Sat 
                    2.2000000     Fri 
                    3.4800000     Fri

The reason to use :func:`dfappend` instead of the vertical concatenation operator for dataframes with strings and categorical variables is that :func:`dfappend` will make sure that the category labels and keys are matched in the resulting dataframe.

::

    // Get the category labels and keys for the day variable
    // for the data from the csv and dta files.
    { lab_csv, key_csv } = getcollabels(tips_csv, "day");    
    { lab_dta, key_dta } = getcollabels(tips_dta, "day");    

After running the above code, we see that the keys and their order are different in these dataframes.

::

    lab_csv =  Fri    key_csv =  0 
               Sat               1 
               Sun               2 
              Thur               3 

    lab_dta = Thur    key_dta =  0 
               Fri               1 
               Sat               2 
               Sun               3 


The reason that the category keys and labels are not the same is that the keys for each label are specified in the Stata dataset, however the CSV file just has the text labels. In the case where the keys are not specified, GAUSS will assign the keys based on the alphabetical order of the category labels.

The vertical concatenation operator is optimized for speed and will not check to see if the keys match. It is designed for numeric variables and dates. It should not be used for dataframes with categorical variables.

Remarks
----------------

* :func:`dfappend` should be used instead of the vertical concatenation operator for dataframes with categorical or string columns, because :func:`dfappend` will merge the metadata in cases where the keys and labels are not identical.

* Both inputs must be dataframes.
