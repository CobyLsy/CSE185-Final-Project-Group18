
library(ape)
library(cluster)

# Read the CSV file
similarity_matrix <- read.csv("/Users/siyanlin/Documents/GitHub/CSE185-Final-Project/symmetric_matrix_Normalized.csv")
dissimilarity_matrix <- read.csv("/Users/siyanlin/Documents/GitHub/CSE185-Final-Project/dissimilarity_matrix.csv")
# Convert to a matrix (if needed)
similarity_matrix <- as.matrix(similarity_matrix)
dissimilarity_matrix <- as.matrix(dissimilarity_matrix[, -1])

aggTree <- agnes(as.dist(dissimilarity_matrix), diss = T, method = "ward")
aggDend <- as.hclust(aggTree)
phy <- as.phylo(aggDend)
write.tree(phy, file = "TreeOutputDiss")
