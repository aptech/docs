
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

Examples
--------------

Example with literal
++++++++++++++++++++

If your current working directory is ``C:\gauss\time-series`` and you enter:

::

    chdir examples;

Then `chdir` will change your current working directory to ``C:\gauss\time-series\examples``.


Example with string
++++++++++++++++++++

If your current working directory is ``C:\gauss\time-series`` and you enter:

::

    dir = "examples";

    // The ^ operator tells GAUSS to use
    // the contents of the string
    chdir ^dir;

Then `chdir` will change your current working directory to ``C:\gauss\time-series\examples``.


Remarks
-------

This is for interactive use. Use :func:`ChangeDir` in a program.

If the directory change fails, `chdir` prints an error message.

.. seealso:: :func:`changedir`, :func:`cdir`

