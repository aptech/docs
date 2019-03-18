
keyword
==============================================

Purpose
----------------

Begins the definition of a keyword procedure. Keywords are user-defined functions with local or global variables.

Format
----------------
.. function:: keyword name(str)

    :param name: name of the keyword. This name will be a global symbol.
    :type name: literal

    :param str: a name to be used inside the keyword to refer to
        the argument that is passed to the keyword when the keyword is called. This will always be local to the keyword, and cannot be
        accessed from outside the keyword or from other keywords or procedures.
    :type str: string

