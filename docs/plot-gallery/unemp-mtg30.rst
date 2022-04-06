
Time Series Plot of US Unempolyment and 30 Year Mortgage Rates
=====================================================================

.. figure:: ../_static/images/unemp-mtg3.jpg
   :scale: 50 %

Step 1: Load, preview, filter and merge data
-------------------------------------------------


::

    example_dir = getGAUSSHome() $+ "examples/";

    unemp = loadd(example_dir $+ "UNRATE.csv", "date(DATE) + UNRATE");

    // Set field width to 10 characters and print 2 after the decimal
    format /rd 10,2;
    
    // Print the first 5 observations
    head(unemp);

::

          DATE     UNRATE 
    2000-01-01       4.00 
    2000-02-01       4.10 
    2000-03-01       4.00 
    2000-04-01       3.80 
    2000-05-01       4.00


::
    
    // Compute descriptive statistics
    call dstatmt(unemp);


::

    ---------------------------------------------------------------------------------
    Variable    Mean    Std Dev    Variance      Minimum      Maximum   Valid Missing
    ---------------------------------------------------------------------------------
    
    DATE       -----      -----       -----   2000-01-01   2021-12-01     264    0 
    UNRATE     5.958      1.944       3.781          3.5         14.7     264    0 


::

    mtg = loadd(example_dir $+ "mortgage_long_form.csv", "date(DATE) + Rate + cat(Maturity)");

    head(mtg);

::

          DATE       Rate   Maturity 
    2000-01-07       8.15      30_yr 
    2000-01-14       8.18      30_yr 
    2000-01-21       8.26      30_yr 
    2000-01-28       8.25      30_yr 
    2000-02-04       8.25      30_yr

::

    call dstatmt(mtg);


::

    ------------------------------------------------------------------------------------
    Variable     Mean   Std Dev    Variance      Minimum      Maximum    Valid  Missing
    ------------------------------------------------------------------------------------
    
    DATE        -----     -----       -----   1991-08-30   2022-01-27     2740      0 
    Rate        5.113     1.668       2.783          2.1         8.89     2740      0 
    Maturity    -----     -----       -----        15_yr        30_yr     2740      0 


Before we can plot our data, we need to:
  * Remove the 15 year mortgage observations.
  * Merge the weekly mortgage data with the monthly unemployment data.

The `selif` procedure provides a convenient way to select observations if they meet a certain criteria.

::

    // Create a binary indicator variable
    // with a 1 in each row where the 
    // Maturity equals 30_yr
    is_30 = mtg[.,"Maturity"] .== "30_yr";

    // Select only 30_yr observations 
    mtg30 = selif(mtg30, is_30); 
    
    call dstatmt(mtg30);

::

    -----------------------------------------------------------------------------------
    Variable    Mean   Std Dev    Variance      Minimum      Maximum     Valid  Missing
    -----------------------------------------------------------------------------------
    
    DATE       -----     -----       -----   2000-01-07   2022-01-27      1152       0 
    Rate       4.989     1.371       1.879         2.65         8.64      1152       0 
    Maturity   -----     -----       -----        30_yr        30_yr      1152       0 


Now we can see that our mortgage data only has observations with 30 year maturity and the date range is closer to that of our unemployment data as well.

Our next step is to merge the mortgage and unmployment variables by the date variable.

::

    // Merge and sort variables based on date
    data = outerJoin(mtg30, "DATE", unemp, "DATE", "full");
    data = sortc(data, "DATE");

    head(data);


::

          DATE       Rate     UNRATE
    2000-01-01          .       4.00
    2000-01-07       8.15          .
    2000-01-14       8.18          .
    2000-01-21       8.26          .
    2000-01-28       8.25          .


Step 2:
---------------

We will start by setting the size we want our graph to be in pixels and then setting up a plotControl structure with default settings.

::

    // Set the graph size
    plotCanvasSize("px", 800 | 460);
    
    // Declare plotControl structure and
    // fill with default settings
    struct plotControl plt;
    plt = plotGetDefaults("xy");


Now we will apply our first custom settings for this graph. We use HTML below to set the title font to be bold. However, you can also use Latex to style text in your GAUSS graphs. See `plotSetTextInterpreter` for more details.

::
    
    // Set title text, font, size and color,
    // using HTML tags for bold text
    plotSetTitle(&plt, "<b>Mortgage and Unemployment Rates</b>", "Arial", 18, "#464646");



::
    
    /*
    ** X-axis settings
    */
    axes_clr = "#6E7079";
    
    // Set wdith (1 pixel) and color of x-axis line
    plotSetXPen(&plt, 1, axes_clr);
    
    // Set range of x-axis to year 2000-2023,
    // Add tick labels every 5 years
    plotSetXRange(&plt, "2000", "2023", 5, "years");
    
    // Turn off x-axis label
    plotSetXLabel(&plt, " ");
    

::

    /*
    ** Y-axis settings
    */
    
    // Turn off y-axis line by setting
    // width to 0 pixels
    plotSetYPen(&plt, 0);
    
    // Enable y-axis major grid lines
    // that are 1 pixel wide, a light gray
    // color (#ccc) and solid (1)
    plotSetYGridPen(&plt, "major", 1, "#ccc", 1);
    
    // Set the y-axis to range from 0-15
    // with tick labels every 3
    plotSetYRange(&plt, 0, 15, 3);


::
    
    /*
    ** Tick label settings
    */ 
    
    plotSetTicLabelFont(&plt, "Arial", 12, axes_clr);
    
    // Format the y-tick label numbers to
    // suppress trailing zeros and add a space
    // and percent sign at the end
    plotSetYTicLabel(&plt, "%g %%");


::
    
    
    /*
    ** Legend settings
    */ 
    plotSetLegend(&plt, "30 yr Mortgage" $| "Unemployment", "top left inside");
    plotSetLegendFont(&plt, "Arial", 12, "#333");
    
    // Set legend background to be
    // fully transparent (0% opacity)
    plotSetLegendBkd(&plt, 1);
    
    // Draw connected lines, ignoring missing values
    plotSetMissGap(&plt, "off");
    
    // Draw plot
    plotXY(plt, data, "Rate + UNRATE ~ DATE");


::
    
    /*
    ** Add recession bars
    */
    
    // Fill 'plt' with default bar plot settings
    plt = plotGetDefaults("bar");
    
    // Set fill style (1=solid), opacity 10%, and color
    plotSetFill(&plt, 1, 0.1, axes_clr);
    
    // Set line style to 0=off
    plotSetLineStyle(&plt, 0);
    
    // Load recession data
    usrec = loadd(getGAUSSHome() $+ "examples/USREC.csv", "date(DATE) + USREC");
    
    // Draw vertical bars over recession dates
    plotAddVBar(plt, usrec);
    
