
msym
==============================================

Purpose
----------------

Allows the user to set the symbol that GAUSS uses when missing values
are converted to ASCII and vice versa.

Format
----------------
.. function:: msym str

    :param str: ,
        if not surrounded by quotes, is forced to
        uppercase. This is the string to be printed
        for missing values. The default is '.'.
    :type str: literal or ^string (up to 8 letters) which

Examples
----------------
In the example below, you first create simulated data. The data represents the scores that a group of students
received on a particular test and also the time that they took. For your calculations, you only want to consider
data from students that completed the test in less than 80 minutes.
The code below replaces the scores from students that took more than 80 minutes with missing
values. It uses the msym keyword to change the visual representation used for missing
values from a '.' to a 'T'. Though, note that the underlying elements are still missing values, not character or string 
elements.

::

    //Set seed for repeatable random numbers
    rndseed 543124;
    
    //Random integers with a mean of 70 and range of 20 to
    //represent time taken for test
    testTime = ceil(30 * rndu(10, 1)) + 60;
    
    //Random integers with a mean of 1000 and a standard 
    //deviation of 10
    score = ceil(10 * rndn(10, 1)) + 1000;
    
    //Maximum allowed time for test
    maxTime = 80;
    
    //Create a mask for times greater than maxTime
    mask = testTime .> maxTime;
    
    //Set scores to be missing values if testTime is greater 
    //than maxTime
    mScores = missex(score, mask);
    
    //Set missing values to print as 'T' to represent that the 
    //score was invalid because the student took too much time
    msym "T";
    
    format /rd 4,0;
    print mScores;

The code above will return:

::

    T 
    1010 
     997 
    1002 
     985 
     997 
    1007 
     995 
       T 
       T

.. seealso:: Functions :func:`print`, :func:`printfm`
