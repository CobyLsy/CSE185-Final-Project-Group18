# CSE185-Final-Project-Group-18

> Ritviksiddha Penchala, Coby Lin
>

## Project Goal

We’d like to implement an alternative approach to the computationally expensive and relatively fast method of using hiearchichal clustering to categorize sequences from data, which corresponds to the **RAxML** tool in lab7. This approach relies on exhaustive pairwise alignment and its resulting bit-scores to perform hiearchical clustering on sequences from the dataset, which trades accuracy down to protein level for speed and simplicity in implementation, while still retaining accuracy in family level on the resulting tree. We will visualize the resulting tree from our approach, for comparison with the phylogenetic tree in order to prove the family level accuracy.

## WorkFlow

1. Perform pairwise alignments instead of multiple sequence alignments on the input fasta file containing sequences.
2. Obtain a dissimilarity matrix from similarity matrix (of bitscores) yielded by the alignment process.
3. Perform hiearchical clustering based on the dissimilarity matrix of sequences in order to categorize them, and save the result into a **newick** tree file(identical in format to that of lab7)
4. Visualize the resulting tree to compare with/benchmark against the results of lab 7 (the phylogenic approach using multiple sequence alignment and **RAxML**).

## How to Run

1. Pairwise Smith Waterman Bitscore Matrix Using External Tool:
   - Package Required: **Fasta36**
   - Package Installation Command, Using **Homebrew**: `brew install brewsci/bio/fasta`
   - Run SSearch on sample sequence file: `ssearch36 -m 8C test_data/pone.0192851.s009.faa test_data/pone.0192851.s009.faa > ssearchResults.txt`. See **ssearchResults.txt** for sample result of aligning sequences in `test_data/pone.0192851.s009.faa`
   - Call: `python BitscoreParse.py ssearchResults.txt` to generate the bitscore matrix from the sample result.\
2. (Not Used in Workflow) Pairwise Smith Waterman Alignment Score Matrix With Our Own Implementation:
   - Format: `python PairwiseAln.py <fasta_file> -m <match Reward> -s <mismatch Penalty> -d <indel Penalty>`
   - Example: `python PairwiseAln.py test_data/pone.0192851.s009.faa -m 1 -s -10 -d -2`
   - Example Output: **alnScoreMatrix.csv** File that shows pairwise local alignment results between every sequence in the input fasta file.
3. Processibng of BitScoreMatrix for Clustering:
   - `python BitscoreParse.py ssearchResultFile` to generate similarity matrix and dissimilarity matrix based on our normalization process.
   - Example: `python BitscoreParse.py ssearchResults.txt`
   - Example Output: **BitScoreMatrixRaw.csv** - the raw bit score matrix, **symmetric_matrix_Normalized.csv** - the similarity matrix, and **dissimilarity_matrix.csv** - the dissimilarity matrix.
4. Hiearchical Clustering and Visualization: 
   - Our R file Clustering.R performs hiearchical clustering using [agnes](https://www.rdocumentation.org/packages/cluster/versions/2.1.6/topics/agnes), and generates a **newick** tree file;
   - Example Output: **TreeOutputDiss**
