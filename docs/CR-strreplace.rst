
strreplace
==============================================

Purpose
----------------
Replace all matches of a substring with a replacement string.

Format
----------------
.. function:: str_new = strreplace(str, search, replace)

    :param str: to be searched and modified.
    :type str: string

    :param search: the substring to search for in *str*.
    :type search: string

    :param replace: the substring with which to replace all instances of *search* found in *str*.
    :type replace: string

    :return str_new: new string which is the same as *str*, except that
        all instances of *search* have been replaced with *replace*.

    :rtype str_new: string

Examples
----------------

Basic search and replace
++++++++++++++++++++++++

::

    str = "My doctor recommends more chocolates, because chocolates are healthy.";
    
    search = "chocolate";
    replace = "vegetable";
        
    new_str = strreplace(str, search, replace);
    
After the code above, *new_str* will be set to:

::

    My doctor recommends more vegetables, because vegetables are healthy.

Regularize addresses in string array
++++++++++++++++++++++++++++++++++++

::

    str = "100 Main Ave" $|
          "112 Charles Avenue" $|
          "49 W State St" $|
          "24 Third Avenue";
    
    search = "Avenue";
    replace = "Ave";
        
    new_str = strreplace(str, search, replace);

After the code above, *new_str* will be set to:

::

       "100 Main Ave"
    "112 Charles Ave"
      "49 W State St"
       "24 Third Ave"

.. seealso:: Functions :func:`strrindx`, :func:`strsect`

