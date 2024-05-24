# Load necessary libraries
if (!requireNamespace("ape", quietly = TRUE)) {
    install.packages("ape")
}
library(ape)

# Print the current working directory
print(getwd())

# Read the alignment score matrix from a TSV file
df <- read.csv("alnScoreMatrix.csv", sep="\t", row.names=1, header=TRUE)

# Handle missing values
df[is.na(df)] <- -Inf

# Convert the alignment scores to distances if necessary
# Assuming higher scores mean more similar
max_score <- max(df, na.rm = TRUE)
distance_matrix <- max_score - df

# Print dimensions of the distance matrix
print(dim(distance_matrix))

# Perform hierarchical clustering
hc <- hclust(as.dist(distance_matrix), method="average")

# Plot the dendrogram and save it
png(filename="hierarchical_clustering_tree.png")
plot(hc, main="Hierarchical Clustering Dendrogram", xlab="Sequences", sub="", cex=0.6)
dev.off()

# Save the tree in Newick format
tree <- as.phylo(hc)
write.tree(tree, file="hierarchical_clustering_tree.nwk")
