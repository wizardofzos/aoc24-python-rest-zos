/* REXX */

parse arg infile
x = bpxwunix('cat 'infile,,file.,se.)


solution = 0

do line = 1 to file.0
    /* Parsing the input file, like we almost always should */
    solution = solution + 1   /* solution = number of lines */
end

/* This is how we report to the API code */
say "solution="solution 

