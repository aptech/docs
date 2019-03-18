
compile
==============================================

Purpose
----------------

Compiles a source file to a compiled code file. See also  Compiler, Chapter  1.

Format
----------------
.. function:: compile source fname

    :param source: literal or ^string, the name of the file to be compiled.
    :type source: TODO

    :param fname: literal or ^string, optional, the name of the file to be created.
        If not given, the file will have the same filename and path as
        source. It will have a .gcg extension.
    :type fname: TODO

Examples
----------------

::

    compile qxy.e;

In this example, the src_path would be searched for qxy.e, which
would be compiled to a file called qxy.gcg
on the same subdirectory qxy.e was found.

::

    compile qxy.e xy;

In this example, the src_path would be searched for qxy.e which
would be compiled to a file called xy.gcg on the current subdirectory.

.. seealso:: Functions :func:`run`, :func:`use`, :func:`saveall`
