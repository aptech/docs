
external
==============================================

Purpose
----------------

Lets the compiler know about symbols that are referenced
above or in a separate file from their definitions.

Format
----------------
.. function:: external proc dog, catexternal keyword dogexternal fn dogexternal matrixx, y, zexternal string mstr, cstrexternal array a, bexternal sparse matrix sma, smbexternal struct structure_type sta, stb

Examples
----------------
Let us suppose that you created a set of procedures defined in
different files, which all set a global matrix _errcode
to some scalar error code if errors were encountered.
You could use the following code to call one of the procedures
in the set and check whether it succeeded:

::

    external matrix _errcode;
    x = rndn(10,5);
    y = myproc1(x);
    if _errcode;
       print "myproc1 failed";
       end;
    endif;

external
_errcode
myproc1
external
_errcode
if
_errcode

.. seealso:: Functions :func:`declare`
