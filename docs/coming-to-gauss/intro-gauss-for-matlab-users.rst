
Introduction to GAUSS for MATLAB Users
======================================

GAUSS and MATLAB are both matrix-based programming languages. If you're comfortable with MATLAB, you'll find GAUSS syntax familiar—but with important differences. This guide covers the key translations.

Why Consider GAUSS?
-------------------

Both languages excel at matrix computation. GAUSS offers:

- **Econometrics focus**: Built-in and add-on functions designed for econometric workflows
- **Competitive speed**: Intel MKL backend, same as MATLAB
- **Lower cost**: Especially for academic and small-team use
- **40-year stability**: Code from the 1990s still runs

The tradeoff: MATLAB has a larger ecosystem (toolboxes, Simulink, community).

Key Syntax Differences
----------------------

+-------------------+---------------------------+---------------------------+
| Feature           | MATLAB                    | GAUSS                     |
+===================+===========================+===========================+
| Indexing          | 1-based                   | 1-based (same)            |
+-------------------+---------------------------+---------------------------+
| Matrix delimiter  | ``[ ]``                   | ``{ }``                   |
+-------------------+---------------------------+---------------------------+
| Row separator     | ``;`` or newline          | ``,`` or newline          |
+-------------------+---------------------------+---------------------------+
| String quotes     | ``" "`` or ``' '``        | ``" "`` only              |
+-------------------+---------------------------+---------------------------+
| Statement end     | Optional ``;``            | Required ``;``            |
+-------------------+---------------------------+---------------------------+
| All rows/cols     | ``:``                     | ``.``                     |
+-------------------+---------------------------+---------------------------+
| Concatenate horiz | ``[A B]``                 | ``A~B``                   |
+-------------------+---------------------------+---------------------------+
| Concatenate vert  | ``[A; B]``                | ``A|B``                   |
+-------------------+---------------------------+---------------------------+
| Solve ``Ax = b``  | ``A\b``                   | ``inv(A)*b`` or ``solpd`` |
+-------------------+---------------------------+---------------------------+

Matrix Creation
---------------

.. code-block:: matlab

    % MATLAB
    A = [1 2 3; 4 5 6; 7 8 9]

::

    // GAUSS
    A = { 1 2 3, 4 5 6, 7 8 9 };

**Note:** GAUSS uses braces ``{ }`` and commas between rows. Semicolons end statements, not rows.

Special matrices:

.. code-block:: matlab

    % MATLAB
    zeros(3,3)
    ones(3,3)
    eye(3)
    rand(3,3)
    randn(3,3)

::

    // GAUSS
    zeros(3, 3);
    ones(3, 3);
    eye(3);
    rndu(3, 3);    // Uniform [0,1]
    rndn(3, 3);    // Standard normal

Sequences:

.. code-block:: matlab

    % MATLAB
    1:5           % Row vector [1 2 3 4 5]
    1:0.5:3       % [1 1.5 2 2.5 3]
    linspace(0,1,5)

::

    // GAUSS
    seqa(1, 1, 5);      // Column vector, start=1, inc=1, n=5
    seqa(1, 0.5, 5);    // [1; 1.5; 2; 2.5; 3]
    seqa(0, 0.25, 5);   // Equivalent to linspace(0,1,5)

Indexing
--------

Both languages use 1-based indexing, but the "all elements" syntax differs:

.. code-block:: matlab

    % MATLAB
    A(1,1)        % Element
    A(1,:)        % First row
    A(:,1)        % First column
    A(1:2,:)      % Rows 1-2
    A(end,:)      % Last row

::

    // GAUSS
    A[1,1];       // Element
    A[1,.];       // First row (dot = all)
    A[.,1];       // First column
    A[1:2,.];     // Rows 1-2
    A[rows(A),.]; // Last row

**Key difference:** MATLAB uses ``:`` for "all", GAUSS uses ``.``

Operators
---------

Element-wise vs. matrix operations:

