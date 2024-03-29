
strreplace
==============================================

Purpose
----------------
Replace all matches of a substring with a replacement string.

Format
----------------
.. function:: str_new = strreplace(str, search, replace)

    :param str: to be searched and modified.
    :type str: string, string array, or categorical variable of a dataframe

    :param search: the substring to search for in *str*.
    :type search: string

    :param replace: the substring with which to replace all instances of *search* found in *str*.
    :type replace: string

    :return str_new: new string, string array of categorical variable of a dataframe  which is the same as *str*, except that
        all instances of *search* have been replaced with *replace*.

    :rtype str_new: string

Examples
----------------

Basic search and replace
++++++++++++++++++++++++

::

    // String to be searched in
    str = "My doctor recommends more chocolates, because chocolates are healthy.";

    // String to be searched for
    search = "chocolate";

    // String to be replaced with
    replace = "vegetable";

    // Build new string
    new_str = strreplace(str, search, replace);

After the code above, *new_str* will be set to:

::

    My doctor recommends more vegetables, because vegetables are healthy.

Regularize addresses in string array
++++++++++++++++++++++++++++++++++++

::

    // String array to be searched
    str = "100 Main Ave" $|
          "112 Charles Avenue" $|
          "49 W State St" $|
          "24 Third Avenue";

    // String to search for
    search = "Avenue";

    // String to replace with
    replace = "Ave";

    // Build new string
    new_str = strreplace(str, search, replace);

After the code above, *new_str* will be set to:

::

       "100 Main Ave"
    "112 Charles Ave"
      "49 W State St"
       "24 Third Ave"

Change the name of categories in a dataframe
+++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create 5x1 string array
    states = "CA" $| "FL" $| "California" $| "California" $| "FL";

    // Convert the string array to a dataframe
    // with the variable name 'States'
    df_states = asdf(states, "States");

    print df_states;

::

          States
              CA
              FL
      California
      California
              FL


When :func:`asdf` created the dataframe ``df_states`` from the string array, ``states``, it made a categorical variable and assigned a separate category to each different string it found in ``states``.

We can use the :func:`getcollabels` function to show the categories and labels found.

::

    // Get the category labels and keys from the
    // first (and only) variable in 'df_states'
    { label, keys } = getcollabels(df_states, 1);

After the above code:

::

    labels = "CA"             keys = 0
             "California"            1
             "FL"                    2

::

    // Replace the "California" label with "CA"
    // and remove the "California" category 
    df_states = strreplace(df_states, "California", "CA");

    print df_states;

::

     States 
         CA 
         FL 
         CA 
         CA 
         FL


::

    // Get the new category labels and keys
    { label, keys } = getcollabels(df_states, 1);


As we see below, the observations that previously had the label ``"California"`` and a key value of 1, have now been merged with the ``"CA"`` category.

::

    labels = "CA"             keys = 0
             "FL"                    2


.. seealso:: Functions :func:`recodecatlabels`, :func:`reordercatlabels`, :func:`setbasecat`, :func:`strrindx`, :func:`strsect`
