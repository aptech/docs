
changeDir
==============================================

Purpose
----------------

Changes the working directory within a program.

Format
----------------
.. function:: d = changeDir(s)

    :param s: directory to change to.
    :type s: string

    :return d: new working directory, or null string if change failed.

    :rtype d: string

Examples
--------------

If your current working directory is ``C:\gauss\time-series`` and you enter:

::

    changeDir("examples");

Then :func:`changeDir` will return:

::

    C:\gauss\time-series\examples

and set your working directory to that folder as well. The folder must exist before using this function.

.. seealso:: Functions `chdir`, :func:`cdir`