.. code-block:: matlab

    % MATLAB
    A * B         % Matrix multiplication
    A .* B        % Element-wise multiplication
    A .^ 2        % Element-wise power
    A'            % Conjugate transpose
    A.'           % Transpose

::

    // GAUSS
    A * B;        // Matrix multiplication (same)
    A .* B;       // Element-wise multiplication (same)
    A .^ 2;       // Element-wise power (same)
    A';           // Transpose (GAUSS has no conjugate transpose)

**Good news:** Element-wise operators (``.* ./ .^``) work the same in both languages.

Concatenation
-------------

.. code-block:: matlab

    % MATLAB
    [A B]         % Horizontal concatenation
    [A; B]        % Vertical concatenation

::

    // GAUSS
    A ~ B;        // Horizontal concatenation (tilde)
    A | B;        // Vertical concatenation (pipe)

Example:

::

    A = { 1 2, 3 4 };
    B = { 5, 6 };

    print A ~ B;   // [1 2 5; 3 4 6]
    print A | B';  // [1 2; 3 4; 5 6]

Linear Algebra
--------------

.. code-block:: matlab

    % MATLAB
    inv(A)
    det(A)
    eig(A)
    [V,D] = eig(A)
    svd(A)
    chol(A)
    rank(A)
    A \ b          % Solve Ax = b

::

    // GAUSS
    inv(A);
    det(A);
    eig(A);               // Returns eigenvalues only
    { val, vec } = eigv(A);  // Eigenvalues and vectors
    { u, s, v } = svd(A);
    chol(A);
    rank(A);
    inv(A) * b;           // Solve Ax = b (no backslash)

**Solving linear systems:** GAUSS doesn't have MATLAB's backslash operator. Use ``inv(A)*b`` for small systems or specialized solvers (``solpd`` for positive definite).

Functions and Procedures
------------------------

.. code-block:: matlab

    % MATLAB
    function y = square(x)
        y = x.^2;
    end

::

    // GAUSS
    proc (1) = square(x);
        retp(x.^2);
    endp;

**Key differences:**

- GAUSS uses ``proc`` / ``endp`` instead of ``function`` / ``end``
- Return values use ``retp()`` not assignment
- Number of outputs declared in ``proc (n) =``

Multiple outputs:

.. code-block:: matlab

    % MATLAB
    function [a, b] = myFunc(x)
        a = x + 1;
        b = x - 1;
    end

::

    // GAUSS
    proc (2) = myFunc(x);
        local a, b;
        a = x + 1;
        b = x - 1;
        retp(a, b);
    endp;

    // Call it
    { result1, result2 } = myFunc(5);

Control Flow
------------

Loops and conditionals are similar:

.. code-block:: matlab

    % MATLAB
    for i = 1:10
        disp(i)
    end

    if x > 0
        disp('positive')
    elseif x < 0
        disp('negative')
    else
        disp('zero')
    end

::

    // GAUSS
    for i (1, 10, 1);
        print i;
    endfor;

    if x > 0;
        print "positive";
    elseif x < 0;
        print "negative";
    else;
        print "zero";
    endif;

**Note:** GAUSS requires semicolons after control statements.

Data Import/Export
------------------

.. code-block:: matlab

    % MATLAB
    data = readtable('file.csv');
    data = xlsread('file.xlsx');
    save('output.mat', 'data')

::

    // GAUSS
    data = loadd("file.csv");
    data = loadd("file.xlsx");
    save data = "output.gdat";   // GAUSS format

    // Or export to CSV/Excel
    saved(data, "output.csv", getcolnames(data));

Statistics and Econometrics
---------------------------

Basic statistics:

.. code-block:: matlab

    % MATLAB
    mean(x)       % Column means
    std(x)        % Column std devs
    sum(x)        % Column sums
    cov(x)        % Covariance matrix

::

    // GAUSS
    meanc(x);     // Column means
    stdc(x);      // Column std devs
    sumc(x);      // Column sums
    vcx(x);       // Covariance matrix

OLS regression:

