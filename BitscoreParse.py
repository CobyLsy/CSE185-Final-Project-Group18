import pandas as pd
import argparse
import copy

def readSSearchResults(filename):

    alnScores = {}

    with open(filename, 'r') as file:
        lines = []

        for line in file.readlines():
            if line.startswith('#'):
                continue

            # Strip leading/trailing whitespace characters
            stripped_line = line.strip()
            
            # Process the line (for example, print it)
            
            fields = stripped_line.split('\t')
            lines.append(fields)
        
        for fields in lines:
            if fields[0] not in alnScores:
                alnScores[fields[0]] = {fields[1]:float(fields[-1])}
            else:
                if fields[1] in alnScores[fields[0]] and alnScores[fields[0]][fields[1]] > float(fields[-1]):
                    continue
                else:
                    alnScores[fields[0]][fields[1]] = float(fields[-1])
    return alnScores

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='construct Bitscore Matrix from given ssearch results file')
    parser.add_argument('seq_files', metavar='seq_files', type = str, help = 'input text file that contains sequences to align')
    args = parser.parse_args()
    filename = args.seq_files
    scores = readSSearchResults(filename)
    df = pd.DataFrame(scores)
    df.to_csv('BitScoreMatrixRaw.csv', index=True)

    header = None
    sortedDict = {}
    with open ('BitScoreMatrixRaw.csv', 'r') as file:
        header = file.readline()
        verticalHeaders = {}
        for line in file.readlines():
            line = line.strip()
            verticalHeaders[line.split(',')[0]] = line.split(',')[1:]
        
        sortedDict = dict(sorted(verticalHeaders.items()))

    file.close()

    with open ('BitScoreMatrixRaw.csv', 'w') as file:
        file.write(header)
        for key, value in sortedDict.items():
            values = ''
            for i in value:
                if i == '':
                    i = '10.0'
                values += i + ','
            values = values[:-1]
            file.write(key + ',' + values + '\n')
    file.close()

    matrix = pd.read_csv('BitScoreMatrixRaw.csv', header=None).values
    
    #symmetrize matrix
    rows, cols = matrix.shape
    for i in range(1,rows):
        for j in range(1, cols):
            matrix[i, j] = float(matrix[i, j])
            matrix[j, i] = float(matrix[j,i])
            # Step 3: Compare each element with its corresponding element in the lower triangle
            if matrix[i, j] != matrix[j, i]:
                max_value = max(matrix[i, j], matrix[j, i])
                matrix[i, j] = max_value
                matrix[j, i] = max_value
    
    '''
    #normalize matrix
    secondLargest = 0
    for i in range(1,rows):
        for j in range(1,cols):
            if j != i and matrix[i,j] > secondLargest:
                secondLargest = matrix[i,j]
    

    for i in range(1,rows):
        for j in range(1, cols):
            if i == j:
                matrix[i,j] = 1
            else:
                matrix[i,j] = matrix[i,j] / secondLargest
    '''
        
    dissimilarMatrix = copy.deepcopy(matrix)
    for i in range(1,rows):
        for j in range(1, cols):
            dissimilarMatrix[i,j] = 100 / dissimilarMatrix[i,j]

    # Convert the numpy array back to a DataFrame
    symmetric_matrix = pd.DataFrame(matrix)
    symmetric_dissimilar = pd.DataFrame(dissimilarMatrix)
    # Step 5: Save the updated matrix back to a CSV file
    output_file = 'symmetric_matrix_Normalized.csv'  # replace with your desired output file name
    symmetric_matrix.to_csv(output_file, header=False, index=False)
    symmetric_dissimilar.to_csv('dissimilarity_matrix.csv', header=False, index=False)