#!/bin/bash
for f in $(ls provided/tsp_test_cases/test-input-*.txt);
do
    echo $f
    time python nearNBapprox.py $f 178
done    

for f in $(ls provided/tsp_example_*.txt);
do
    echo $f
   time python nearNBapprox.py $f
done 

