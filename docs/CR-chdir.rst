
chdir
==============================================

Purpose
----------------

Changes working directory in interactive mode.

Format
----------------
.. function:: chdir dirstr

    :param dirstr: directory to change to.
    :type dirstr: literal or ^string

Remarks
-------

This is for interactive use. Use :func:`ChangeDir` in a program.

If the directory change fails, :func:`chdir` prints an error message.

Examples
--------------

Example with literal
++++++++++++++++++++

If your current working directory is ``C:\gauss\time-series`` and you enter:

::

    chdir examples;

Then :func:`chdir` will change your current working directory to ``C:\gauss\time-series\examples``.


Example with string
++++++++++++++++++++

If your current working directory is ``C:\gauss\time-series`` and you enter:

::
 
    dir = "examples";

    // The ^ operator tells GAUSS to use
    // the contents of the string
    chdir ^dir;

Then :func:`chdir` will change your current working directory to ``C:\gauss\time-series\examples``.


.. seealso:: :func:`changedir`, :func:`cdir`

