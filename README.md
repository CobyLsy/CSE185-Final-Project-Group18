# CSE185-Final-Project-Group-18

> Ritviksiddha Penchala, Coby Lin
>

## Project Goal

We’d like to implement an alternative approach to the computationally expensive and relatively fast method of using hiearchichal clustering to categorize sequences from data, which corresponds to the **RAxML** tool in lab7. This approach relies on exhaustive pairwise alignment and its resulting bit-scores to perform hiearchical clustering on sequences from the dataset, which trades accuracy down to protein level for speed and simplicity in implementation, while still retaining accuracy in family level on the resulting tree. We will visualize the resulting tree from our approach, for comparison with the phylogenetic tree in order to prove the family level accuracy.

## WorkFlow

1. Perform pairwise alignments instead of multiple sequence alignments on the input fasta file containing sequences.
2. Obtain a dissimilarity matrix from similarity matrix yielded by the alignment process.
3. Perform hiearchical clustering based on the dissimilarity matrix of sequences in order to categorize them, and save the result into a **newick** tree file(identical in format to that of lab7)
4. Visualize the resulting tree to compare with/benchmark against the results of lab 7 (the phylogenic approach using multiple sequence alignment and **RAxML**).

## How to Run

  - Format: `python PairwiseAln.py <fasta_file> -m <match Reward> -s <mismatch Penalty> -d <indel Penalty>` 
  - Example: `python PairwiseAln.py test_data/pone.0192851.s009.faa -m 1 -s -10 -d -2`
  - Example Output: **alnScoreMatrix.csv** File that shows pairwise local alignment results between every sequence in the input fasta file.
