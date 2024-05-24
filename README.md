# CSE185-Final-Project-Group-18

> Ritviksiddha Penchala, Coby Lin
>

## Project Goal

## How to Run

  Format: `python PairwiseAln.py <fasta_file> -m <match Reward> -s <mismatch Penalty> -d <indel Penalty>` 
  Example: `python PairwiseAln.py test_data/pone.0192851.s009.faa -m 1 -s -10 -d -2`
  Example Output: **alnScoreMatrix.csv** File that shows pairwise local alignment results between every sequence in the input fasta file.
