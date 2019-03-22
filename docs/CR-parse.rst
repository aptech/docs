
parse
==============================================

Purpose
----------------
Parses a string, returning a character vector of tokens.

Format
----------------
.. function:: parse(str, delim)

    :param str: 
    :type str: string consisting of a series of tokens and/or delimiters

    :param delim: 
    :type delim: NxK character matrix of delimiters that might be
        found in  str

    :returns: tok (*Mx1 character vector*) consisting of the tokens
        contained in  str. All tokens are returned; any
        delimiters found in  str are ignored.

Remarks
-------

The tokens in str must be 8 characters or less in size. This is because
they are returned in a character vector in which each element is
represented as a double precision value. If they are longer, the
contents of tok is unpredictable. Use string arrays to create arrays of
text with elements longer than 8 characters.


Examples
----------------

names = "GDP;GNP;M1;M2";
namesVec = parse(names, ";");

//The '$' is used when printing character vectors
print $namesVec;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The code above will return:

::

    GDP 
       GNP 
        M1 
        M2

obs = 1000;
names = "Age,Weight,Height";

//Create uniform random integers between 1 and 77
data1 = ceil(77 * rndu(obs,1));

//Create normal random integers centered at 100 with a 
//standard deviation of 9
data2 = ceil(100 + 9*rndn(obs,1));

//Create uniform random numbers between 0 and 60
data3 = ceil(60 * rndu(obs,1));

//Horizontally concatenate data into 'obs'x3 matrix
data = data1~data2~data3;

//Print the data using the procedure below
printStats(names, data);

//Create procedure to take our data, calculate some basic
//stats and print them
proc (0) = printStats( names, data);
   local title, vars, sepVars;

   //Set to print with 6 spaces between numbers and 0
   //digits after the decimal
   format /rd 6,0;
	
   //Create the titles to print for each column
   title = parse("var,mean,max,min", ",");
	
   //Extract the substrings from 'names' into a character 
   //array using the comma as a separator between tokens
   sepVars = parse(names, ",");
   print "-----------------------------------";
	
   //The '$' tells GAUSS to print as character data
   print $title';
   print "-----------------------------------"
   //Loop through as many times as there are rows in
   //'sepVars'
   for i( 1, rows(sepVars), 1);
      //Two semi-colons at the end of a print statement
      //prevents a new-line after the print
      print $sepVars[i];;
      print meanc(data[.,i]);;
      print maxc(data[.,i]);;	
      print minc(data[.,i]);
   endfor;
   print "-----------------------------------";
endp;
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The code above will produce output like this:

::

    -----------------------------------
       var   mean    max    min 
    -----------------------------------
       Age     38     77      1 
    Weight    101    135     75 
    Height     31     60      1 
    -----------------------------------

.. seealso:: Functions :func:`token`
