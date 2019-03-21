
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

.. seealso:: :func:`changedir`, :func:`cdir`

