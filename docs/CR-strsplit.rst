
strsplit
==============================================

Purpose
----------------
Splits a string into individual tokens.

Format
----------------
.. function:: strsplit(str,  
			   
			  			sep)

    :param str: 
    :type str: String or Nx1 string array to be split

    :param sep: string containing the
        
        character used to separate the input string into individual tokens.
    :type sep: Optional argument

    :returns: sa (*1xK or NxK string array*) .

Remarks
-------

**Case 1: No supplied separator**
If strsplit is called with only one input (i.e. a separator is not
passed in as the second argument), each of the following characters are
considered delimiters:

+-----------------+----------+
| space           | ASCII 32 |
+-----------------+----------+
| tab             | ASCII 9  |
+-----------------+----------+
| comma           | ASCII 44 |
+-----------------+----------+
| newline         | ASCII 10 |
+-----------------+----------+
| carriage return | ASCII 13 |
+-----------------+----------+

The input string will be split at each occurence of ANY of the
separators listed in the table above. For example:

::

       sa = "alpha 1,beta 2,gamma 3";
       strsplit(s); 

will return a 1x6 string array with the following contents:

::

       "alpha"    "1"       "beta"    "2"    "gamma"    "3"        

Tokens containing delimiters must be enclosed in single or double quotes
or parentheses. Tokens enclosed in single or double quotes will NOT
retain the quotes upon translation. Tokens enclosed in parentheses WILL
retain the parentheses after translation. Parentheses cannot be nested.

**Case 2: Supplied separator**
If a separator is passed to strsplit, the input string will be split
into individual tokens at each instance of the specified separator. Only
the supplied separator will be used to separate the tokens. Separators
may only be 1 character. Any remaining white-space will be preserved.
For example:

::

       strsplit("alpha 1,beta 2,gamma 3", ","); 

will return a 1x3 string array with the following contents:

::

       "alpha 1"    "beta 2"   "gamma 3"   

Rows with fewer tokens will be padded on the right. For example:

::

       string s  = { "1982-04-19", "1994-06" };
       strsplit(s, "-");

will return:

::

       "1982"    "04"       "19"
       "1994"    "06"         ""   


Examples
----------------

Dates
+++++

::

    dt = "1977/04/03";
    dt_split = strsplit(dt, "/");

After the code above, dt_split will be a 1x3 string array with the following contents:

::

    "1977"    "04"    "03"

Comma-separated list of variables
+++++++++++++++++++++++++++++++++

::

    vars = "CPI,PPI,Employment,Oil:Brent blend,Oil:WTI";
    vars = strsplit(vars, ",");

After the code above, vars will be a 1x5 string array with the following contents:

::

    "CPI"    "PPI"    "Employment"    "Oil:Brent blend"    "Oil:WTI"

String array with supplied separator
++++++++++++++++++++++++++++++++++++

::

    // Create a 3x1 string array
    string dow_str = { "apple:technology",
                       "goldman sachs:finance",
                       "home depot:retail" };
    			
    // Split 'dow_str' into a 3x2 string array 
    dow_sa = strsplit(dow_str, ":");

The above code sets dow_sa to be equal to:

::

    "apple"           "technology"		
    "goldman sachs"   "finance"
    "home depot"      "retail"

String array without supplied separator
+++++++++++++++++++++++++++++++++++++++

Elements that contain spaces may be grouped with single tics, like this:

::

    ss = "classification 'scientific taxonomy'";
    ss2 = strsplit(ss);
    
    print "ss2[1] = " ss2[1];
    print "ss2[2] = " ss2[2];

In this program, 'scientific taxonomy' is kept as one token, and thus the output from the above code is:

::

    ss2[1] = classification
    ss2[2] = scientific taxonomy

String array with multi-character delimiter
+++++++++++++++++++++++++++++++++++++++++++

::

    ss = "h5://example.h5";
    ss2 = strsplit(ss, "://");
    
    print "ss2[1] = " ss2[1];
    print "ss2[2] = " ss2[2];

The output from the above code is:

::

    ss2[1] = h5 
    ss2[2] = example.h5

.. seealso:: Functions :func:`strsplitPad`
