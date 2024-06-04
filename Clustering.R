

# Read the CSV file
similarity_matrix <- read.csv("/Users/siyanlin/Documents/GitHub/CSE185-Final-Project/symmetric_matrix_Normalized.csv")
dissimilarity_matrix <- read.csv("/Users/siyanlin/Documents/GitHub/CSE185-Final-Project/dissimilarity_matrix.csv")
# Convert to a matrix (if needed)
similarity_matrix <- as.matrix(similarity_matrix)
dissimilarity_matrix <- as.matrix(dissimilarity_matrix)


distance_object <- as.dist(dissimilarity_matrix[, -1])

hc <- hclust(distance_object, method = "ward.D2")

