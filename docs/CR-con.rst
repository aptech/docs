
con
==============================================

Purpose
----------------
Requests input from the keyboard (console), and returns it in a matrix.

Format
----------------
.. function:: con(r, c)

    :param r: row dimension of matrix.
    :type r: scalar

    :param c: column dimension of matrix.
    :type c: scalar

    :returns: x (*rxc matrix*)

Remarks
-------

:func:`con` gets input from the active window. GAUSS will not ''see'' any input
until you press ``ENTER``, so follow each entry with an ``ENTER``.

*r* and *c* may be any scalar-valued expressions. Nonintegers will be
truncated to an integer.

If *r* and *c* are both set to 1, :func:`con` will cause a question mark to appear
in the window, indicating that it is waiting for a scalar input.

Otherwise, con will cause the following prompt to appear in the window:

::

            - [1,1]

indicating that it is waiting for the :math:`[1,1]` element of the matrix to be
inputted. The - means that :func:`con` will move horizontally through the matrix
as you input the matrix elements. To change this or other options, or to
move to another part of the matrix, use the following commands:

+---------+-------------------------------------+---+--------------+
| u       | up one row                          | U | first row    |
+---------+-------------------------------------+---+--------------+
| d       | down one row                        | D | last row     |
+---------+-------------------------------------+---+--------------+
| l       | left one column                     | L | first column |
+---------+-------------------------------------+---+--------------+
| r       | right one column                    | R | last column  |
+---------+-------------------------------------+---+--------------+
| t       | first element                       |   |              |
+---------+-------------------------------------+---+--------------+
| b       | last element                        |   |              |
+---------+-------------------------------------+---+--------------+
| g #, #  | goto element                        |   |              |
+---------+-------------------------------------+---+--------------+
| g #     | goto element of vector              |   |              |
+---------+-------------------------------------+---+--------------+
|         |                                     |   |              |
+---------+-------------------------------------+---+--------------+
| h       | move horizontally, default          |   |              |
+---------+-------------------------------------+---+--------------+
| v       | move vertically, default            |   |              |
+---------+-------------------------------------+---+--------------+
| exttt\\ | move diagonally, default            |   |              |
+---------+-------------------------------------+---+--------------+
| s       | show size of matrix                 |   |              |
+---------+-------------------------------------+---+--------------+
| n       | display element as numeric, default |   |              |
+---------+-------------------------------------+---+--------------+
| c       | display element as character        |   |              |
+---------+-------------------------------------+---+--------------+
| e       | exp(1)                              |   |              |
+---------+-------------------------------------+---+--------------+
| p       | pi                                  |   |              |
+---------+-------------------------------------+---+--------------+
| .       | missing value                       |   |              |
+---------+-------------------------------------+---+--------------+
|         |                                     |   |              |
+---------+-------------------------------------+---+--------------+
| ?       | show help screen                    |   |              |
+---------+-------------------------------------+---+--------------+
| x       | exit                                |   |              |
+---------+-------------------------------------+---+--------------+

If the desired matrix is 1xN or Nx1, then :func:`con` will automatically exit
after the last element has been entered, allowing you to input the
vector quickly.

If the desired matrix is NxK, you will need to type ``'x'`` to exit when you
have finished entering the matrix data. If you exit before all elements
have been entered, unspecified elements will be zeroed out.

Use a leading single quote for character input.

Examples
----------------

::

    n = con(1,1);
    print rndn(n,n);

If you enter 2 at the :func:`con` generated prompt:

::

    ? 2

the code above will return a 2x2 random matrix, similar to:

::

    -1.2505596        1.6322417
    -1.0894098       0.74763307

In this example, the :func:`con` function is used to obtain
the size of a square matrix of Normal random
variables which is to be printed out.

.. seealso:: Functions :func:`cons`, :func:`let`, :func:`load`

