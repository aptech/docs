Structures
===============================================

Structures group related data into a single variable. In GAUSS, they
serve two primary purposes: bundling configuration options for a
function call (a *control structure*), and bundling the results that a
function returns (an *output structure*). Nearly every estimation
function in GAUSS follows this pattern.

::

    // 1. Create a control structure with default settings
    struct olsmtControl ctl;
    ctl = olsmtControlCreate();

    // 2. Change the settings you need
    ctl.output = 1;

    // 3. Call the estimation function
    struct olsmtOut out;
    out = olsmt(getGAUSSHome("examples/credit.dat"), "Limit ~ Income + Rating", ctl);

    // 4. Examine the results in the output structure
    print "Coefficients:";
    print out.b;

    print "Standard errors:";
    print out.stderr;

    print "R-squared:";
    print out.rsq;

If you have used :func:`olsmt`, :func:`glm`, :func:`quantileFit`, or
any of the time series functions, you have already used structures.
This page explains how structures work, how to define your own, and how
to get the most out of the control/output pattern.


The Control Structure Pattern
-----------------------------------------

The most important thing to understand about structures in GAUSS is the
**control-in, output-out** pattern. This is how almost all estimation
and modeling functions work:

1. Create a control structure filled with sensible defaults.
2. Override only the members you want to change.
3. Pass the control structure to the estimation function.
4. Receive an output structure containing the results.

The following example demonstrates this workflow with :func:`olsmt`.

Example: OLS with control and output structures
+++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load data
    fname = getGAUSSHome("examples/credit.dat");

    // Step 1: Create a control structure with defaults
    struct olsmtControl ctl;
    ctl = olsmtControlCreate();

    // Step 2: Change settings
    ctl.output = 1;         // Print a full report
    ctl.cov = "hac";        // HAC (Newey-West) standard errors
    ctl.con = 1;            // Include an intercept (default)

    // Step 3: Call olsmt with the control structure
    struct olsmtOut out;
    out = olsmt(fname, "Balance ~ Income + Rating + Cards", ctl);

    // Step 4: Examine output members
    print "Coefficient estimates:";
    print out.b;

    print "Standard errors:";
    print out.stderr;

    print "R-squared = " out.rsq;
    print "Durbin-Watson = " out.dwstat;

.. tip::

    You do not have to set every member of the control structure. The
    ``Create`` function fills every member with a sensible default. Only
    override the settings you need.

Common control and output structures
+++++++++++++++++++++++++++++++++++++++

Many GAUSS functions follow the same naming convention:

.. list-table::
    :widths: 25 25 25 25
    :header-rows: 1

    * - Function
      - Control Structure
      - Create Function
      - Output Structure

    * - :func:`olsmt`
      - ``olsmtControl``
      - :func:`olsmtControlCreate`
      - ``olsmtOut``

    * - :func:`glm`
      - ``glmControl``
      - :func:`glmControlCreate`
      - ``glmOut``

    * - :func:`quantileFit`
      - ``qfitControl``
      - :func:`qfitControlCreate`
      - ``qfitOut``

    * - :func:`gmmFit`
      - ``gmmControl``
      - :func:`gmmControlCreate`
      - ``gmmOut``

    * - :func:`plotXY`
      - ``plotControl``
      - :func:`plotGetDefaults`
      - (none)


Defining Structures
-----------------------------------------

A structure definition lists the name and type of each member. The
syntax is:

::

    struct my_struct {
        scalar count;
        matrix data;
        string label;
        string array names;
    };

Member types
++++++++++++++++++++++++++++++

A structure can contain members of the following types:

.. list-table::
    :widths: 20 40 40
    :header-rows: 1

    * - Type
      - Description
      - Default Value

    * - ``scalar``
      - A single numeric value. This type is unique to structures.
      - ``0``

    * - ``matrix``
      - A matrix of any size.
      - ``{}`` (empty matrix)

    * - ``array``
      - An N-dimensional array.
      - ``0`` (1-D array set to zero)

    * - ``string``
      - A single string.
      - ``""`` (empty string)

    * - ``string array``
      - An array of strings.
      - ``""`` (1x1 string array set to empty)

    * - ``struct``
      - A nested structure of another type.
      - (members initialized to their defaults)

Nested structures
++++++++++++++++++++++++++++++

Structures can contain other structures as members:

::

    struct point {
        scalar x;
        scalar y;
    };

    struct rectangle {
        struct point upper_left;
        struct point lower_right;
    };


Creating and Initializing
-----------------------------------------

