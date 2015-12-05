To solve an instance of the TSP problem run
    python tspApprox.py <inputfile>
    
the distance of the resulting tour followed by the city id's in order of the best tour found will be output to the file <inputfile>.tour

If you would like to limit the time that the solver runs provide it with a 3rd argument in number of seconds like so f you wanted it to run for approxamatly 3 minutes
    python tspApprox.py <inputfile> 90
   
it will terminate when the time has exceded the supplied time after it has completed at least one Nearest Neighbor tour and 1 iteration of 2-opt,  for example_3 this can take up to 4 minutes.
