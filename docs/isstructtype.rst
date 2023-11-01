
isstructype
==============================================

Purpose
----------------

Returns 1 if structure matches the input type.

Format
----------------
.. function:: structure_matches = isStructType(struct, type)

    :param struct_name: Structure to check.
    :type struct_name: Struct

    :param struct_type: Structure type to check for.
    :type struct_type: String
    
    :return structure_matches: 1 if *struct_name* is type specified by *struct_type*.
    :rtype structure_matches: scalar

Examples
----------------

::

    // Create structure 
    struct plotControl plt;
    plt = plotGetDefaults("Bar");
    
    // Check if structure is olsmtControl
    isStructType(plt, "olsmtControl");

Because `plt` is a plotControl structure this returns 0.

::

    // Now check for plotControl structure
    isStructType(plt, "plotControl");

This returns 1 because `plt` is a plotControl structure. 