Declaring an instance
++++++++++++++++++++++++++++++

To use a structure, declare an instance with the ``struct`` keyword:

::

    struct olsmtControl ctl;

If the structure type is defined in the GAUSS Run-Time Library (such as
``olsmtControl``, ``plotControl``, or ``glmControl``), no ``#include``
is needed. For custom structure types defined in a separate file, use
``#include``:

::

    #include mystruct.sdf

    struct my_struct s;

Initializing members
++++++++++++++++++++++++++++++

Members are accessed using dot notation:

::

    struct olsmtControl ctl;
    ctl = olsmtControlCreate();

    // Set individual members
    ctl.output = 1;
    ctl.cov = "hac";
    ctl.con = 0;

When a structure is first declared, all members are set to their type
defaults (scalars to ``0``, matrices to ``{}``, strings to ``""``).
However, for built-in structures you should always call the
corresponding ``Create`` function, which sets members to the correct
application defaults:

::

    // Correct: use the Create function
    struct olsmtControl ctl;
    ctl = olsmtControlCreate();

    // Also correct for plotControl
    struct plotControl plt;
    plt = plotGetDefaults("xy");


Accessing Members
-----------------------------------------

Use dot notation to read or write any member of a structure:

::

    // Write
    ctl.output = 1;
    ctl.cov = "robust";

    // Read
    print ctl.output;
    print ctl.cov;

For nested structures, chain the dots:

::

    struct rectangle r;
    r.upper_left.x = 0;
    r.upper_left.y = 10;
    r.lower_right.x = 5;
    r.lower_right.y = 0;

For arrays of structures, use indexing before the dot:

::

    struct olsmtControl ctl;
    ctl = reshape(olsmtControlCreate(), 3, 1);

    // Access the second element's 'output' member
    ctl[2].output = 1;


Structures in Procedures
-----------------------------------------

Structures can be passed to and returned from procedures, just like
matrices and strings.

Passing a structure as an argument
++++++++++++++++++++++++++++++++++++

Declare the structure type in the procedure signature:

::

    proc (1) = computeArea(struct rectangle rect);
        local width, height;
        width = rect.lower_right.x - rect.upper_left.x;
        height = rect.upper_left.y - rect.lower_right.y;
        retp(width * height);
    endp;

Structures are passed **by value**. The procedure receives a local copy
of the structure. Modifications inside the procedure do not affect the
caller's original structure.

Returning a structure
++++++++++++++++++++++++++++++

A procedure can return a structure:

::

    proc (1) = centerRectangle(struct rectangle rect);
        local width, height;
        struct rectangle centered;

        width = rect.lower_right.x - rect.upper_left.x;
        height = rect.upper_left.y - rect.lower_right.y;

        centered.upper_left.x = -width / 2;
        centered.upper_left.y = height / 2;
        centered.lower_right.x = width / 2;
        centered.lower_right.y = -height / 2;

        retp(centered);
    endp;

This is the pattern used by every GAUSS estimation function: the
function accepts a control structure and returns an output structure.


Complete Examples
-----------------------------------------

Example 1: OLS regression with custom settings
+++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load the credit dataset
    fname = getGAUSSHome("examples/credit.dat");

    // Create control structure with defaults
    struct olsmtControl ctl;
    ctl = olsmtControlCreate();

    // Customize settings
    ctl.output = 1;          // Print report
    ctl.cov = "robust";      // Heteroskedasticity-robust SEs

    // Run OLS
    struct olsmtOut out;
    out = olsmt(fname, "Balance ~ Income + Rating", ctl);

    // Access results programmatically
    print "Coefficients:";
    print out.b;

    print "Robust standard errors:";
    print out.stderr;

    print "R-squared = " out.rsq;

Example 2: GLM with output structure
+++++++++++++++++++++++++++++++++++++++

::

    // Load data and remove missing values
    fname = getGAUSSHome("examples/auto2.dta");
    df = loadd(fname, "mpg + weight + rep78");
    df = packr(df);

    // Create GLM control structure
    struct glmControl gc;
    gc = glmControlCreate();

    // Run GLM
    struct glmOut out;
    out = glm(df, "mpg ~ weight + factor(rep78)", "normal", gc);

    // Examine output -- glmOut uses nested structures
    print "Coefficients:";
    print out.coef.estimates;

    print "Standard errors:";
    print out.coef.se;

Example 3: Plotting with plotControl
+++++++++++++++++++++++++++++++++++++++

