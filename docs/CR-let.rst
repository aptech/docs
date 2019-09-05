
let
==============================================

Purpose
----------------

Creates a matrix from a list of numeric or character values. The result is always of type matrix,
string, or string array.

.. _let:
.. index:: let

Format
----------------

::

    let x = constant_list;

Remarks
-------

Expressions and variable names are not allowed in the `let` command, expressions such as this:

::

    let x[2, 1] = 3*a b

are illegal. To define matrices by combining matrices and expressions,
use an expression containing the concatenation operators: ``~`` and ``|``.

Numbers can be entered in scientific notation. The syntax is :math:`dE±n`, where
*d* is a number and *n* is an integer (denoting the power of 10):

::

    let x = 1e+10 1.1e-4 4.019e+2;

Complex numbers can be entered by joining the real and imaginary parts
with a sign (+ or -); there should be no spaces between the numbers and
the sign. Numbers with no real part can be entered by appending an "i"
to the number:

::

    let x = 1.2+23 8.56i 3-2.1i -4.2e+6i 1.2e-4-4.5e+3i;

If curly braces are used, the `let` is optional.

::

    let x = { 1 2 3, 4 5 6, 7 8 9 };

::

    x = { 1 2 3, 4 5 6, 7 8 9 };

If indices are given, a matrix of that size will be created:

::

    let x[2,2] = 1 2 3 4;

::

    x = 1 2
        3 4

If indices are not given, a column vector will be created:

::

    let x = 1 2 3 4;

::

        1
    x = 2
        3
        4

You can create matrices with no elements, i.e., "empty matrices" . Just
use a set of empty curly braces:

::

    x = {};

Empty matrices are chiefly used as the starting point for building up a
matrix, for example in a `do` loop. See **Matrices**, Section 1.0.1, for
more information on empty matrices.

Character elements are allowed in a `let` statement:

::

    let x = age pay sex;

::

        AGE
    x = PAY
        SEX

Lowercase elements can be created if quotation marks are used. Note that
each element must be quoted.

::

   let x = "age""pay""sex";

::

        age
    x = pay
        sex


Examples
----------------

::

    let x;

assigns *x* to be:

::

    x = 0

::

    let x = { 1 2 3, 4 5 6, 7 8 9 };

assigns *x* to be:

::

        1 2 3
    x = 3 4 5
        6 7 8

::

    let x[3,3] = 1 2 3 4 5 6 7 8 9;

assigns *x* to be:

::

        1 2 3
    x = 3 4 5
        6 7 8

::

    let x[3,3] = 1;

assigns *x* to be:

::

        1 1 1
    x = 1 1 1
        1 1 1

::

    let x[3,3];

assigns *x* to be:

::

    0 0 0
    x = 0 0 0
        0 0 0

::

    let x = dog cat;

assigns *x* to be:

::

    x = DOG
        CAT

::

    let x = "dog""cat";

assigns *x* to be:

::

    x = dog
        cat

::

    let string x = { "Median Income", "Country" };

assigns *x* to be:

::

    x = Median Income
        Country

.. seealso:: Functions :func:`con`, :func:`cons`, `declare`, `load`
