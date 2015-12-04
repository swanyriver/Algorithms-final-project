#!/bin/bash
for f in $(ls provided/tsp_test_cases/test-input-*.txt);
do
    echo "---------------$f--------------------------------"
    echo 
    time python -u nearNBapprox.py $f 178
    head -1 $f.tour
    echo " "
    echo "  "
    echo "  "
done    

for f in $(ls provided/tsp_example_*.txt);
do   
    echo "---------------$f--------------------------------"
    echo 
    time python -u nearNBapprox.py $f
    head -1 $f.tour
    echo " "
    echo "  "
    echo "  "
done 