.. code-block:: matlab

    % MATLAB (Statistics Toolbox)
    mdl = fitlm(X, y);

::

    // GAUSS (built-in)
    call olsmt(data, "y ~ x1 + x2");

Quick Reference Table
---------------------

+-------------------------+---------------------------+---------------------------+
| Operation               | MATLAB                    | GAUSS                     |
+=========================+===========================+===========================+
| Create matrix           | ``[1 2; 3 4]``            | ``{ 1 2, 3 4 }``          |
+-------------------------+---------------------------+---------------------------+
| Zeros                   | ``zeros(n,m)``            | ``zeros(n, m)``           |
+-------------------------+---------------------------+---------------------------+
| Identity                | ``eye(n)``                | ``eye(n)``                |
+-------------------------+---------------------------+---------------------------+
| Random uniform          | ``rand(n,m)``             | ``rndu(n, m)``            |
+-------------------------+---------------------------+---------------------------+
| Random normal           | ``randn(n,m)``            | ``rndn(n, m)``            |
+-------------------------+---------------------------+---------------------------+
| Sequence                | ``1:n``                   | ``seqa(1, 1, n)``         |
+-------------------------+---------------------------+---------------------------+
| All rows                | ``A(:,j)``                | ``A[.,j]``                |
+-------------------------+---------------------------+---------------------------+
| All columns             | ``A(i,:)``                | ``A[i,.]``                |
+-------------------------+---------------------------+---------------------------+
| Last element            | ``A(end)``                | ``A[rows(A)*cols(A)]``    |
+-------------------------+---------------------------+---------------------------+
| Horizontal concat       | ``[A B]``                 | ``A~B``                   |
+-------------------------+---------------------------+---------------------------+
| Vertical concat         | ``[A; B]``                | ``A|B``                   |
+-------------------------+---------------------------+---------------------------+
| Transpose               | ``A'`` or ``A.'``         | ``A'``                    |
+-------------------------+---------------------------+---------------------------+
| Element-wise mult       | ``A .* B``                | ``A .* B``                |
+-------------------------+---------------------------+---------------------------+
| Matrix mult             | ``A * B``                 | ``A * B``                 |
+-------------------------+---------------------------+---------------------------+
| Solve Ax=b              | ``A \ b``                 | ``inv(A)*b``              |
+-------------------------+---------------------------+---------------------------+
| Eigenvalues             | ``eig(A)``                | ``eig(A)``                |
+-------------------------+---------------------------+---------------------------+
| Column means            | ``mean(A)``               | ``meanc(A)``              |
+-------------------------+---------------------------+---------------------------+
| Column sums             | ``sum(A)``                | ``sumc(A)``               |
+-------------------------+---------------------------+---------------------------+
| Print                   | ``disp(x)``               | ``print x``               |
+-------------------------+---------------------------+---------------------------+
| Comment                 | ``% comment``             | ``// comment``            |
+-------------------------+---------------------------+---------------------------+

Common Gotchas
--------------

1. **Semicolons are required.** Every statement must end with ``;``

2. **Braces not brackets.** Matrices use ``{ }`` not ``[ ]``

3. **Dot not colon.** "All rows" is ``A[.,1]`` not ``A(:,1)``

4. **No backslash.** Use ``inv(A)*b`` instead of ``A\b``

5. **String quotes.** Only double quotes ``"string"`` work

6. **Procedure syntax.** Use ``proc``/``endp``/``retp`` not ``function``/``end``/``return``

7. **Local variables.** Declare with ``local`` inside procedures

What's Next?
------------

- :doc:`../getting-started/quickstart` — General GAUSS introduction
- :doc:`../getting-started/running-existing-code` — If you have existing code
- `NumPy for MATLAB Users <https://numpy.org/doc/stable/user/numpy-for-matlab-users.html>`_ — Similar guide that inspired this one

.. seealso::

    :func:`loadd`, :func:`olsmt`, :func:`inv`, :func:`eig`, :func:`rndn`