The :func:`plotControl` structure controls all visual aspects of GAUSS
plots. This is another example of the control structure pattern:

::

    // Load data
    df = loadd(getGAUSSHome("examples/auto2.dta"));

    // Create a plotControl structure with XY defaults
    struct plotControl plt;
    plt = plotGetDefaults("scatter");

    // Customize the plot
    plotSetTitle(&plt, "Fuel Economy vs. Weight");
    plotSetXLabel(&plt, "Weight (lbs)");
    plotSetYLabel(&plt, "Miles per Gallon");

    // Draw the scatter plot
    plotScatter(plt, df, "mpg ~ weight");

.. note::

    Plot control functions like :func:`plotSetTitle` take a *pointer* to
    the structure (``&plt``) rather than the structure itself. This allows
    them to modify the structure in place. See the
    `Structure Pointers`_ section below.


Defining Your Own Structures
-----------------------------------------

While most users will work with the built-in control and output
structures, you can define your own for custom procedures. The typical
pattern is:

1. Define the structure in a ``.sdf`` file.
2. Write a ``Create`` function that returns an initialized instance.
3. Write procedures that accept and return the structure.

::

    // --- mymodel.sdf ---
    struct myModelControl {
        scalar maxIters;
        scalar tol;
        scalar verbose;
    };

    struct myModelOut {
        matrix coefficients;
        matrix standardErrors;
        scalar converged;
    };

::

    // --- mymodel.src ---
    #include mymodel.sdf

    proc (1) = myModelControlCreate();
        struct myModelControl ctl;
        ctl.maxIters = 100;
        ctl.tol = 1e-8;
        ctl.verbose = 1;
        retp(ctl);
    endp;

    proc (1) = myModelEstimate(x, y, struct myModelControl ctl);
        local b, se, iter;
        struct myModelOut out;

        // ... estimation logic ...

        out.coefficients = b;
        out.standardErrors = se;
        out.converged = (iter < ctl.maxIters);
        retp(out);
    endp;


Arrays of Structures
-----------------------------------------

You can create arrays (vectors) of structures using :func:`reshape` or
vertical concatenation:

::

    // Create a 5x1 vector of DS structures
    struct DS d;
    d = reshape(dsCreate(), 5, 1);

    // Access members of individual elements
    d[1].dataMatrix = rndn(100, 3);
    d[2].dataMatrix = rndn(200, 5);

You can also concatenate individual structures:

::

    struct olsmtControl ctl1, ctl2, ctl_array;
    ctl1 = olsmtControlCreate();
    ctl2 = olsmtControlCreate();

    // Vertical concatenation
    ctl_array = ctl1 | ctl2;

    // Set different options for each
    ctl_array[1].con = 0;
    ctl_array[2].con = 1;


Structure Pointers
-----------------------------------------

A structure pointer holds the address of a structure rather than a copy
of it. Pointers are useful when you want a procedure to modify a
structure in place, avoiding the overhead of copying large structures.

Creating a pointer
++++++++++++++++++++++++++++++

::

    struct olsmtControl ctl;
    ctl = olsmtControlCreate();

    // Create a pointer to 'ctl'
    struct olsmtControl *p;
    p = &ctl;

Accessing members through a pointer
+++++++++++++++++++++++++++++++++++++

Use the arrow syntax (``->``) instead of dot notation:

::

    // These two lines have the same effect
    ctl.output = 1;
    p->output = 1;

Modifying the structure through the pointer modifies the original
structure, not a copy.

Using pointers in procedures
++++++++++++++++++++++++++++++

When a procedure takes a structure pointer, it can modify the caller's
structure directly without returning it:

::

    proc (0) = setDefaults(struct myModelControl *p);
        p->maxIters = 100;
        p->tol = 1e-8;
        p->verbose = 1;
    endp;

    struct myModelControl ctl;
    struct myModelControl *cp;
    cp = &ctl;
    setDefaults(cp);

    // 'ctl' has now been modified
    print ctl.maxIters;

This is exactly how the ``plotSet*`` functions work: they take a pointer
to a ``plotControl`` structure and modify it in place.

.. note::

    Structure pointers cannot be members of a structure. They are
    primarily used as procedure arguments to allow in-place modification.


Saving and Loading Structures
-----------------------------------------

Structures can be saved to disk and loaded back later using
:func:`saveStruct` and :func:`loadStruct`. The file is saved with an
``.fsr`` extension.

