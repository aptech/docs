
tab
==============================================

Purpose
----------------

Tabs the cursor to a specified text column.

Format
----------------
.. function:: tab(col) 
			  print expr1 expr2 tab(col1) expr3 tab(col2) expr4 ...

    :param col: the column position to tab to.
    :type col: scalar



Remarks
-------

col specifies an absolute column position. If col is not an integer, it
will be truncated.

tab can be called alone or embedded in a print statement. You cannot
embed it within a parenthesized expression in a print statement, though.
For example:

::

   print (tab(20) c + d * e);

will not give the results you expect. If you have to use parenthesized
expressions, write it like this instead:
::

   print tab(20) (c + d * e);

