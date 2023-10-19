
dfLonger
==============================================

Purpose
----------------
Converts a GAUSS dataframe in wide panel format to long panel format.


Format
----------------
.. function:: df_long = dfLonger(df_wide, columns, names_to, values_to [, pctl])

    :param df_wide: A GAUSS dataframe in wide panel format.
    :type df_wide: Dataframe

    :param columns:  The columns that should be used in the conversion.
    :type columns: String array

    :param names_to: Specifies the variable name(s) for the new column(s) created to store the wide variable names.
    :type names_to: String array

    :param values_to: The name of the new column containing the values.
    :type values_to: String

    :param pctl: An optional :class:`pivotControl` structure with the following members:

        .. list-table::
            :widths: auto

            * - pctl.names_prefix
              - String, the characters, if any, that should be stripped from the front of the wide variable names before they are assigned to a long column.  Default = "", no prefix.
            * - pctl.names_sep_strip
              - String, the character(s), if any, that mark where the ``names_to`` names should be broken up. Default = "", do not break up ``names_to``.
            * - pctl.names_pattern_strip
              - String, a regular expression specifying groups in ``names_to`` names should be broken up. Default = "", do not break up ``names_to``.
            * - pctl.names_types
              - String, containing either: i. a column vector of types for each of the ``names_to`` variables, or ii. an *n x 2* matrix where the first column is the name of the column and the second column contains the types for the variable in the first column. (i.e. ``pctl.names_types = { "Index" "number", "Year" "date" };``. Valid type options include: "date", "number", "category", and "string".
            * - pctl.values_drop_missing
              - Scalar, 0 or 1. If set to 1, all rows with missing values will be removed. Default = 0.

    :type pctl: struct

    :return df_long: The input data converted to long form.

    :rtype df_long: Dataframe

Examples
----------------

Example 1: Basic default case
+++++++++++++++++++++++++++++++++

Step one, load the data.

::

    // Load data
    file_name = getGAUSSHome("examples/tiny_car_panel.csv");
    df_wide = loadd(file_name);

    print df_wide;

::

           Years     Cars_compact       Cars_truck         Cars_SUV
      1973-01-01        5.0000000                .        3.0000000
      1974-01-01        2.0000000        1.0000000        9.0000000


Step two, get the names of the columns we want to pivot to long format.

::

    // Get all column names and remove the first column name, 'Years'
    columns = getcolnames(df_wide);
    columns = trimr(columns, 1, 0);
    print columns;

::

    Cars_compact
      Cars_truck
        Cars_SUV


Step three, perform the pivot.

::

    names_to = "Class";
    values_to = "Count";

    df_long = dfLonger(df_wide, columns, names_to, values_to);

After the above code,  *df_long* will equal:

::

         Years            Class            Count
    1973-01-01     Cars_compact        5.0000000
    1973-01-01       Cars_truck                .
    1973-01-01         Cars_SUV        3.0000000
    1974-01-01     Cars_compact        2.0000000
    1974-01-01       Cars_truck        1.0000000
    1974-01-01         Cars_SUV        9.0000000



Example 2: Basic case with `names_prefix`
+++++++++++++++++++++++++++++++++++++++++++++

You may notice that the elements in the *Class* variable from our previous example
contain a redundant prefix, *Cars_*. We can remove that by using the :class:`pivotControl` structure
and setting the `names_prefix` member to *Class_*.

::

     // Load data
     file_name = getGAUSSHome("examples/tiny_car_panel.csv");
     df_wide = loadd(file_name);

     print df_wide;

::

           Years     Cars_compact       Cars_truck         Cars_SUV
      1973-01-01        5.0000000                .        3.0000000
      1974-01-01        2.0000000        1.0000000        9.0000000

::

    // Get all column names and remove the first column name, 'Years'
    columns = getcolnames(df_wide);
    columns = trimr(columns, 1, 0);

    names_to = "Class";
    values_to = "Count";

    // Declare pivotControl structure and fill with default values
    struct pivotControl pctl;
    pctl = pivotControlCreate();

    pctl.names_prefix = "Cars_";

    // Call dfLonger with optional control structure
    df_long = dfLonger(df_wide, columns, names_to, values_to, pctl);


This time, our *Class* variable will not contain the redundant prefix as we see below:

::

         Years       Class            Count
    1973-01-01     compact        5.0000000
    1973-01-01       truck                .
    1973-01-01         SUV        3.0000000
    1974-01-01     compact        2.0000000
    1974-01-01       truck        1.0000000
    1974-01-01         SUV        9.0000000


Example 3: Advanced options: splitting variable names and setting variable types
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In this example, we will use the *names_sep_split* member of the :class:`pivotControl` structure to break up the
variable names. We will also use the *names_types* member to set the types for the newly created long form variables.

::

  // Load the data
  df_wide = loadd(getGAUSSHome("examples/olympic_vault_wide.csv"));
  print df_wide;   

::

         Country     vault_2012_f     vault_2012_m     vault_2016_f     vault_2016_m 
   United States        48.100000        46.600000        46.900000        45.900000 
          Russia        46.400000        46.900000        45.700000        46.000000 
           China        44.300000        48.300000        44.300000        45.000000

::

  // Get the list of variables to pivot
  // all of them except for the first, 'Country'
  columns =  getcolnames(df_wide);
  columns = columns[2:rows(columns)];

  print columns;

::

    vault_2012_f 
    vault_2012_m 
    vault_2016_f 
    vault_2016_m


Next we will declare our :class:`pivotControl` structure and specify that we want to split the pivot variable names at each underscore.

::
  
  // Declare 'pctl' to be a pivotControl structure
  // and fill with default settings
  struct pivotControl pctl;
  pctl = pivotControlCreate();
  
  // Split the variable names from 'columns', i.e. vault_2012_f, etc
  // every time an underscore is encountered
  pctl.names_sep_split = "_";


Looking at the variable names we just printed earlier, we can see that if we split them at each underscore, we will end up with three separate tokens from each name. Below
we specify a *names_to* for each of these tokens.

::

  names_to = "event" $| "year" $| "gender";
  values_to = "score";


Our final setting is to specify the types we want for each of the *names_to* variables.

::
  
  // Convert 'year' to be a date variable.
  pctl.names_types = { "year" "date" };


Now we call :func:`dfLonger` with the inputs we created and print out the results.

::
  
  df_long = dfLonger(df_wide, columns, names_to, values_to, pctl); 
  print df_long;

::

         Country            event             year           gender            score 
   United States            vault             2012                f        48.100000 
   United States            vault             2012                m        46.600000 
   United States            vault             2016                f        46.900000 
   United States            vault             2016                m        45.900000 
          Russia            vault             2012                f        46.400000 
          Russia            vault             2012                m        46.900000 
          Russia            vault             2016                f        45.700000 
          Russia            vault             2016                m        46.000000 
           China            vault             2012                f        44.300000 
           China            vault             2012                m        48.300000 
           China            vault             2016                f        44.300000 
           China            vault             2016                m        45.000000

We can verify the column types by using the :func:`getcoltypes` function.

::

  print getcoltypes(df_long, "event"$|"year"$|"gender")

::

            type 
        category 
            date 
        category 
 

Example 4: Advanced options: splitting variable names with regular expressions
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In this example, we will take two pairs of variable names, *Brand1* plus *Brand2* and *Price1* plus *Price2* and:

1. Split the variable names by word (Brand or Price) and integer (1 or 2).
2. Create columns from the numberless column names.
3. Create a new variable named *Index* containing the integers from the end of the variable names.

::

    // Create file name with full path
    file = getGAUSSHome("examples/chocolate_choice_wide_short.csv");

    // Load specified variables (specifying the Brand variables to be categorical)
    df_choc = loadd(file, "Subject + Trial + Selection + cat(Brand1) + cat(Brand2) + Price1 + Price2");

    // Print the first 5 rows
    head(df_choc);

::

   Subject      Trial  Selection     Brand1     Brand2     Price1     Price2 
      2401          1          1       Dove     Godiva        0.6        0.7 
      2401          2          2     Godiva     Godiva        2.7        3.9 
      2401          3          2  Hershey's     Godiva        1.7        3.7 
      2401          4          1      Lindt      Lindt          1        3.6 
      2401          5          2  Hershey's     Godiva        0.8        1.5


Next we will specify the *columns* input as in our previous examples:    
    
::
    
    // Column names that will be split
    columns = "Brand1" $| "Brand2" $| "Price1" $| "Price2";


Our *names_to* input will be a little different this time, however.

::
    
    names_to = ".value" $| "Index";
    values_to = "";

Since we will be splitting the variable names into 2 pieces (i.e. *Brand1* -> *Brand* *1*), we need to set one element of *names_to* for each of the pieces from the split variable name. The first element is *".value"*. This tells :func:`dflonger` to take the first piece of the variable name (*Brand* or *Price*) and create a column with the all the values from all matching columns. 

In other words, combine all the values from the variables *Brand1* and *Brand2* into a single variable named *Brand* and do the same for the *Price* columns.  

The second element of *names_to* tells :func:`dflonger` to create a column named *Index* and fill it with the contents of the second piece of the variable names (i.e *1* or *2*). 

Since *names_to* is specifying where to send the "values", *values_to* will be empty.

Now we can set our other options using the `pivotControl` structure.

::
    
    // Declare 'pctl' to be a pivotControl structure
    // and fill with default settings
    struct pivotControl pctl;
    pctl = pivotControlCreate();

The *names_pattern_split* member of the `pivotControl` structure is where we can assign a string with a regular expression that will split the *columns* we specified earlier. A full description of regular expressions is beyond our scope here, however, the most important thing to know is that each statement inside a pair of parentheses is a group. The name will be split by group.

The first group is ``(Brand|Price)``. That will match either "Brand" or "Price". If we had several variable names and did not want to explicitly list them all, we could make our first group ``([a-zA-Z])``. That would match any upper or lower case characters.

Our second group is  ``([0-9])``. That will match any integer. 

::
    
    // Set the regex to split the variable names
    pctl.names_pattern_split = "(Brand|Price)([0-9])";


By default the variables created from the pieces of the variable names will be categorical variables. Since the second peice of our variable, that we set to be called *Index* earlier when we set *names_to*, will be integers, we may not want it to be a categorical variable. So for this example, we will tell GAUSS to make it a numerical variable. 
::
    
    pctl.names_types = { "Index" "number" };  

Now we can call :func:`dflonger` with the inputs we have created.

::
    
    // Convert the dataframe to long format according to our specifications
    df_long = dfLonger(df_choc, columns, names_to, values_to, pctl);

    // Print the first 5 rows of the long form dataframe
    head(df_long);

::

   Subject      Trial  Selection      Index      Brand      Price 
      2401          1          1          1       Dove        0.6 
      2401          1          1          2     Godiva        0.7 
      2401          2          2          1     Godiva        2.7 
      2401          2          2          2     Godiva        3.9 
      2401          3          2          1  Hershey's        1.7    




.. seealso:: Functions :func:`dfwider`