::

    // Save a structure to disk
    struct olsmtOut out;
    // ... (populate 'out' from an estimation) ...
    ret = saveStruct(out, "my_results");

    // Load it back later
    struct olsmtOut loaded;
    { loaded, ret } = loadStruct("my_results", "olsmtOut");


DS and PV Structures
-----------------------------------------

The ``DS`` (data set) and ``PV`` (parameter vector) structures are
specialized structures used primarily by the lower-level optimization
functions such as :func:`sqpSolveMT`.

DS structure
++++++++++++++++++++++++++++++

The ``DS`` structure is a container for passing data to optimization
functions. The most commonly used members are shown below:

::

    struct DS {
        scalar type;
        matrix dataMatrix;
        array dataArray;
        string dname;
        string array vnames;
    };

.. note::

    The full ``DS`` structure contains additional members
    (``endoMatrix``, ``exoMatrix``, etc.) used by specific optimization
    functions. See the :func:`dsCreate` reference page for the complete
    definition.

Create an instance with :func:`dsCreate`:

::

    struct DS d0;
    d0 = dsCreate();
    d0.dataMatrix = loadd(getGAUSSHome("examples/credit.dat"));

.. note::

    In modern GAUSS (version 16+), you can pass data matrices directly
    to optimization functions instead of wrapping them in a ``DS``
    structure. The ``DS`` structure is still supported for backward
    compatibility.

PV structure
++++++++++++++++++++++++++++++

The ``PV`` structure manages a parameter vector for optimization. It
lets you "pack" named parameter matrices into a single vector, and
"unpack" them back into their original shapes during optimization.

::

    struct PV p0;
    p0 = pvCreate();

    // Pack parameters with names
    p0 = pvPack(p0, 1.0, "constant");
    p0 = pvPack(p0, { 0.1, 0.1 }, "garch");
    p0 = pvPack(p0, { 0.1, 0.1 }, "arch");
    p0 = pvPack(p0, 0.1, "omega");

    // Later, unpack by name
    b0 = pvUnpack(p0, "constant");
    garch = pvUnpack(p0, "garch");

The ``PV`` structure also supports masked matrices (where only some
elements are free parameters) and symmetric matrices. See the reference
pages for :func:`pvPack`, :func:`pvPackm`, :func:`pvPacks`,
:func:`pvUnpack`, and :func:`pvCreate` for details.


Rules and Tips
-----------------------------------------

- **Always use the Create function.** For built-in structures, call
  the corresponding ``Create`` function (e.g.,
  :func:`olsmtControlCreate`, :func:`glmControlCreate`) to get correct
  defaults. Do not rely on the zero-initialization of a bare
  declaration.

- **Structures are passed by value.** When you pass a structure to a
  procedure, the procedure gets a local copy. Modifications inside the
  procedure do not affect the original. Use structure pointers if you
  need in-place modification.

- **Use** ``local`` **only inside procedures.** Local variables,
  including local structures, are declared with ``struct`` inside
  procedure bodies, not at global scope.

- **Structure definitions go in** ``.sdf`` **files.** By convention,
  structure definitions are saved in files with a ``.sdf`` extension
  and included with ``#include``. If the structure is part of a loaded
  library, no ``#include`` is needed.

- **Member names are case sensitive.** ``ctl.output`` and
  ``ctl.Output`` refer to different members.

- **The** ``scalar`` **type is unique to structures.** Outside of a
  structure definition, there is no ``scalar`` type in GAUSS. Inside a
  structure, ``scalar`` restricts a member to a single numeric value,
  which is more efficient than a 1x1 matrix.

.. tip::

    When exploring an unfamiliar output structure, use :func:`print` to
    display individual members. For example, after running
    :func:`olsmt`, try ``print out.b;`` to see the coefficient
    estimates, ``print out.stderr;`` for standard errors, and
    ``print out.rsq;`` for the R-squared value.


What's Next
-----------------------------------------

- Run :func:`olsmt` with a control structure and explore the members
  of the output structure.
- Try :func:`glm` for generalized linear models, which follows the same
  control-in, output-out pattern.
- Use ``plotControl`` structures to customize your plots with functions
  like :func:`plotSetTitle`, :func:`plotSetXLabel`, and
  :func:`plotSetLineColor`.

.. seealso:: Functions :func:`olsmt`, :func:`olsmtControlCreate`, :func:`glm`, :func:`glmControlCreate`, :func:`quantileFit`, :func:`pvPack`, :func:`pvUnpack`, :func:`pvCreate`, :func:`dsCreate`, :func:`saveStruct`, :func:`loadStruct`, :func:`plotGetDefaults`
