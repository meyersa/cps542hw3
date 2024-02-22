#!/bin/bash

# Run sorting algorithms
python3 -u sortingAlg.py "inp-1000k/infile1.dat" "results/output1" 1000000 0 1 1 1
wait

python3 -u sortingAlg.py "inp-1000k/infile2.dat" "results/output2" 1000000 0 1 1 1
wait

python3 -u sortingAlg.py "inp-1000k/infile3.dat" "results/output3" 1000000 0 1 1 1
wait

python3 -u sortingAlg.py "inp-1000k/infile4.dat" "results/output4" 1000000 0 1 1 1
wait

# Trigger curl command
curl -X POST -H "Content-Type: application/json" -d '{"content":null,"embeds":[{"title":"CPS542 PyAlgComp","description":"Finished running algorithms","color":null}],"attachments":[]}' $WEBHOOK_URL
