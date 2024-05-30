import pandas as pd
import argparse

def readSSearchResults(filename):

    alnScores = {}

    with open(filename, 'r') as file:
        lines = []

        for line in file.readlines():
            # Strip leading/trailing whitespace characters
            stripped_line = line.strip()
            
            # Skip lines that start with #
            if stripped_line.startswith('#'):
                continue
            # Process the line (for example, print it)
            
            fields = stripped_line.split('\t')
            lines.append(fields)
        lines = sorted(lines, key=lambda x: (x[0], x[1]))
        for fields in lines:
            if fields[0] not in alnScores:
                alnScores[fields[0]] = {fields[1]:fields[-1]}
            else:
                alnScores[fields[0]][fields[1]] = fields[-1]
            
    return alnScores
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='construct Bitscore Matrix from given ssearch results file')
    parser.add_argument('seq_files', metavar='seq_files', type = str, help = 'input text file that contains sequences to align')
    args = parser.parse_args()
    filename = args.seq_files
    scores = readSSearchResults(filename)
    df = pd.DataFrame(scores)
    df.to_csv('BitScoreMatrix.csv', index=True)
