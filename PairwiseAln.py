import argparse
import pandas as pd


#LocalAlignment Implemented Using Smith-Waterman
def LocalAlignment(match_reward: int, mismatch_penalty: int, indel_penalty: int,
                    s: str, t: str):
    rows, cols = len(s) + 1, len(t) + 1
    score_matrix = [[0] * cols for _ in range(rows)]

    maxScore = 0
    maxI, maxJ = 0, 0

    # Fill in the matrix based on match, mismatch, and gap penalties
    for i in range(1, rows):
        for j in range(1, cols):
            match_mismatch_score = match_reward if s[i - 1] == t[j - 1] else (-mismatch_penalty)

            diagonal = score_matrix[i - 1][j - 1] + match_mismatch_score
            left = score_matrix[i][j - 1] - indel_penalty
            up = score_matrix[i - 1][j] - indel_penalty

            score_matrix[i][j] = max(diagonal, left, up, 0)
            if score_matrix[i][j] > maxScore:
                maxScore = score_matrix[i][j]
                maxI, maxJ = i, j
        
    
    alignment1, alignment2 = '', ''
    i, j = maxI, maxJ

    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        if score_matrix[i][j] == score_matrix[i - 1][j - 1] + (match_reward if s[i - 1] == t[j - 1] else (-mismatch_penalty)):
            alignment1 = s[i - 1] + alignment1
            alignment2 = t[j - 1] + alignment2
            i -= 1
            j -= 1
        elif score_matrix[i][j] == score_matrix[i - 1][j] - indel_penalty:
            alignment1 = s[i - 1] + alignment1
            alignment2 = '-' + alignment2
            i -= 1
        else:
            alignment1 = '-' + alignment1
            alignment2 = t[j - 1] + alignment2
            j -= 1
    
    return [maxScore,alignment1,alignment2]

def FastaParse(filename):
    seqDict = {}
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while len(line) != 0:
            if line[0 == '>']:
                seqDict[line] = file.readline().strip()
            line = file.readline().strip()
    file.close()
    return seqDict



'''
<seq_files> -m <match> -s <mismatch> -d <indel> -a
'''
def main():
    parser = argparse.ArgumentParser(description='calculate local alignment score of given two sequences, using given match reward, mismatch penalty, and linear gap penalty')
    parser.add_argument('seq_files', metavar='seq_files', type = str, help = 'input text file that contains sequences to align')

    parser.add_argument('-m', metavar = 'INT', type = int, help = 'custom match reward')
    parser.add_argument('-s', metavar = 'INT', type = int, help = 'custom mismatch penalty')
    parser.add_argument('-d', metavar = 'INT', type = int, help = 'custom indel penalty (linear)')
    parser.add_argument('-a', action = 'store_const', const=True, default=False, help = 'show actual alignment itself')
    args = parser.parse_args()
    filename = args.seq_files
    seqs = FastaParse(filename)
    
    m,s,d = args.m, -args.s, -args.d

    alnScores = {}
    for seq in seqs:
        alnScores[seq] = {}
        toPopulate = {other for other in seqs if other != seq}
        for i in toPopulate:
            alnScores[seq][i] = {'Score' : None, 'Alignment' : None}

    for seq in alnScores:
        for i in alnScores[seq]:
            if alnScores[seq][i]['Score'] == None and alnScores[seq][i]['Alignment'] == None:
                print('aligning ' +seq +' with ' + i)
                
                score, alignment1, alignment2 = LocalAlignment(m,s,d,seqs[seq],seqs[i])
                alnScores[seq][i] = {'Score' : score, 'Alignment' : alignment1}
                alnScores[i][seq] = {'Score' : score, 'Alignment' : alignment2}
    
    #print(seqs)
    #print(alnScores)
    print('DONE')
    scores = {}
    for outer_key, inner_dict in alnScores.items():
        scores[outer_key] = {inner_key: values['Score'] for inner_key, values in inner_dict.items()}
    df = pd.DataFrame(scores)
    df.head()
    # df = df.fillna(0)
    
    # df.to_csv('alnScoreMatrix.csv', index=True)
        
if __name__ == '__main__':
   main()
   
